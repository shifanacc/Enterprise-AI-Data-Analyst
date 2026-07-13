"""
kpi_dashboard.py

Professional KPI Dashboard
"""

import streamlit as st
from utils.data_loader import get_dataframe


def show_kpis():

    df = get_dataframe()

    if df is None or df.empty:
        return

    cols = st.columns(4)

    metrics = []

    # Total Sales
    if "Sales" in df.columns:
        metrics.append((
            "💰 Total Sales",
            f"${df['Sales'].sum():,.2f}"
        ))

    # Total Profit
    if "Profit" in df.columns:
        metrics.append((
            "💵 Total Profit",
            f"${df['Profit'].sum():,.2f}"
        ))

    # Orders
    metrics.append((
        "📦 Orders",
        f"{len(df):,}"
    ))

    # Customers
    if "Customer" in df.columns:
        metrics.append((
            "👥 Customers",
            f"{df['Customer'].nunique():,}"
        ))

    # Products
    elif "Product" in df.columns:
        metrics.append((
            "📦 Products",
            f"{df['Product'].nunique():,}"
        ))

    # Average Sales
    if len(metrics) < 4 and "Sales" in df.columns:
        metrics.append((
            "📈 Avg Sales",
            f"${df['Sales'].mean():,.2f}"
        ))

    for col, metric in zip(cols, metrics):
        col.metric(metric[0], metric[1])