"""
analyst.py

Enterprise AI Data Analyst
Upload business datasets, ask questions in natural language, and receive AI-powered insights instantly.
"""

import streamlit as st
import pandas as pd

from transformer.predict import predict_intent

from analytics.router import execute_intent
from analytics.smart_router import execute_parsed_query
from analytics.dynamic_router import execute_dynamic_query

from utils.data_loader import set_dataframe
from utils.dataset_detector import analyze_dataset
from utils.column_mapper import normalize_columns
from utils.schema_normalizer import normalize_dataset
from utils.filters import apply_filters
from utils.export import export_csv, export_excel
from analytics.kpi_dashboard import show_kpis

from visualization.auto_visualizer import visualize
from analytics.smart_insights import generate_smart_insights
from nlp.query_parser import parse_query
from utils.pdf_export import export_pdf

from utils.chat_history import (
    initialize_chat,
    add_user_message,
    add_ai_message,
    clear_chat,
)

# =================================================
# Page Configuration
# Base theme (canvas/accent) lives in .streamlit/config.toml
# =================================================

st.set_page_config(
    page_title="Enterprise AI Data Analyst",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

# =================================================
# Enterprise BI styling
# Dark navy nav rail + light report canvas + gold accent
# =================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;600;700&display=swap');

    :root {
        --navy: #1B2A4A;
        --navy-light: #24365C;
        --gold: #F2C811;
        --canvas: #F3F2F1;
        --ink: #252423;
        --border: #E1E1E1;
    }

    html, body, [class*="css"] {
        font-family: 'Segoe UI', 'Inter', sans-serif;
    }

    html, body,
    #root,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stHeader"] {
        background-color: var(--canvas) !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1180px;
    }

    /* Force any plain markdown text (e.g. from show_kpis) to stay
       readable on the light canvas, without touching our own
       explicitly-colored classes below (topbar/tile/pill/sidebar). */
    [data-testid="stMarkdownContainer"] * {
        color: var(--ink) !important;
    }

    /* st.caption() uses a separate container and was rendering
       near-invisible on the light canvas — force a readable muted gray. */
    [data-testid="stCaptionContainer"] * {
        color: #6B6B6B !important;
    }

    /* ---------- Top bar ---------- */
    /* Contained (not full-bleed) so it never collides with
       Streamlit's own toolbar at the very top of the page. */
    .topbar {
        background: var(--navy);
        padding: 1.1rem 1.6rem;
        margin-bottom: 1.6rem;
        color: #fff;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 3px solid var(--gold);
        border-radius: 6px;
    }
    .topbar-title {
        font-size: 1.25rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        color: #fff !important;
    }
    .topbar-subtitle {
        font-size: 0.8rem;
        opacity: 0.75;
        margin-top: 0.1rem;
        color: #fff !important;
    }
    .status-pill {
        background: rgba(242, 200, 17, 0.15);
        color: var(--gold) !important;
        border: 1px solid rgba(242, 200, 17, 0.4);
        padding: 0.3rem 0.85rem;
        border-radius: 4px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.03em;
    }

    /* ---------- Report canvas cards ---------- */
    .panel {
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-radius: 4px;
        padding: 1.4rem 1.5rem;
        margin-bottom: 1.4rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .panel-title {
        font-size: 0.95rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        color: var(--navy) !important;
        border-bottom: 2px solid var(--gold);
        padding-bottom: 0.6rem;
        margin-bottom: 1rem;
        display: inline-block;
    }

    /* ---------- KPI tiles ---------- */
    .tile {
        background: #FFFFFF;
        border: 1px solid var(--border);
        border-top: 3px solid var(--navy);
        border-radius: 4px;
        padding: 1rem 1.2rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .tile-label {
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        color: #6B6B6B !important;
        margin-bottom: 0.4rem;
    }
    .tile-value {
        font-size: 1.75rem;
        font-weight: 700;
        color: var(--navy) !important;
        line-height: 1.1;
    }

    /* ---------- Badges ---------- */
    .pill {
        display: inline-block;
        padding: 0.28rem 0.75rem;
        border-radius: 4px;
        font-size: 0.76rem;
        font-weight: 700;
        background: var(--navy);
        color: #fff !important;
        letter-spacing: 0.02em;
    }
    .pill-gold {
        background: var(--gold);
        color: var(--navy) !important;
    }

    /* ---------- Buttons ---------- */
    /* Explicit background forced (not relying on Streamlit defaults),
       since dark default button backgrounds were swallowing the text. */
    .stButton > button,
    .stDownloadButton > button,
    [data-testid="stFileUploaderDropzone"] button,
    [data-testid="stBaseButton-secondary"],
    [data-testid="stBaseButton-primary"] {
        background-color: #FFFFFF !important;
        border-radius: 3px !important;
        font-weight: 600 !important;
        border: 1.5px solid var(--navy) !important;
        color: var(--navy) !important;
    }
    .stButton > button *,
    .stDownloadButton > button *,
    [data-testid="stFileUploaderDropzone"] button *,
    [data-testid="stBaseButton-secondary"] *,
    [data-testid="stBaseButton-primary"] * {
        color: var(--navy) !important;
    }
    .stButton > button:hover,
    .stDownloadButton > button:hover,
    [data-testid="stFileUploaderDropzone"] button:hover,
    [data-testid="stBaseButton-secondary"]:hover,
    [data-testid="stBaseButton-primary"]:hover {
        background-color: var(--navy) !important;
    }
    .stButton > button:hover *,
    .stDownloadButton > button:hover *,
    [data-testid="stFileUploaderDropzone"] button:hover *,
    [data-testid="stBaseButton-secondary"]:hover *,
    [data-testid="stBaseButton-primary"]:hover * {
        color: #FFFFFF !important;
    }

    /* ---------- File uploader ---------- */
    [data-testid="stFileUploaderDropzone"] {
        border-radius: 4px;
        border: 1.5px dashed #B0B0B0 !important;
        background: #FAFAFA !important;
    }
    [data-testid="stFileUploaderDropzone"] section,
    [data-testid="stFileUploaderDropzone"] span,
    [data-testid="stFileUploaderDropzone"] small,
    [data-testid="stFileUploaderDropzone"] div {
        color: var(--ink) !important;
    }

    /* ---------- Chat input ---------- */
    [data-testid="stChatInput"] {
        border-radius: 4px;
    }
    [data-testid="stChatInput"]:focus-within {
        box-shadow: 0 0 0 1px var(--navy);
    }

    /* ---------- Expander ---------- */
    [data-testid="stExpander"] {
        border-radius: 4px;
        border: 1px solid var(--border) !important;
    }

    /* ---------- Sidebar: dark nav rail ---------- */
    section[data-testid="stSidebar"] {
        background: var(--navy);
    }
    section[data-testid="stSidebar"] * {
        color: #E8EAF0 !important;
    }
    section[data-testid="stSidebar"] h2 {
        color: #fff !important;
        border-left: 3px solid var(--gold);
        padding-left: 0.6rem;
    }
    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.15);
    }
    .nav-label {
        font-size: 0.68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        opacity: 0.5;
        margin-bottom: 0.15rem;
        margin-top: 0.6rem;
    }
    .nav-value {
        font-size: 0.86rem;
        margin-bottom: 0.4rem;
    }

    .footer {
        text-align: center;
        opacity: 0.45;
        font-size: 0.78rem;
        padding-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# =================================================
# Sidebar (nav rail)
# =================================================

with st.sidebar:
    st.markdown("## AI ANALYST")
    st.caption("AI-Powered Business Analytics")

    st.markdown("---")

    st.markdown('<div class="nav-label">Status</div><div class="nav-value">System Ready</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-label">Version</div><div class="nav-value">1.0</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-label">Developers</div><div class="nav-value">Nihal · Shifana · Murshid</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-label">Project</div><div class="nav-value">Final Year Deep Learning Project</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.caption("Powered by Transformer NLP + Streamlit")

# =================================================
# Top bar
# =================================================

st.markdown("""
<div class="topbar">
    <div>
        <div class="topbar-title">Enterprise AI Data Analyst</div>
        <div class="topbar-subtitle"></div>
    </div>
    <div class="status-pill">SYSTEM READY</div>
</div>
""", unsafe_allow_html=True)

initialize_chat()

df = None
# ===============================================
# PROJECT OVERVIEW
# ===============================================

st.markdown("""
<div style="
background:#ffffff;
border:1px solid #d9dde5;
border-left:6px solid #F2C94C;
border-radius:12px;
padding:25px;
margin-bottom:25px;
box-shadow:0 4px 12px rgba(0,0,0,0.08);
">

<h2 style="color:#1B2A4A; margin-bottom:10px;">
 About the Application
</h2>

<p style="font-size:16px; color:#444; line-height:1.7;">
<b>Enterprise AI Data Analyst</b>is an AI-powered business analytics platform that enables 
users to upload CSV and Excel datasets, ask questions in natural language, 
and receive meaningful business insights without writing SQL or programming code.
</p>

<hr>

<h4 style="color:#1B2A4A;"> Key Features</h4>

<ul style="line-height:1.9; color:#444; font-size:15px;">
<li> Upload CSV & Excel datasets</li>
<li> AI-powered natural language understanding</li>
<li> Interactive business analytics</li>
<li> Intelligent business insights</li>
<li> Fast and user-friendly interface</li>
</ul>

<hr>

<p style="font-size:16px; color:#444; line-height:1.8;">
This application simplifies business data analysis by enabling users to interact with enterprise datasets using natural language. It is designed to provide AI-powered insights that support faster and more informed business decision-making.
</p>
""", unsafe_allow_html=True)

# =================================================
# PANEL: Dataset Management
# =================================================

st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown('<div class="panel-title">Dataset Management</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel dataset",
    type=["csv", "xlsx", "xls"],
    label_visibility="visible",
)

if uploaded_file is not None:

    try:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file, engine="openpyxl")

        else:
            df = pd.read_excel(uploaded_file)

        # Normalize
        df = normalize_dataset(df)

        # Apply Filters
        df = apply_filters(df)

        # Save DataFrame
        set_dataframe(df)

        # Dataset Information
        info = analyze_dataset(df)
        mapping = normalize_columns(df)

        st.success(f"**{uploaded_file.name}** loaded successfully.")

        # -----------------------------------
        # KPI Dashboard (project-provided KPIs)
        # -----------------------------------
        show_kpis()

        st.write("")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="tile">
                <div class="tile-label">Rows</div>
                <div class="tile-value">{info['rows']:,}</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="tile">
                <div class="tile-label">Columns</div>
                <div class="tile-value">{info['columns']}</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="tile">
                <div class="tile-label">File</div>
                <div class="tile-value" style="font-size:1.1rem;">{uploaded_file.name}</div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")

        with st.expander("View Detected Columns"):
            st.json(mapping)

        with st.expander("Dataset Preview", expanded=False):
            st.caption(f"Showing first **{min(20, len(df))}** of **{len(df):,}** rows")
            st.dataframe(
                df.head(20),
                use_container_width=True,
                height=350,
            )

    except Exception as e:
        st.error(f"Error loading file: {str(e)}")

st.markdown('</div>', unsafe_allow_html=True)

# =================================================
# PANEL: Conversation
# =================================================

st.markdown('<div class="panel">', unsafe_allow_html=True)

hist_col1, hist_col2 = st.columns([8, 2])
with hist_col1:
    st.markdown('<div class="panel-title">Conversation</div>', unsafe_allow_html=True)
with hist_col2:
    if st.button("Clear History", use_container_width=True):
        clear_chat()
        st.rerun()

if st.session_state.messages:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
else:
    st.caption("No conversation yet — upload a dataset above and ask a question below to get started.")

st.markdown('</div>', unsafe_allow_html=True)

# =================================================
# PANEL: AI Business Assistant
# =================================================

st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown('<div class="panel-title">AI Business Assistant</div>', unsafe_allow_html=True)

question = st.chat_input("Ask a business question about your data...")

if question:

    if df is None:
        st.warning("Please upload a dataset first.")

    else:

        add_user_message(question)

        with st.chat_message("user"):
            st.write(question)

        try:

            # -----------------------------
            # Intent Prediction
            # -----------------------------
            intent, confidence = predict_intent(question)

            # -----------------------------
            # Query Parsing
            # -----------------------------
            parsed_query = parse_query(question)

            # -----------------------------
            # Dynamic Router
            # -----------------------------
            result = execute_dynamic_query(parsed_query)

            # -----------------------------
            # Smart Router
            # -----------------------------
            if result is None:
                result = execute_parsed_query(parsed_query)

            # -----------------------------
            # Transformer Router
            # -----------------------------
            if result is None:
                result = execute_intent(intent)

            # -----------------------------
            # Dashboard
            # -----------------------------
            if intent == "dashboard_summary":
                add_ai_message(question)
                st.stop()

            # -----------------------------
            # Assistant Response
            # -----------------------------
            with st.chat_message("assistant"):

                pcol1, pcol2 = st.columns(2)
                with pcol1:
                    st.markdown(f'<span class="pill">INTENT: {intent}</span>', unsafe_allow_html=True)
                with pcol2:
                    st.markdown(f'<span class="pill pill-gold">CONFIDENCE: {confidence:.2f}%</span>', unsafe_allow_html=True)

                st.write("")

                with st.expander("Query Analysis"):
                    st.json(parsed_query)

                st.divider()

                if result is not None:

                    # Visualization
                    visualize(intent, result)

                    # Smart AI Insights
                    insights = generate_smart_insights(intent, result)

                    if insights:
                        st.divider()
                        st.markdown("**AI Business Insights**")
                        for insight in insights:
                            st.info(insight)

                    # Export Results
                    if isinstance(result, pd.DataFrame):

                        st.divider()
                        st.markdown("**Export Reports**")

                        col1, col2, col3 = st.columns(3)

                        with col1:
                            export_csv(result)

                        with col2:
                            export_excel(result)

                        with col3:
                            export_pdf(
                                question=question,
                                intent=intent,
                                result=result,
                                insights=insights
                            )

                    add_ai_message(question)

                else:
                    st.warning("No result found for this query.")

        except Exception as e:
            st.error(f"{e}")

st.markdown('</div>', unsafe_allow_html=True)

# =================================================
# Footer
# =================================================



st.markdown(
    '<div class="footer">Enterprise AI Data Analyst &nbsp;·&nbsp; Final Year Deep Learning Project &nbsp;·&nbsp; Version 1.0 &nbsp;·&nbsp; © 2026</div>',
    unsafe_allow_html=True,
)