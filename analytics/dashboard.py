"""
dashboard.py

Professional Dashboard
"""

import streamlit as st
from analytics.engine import AnalyticsEngine


def show_dashboard():

    engine = AnalyticsEngine()

    # --------------------------------
    # KPI Cards
    # --------------------------------
    col1, col2, col3, col4 = st.columns(4)

    sales = engine.total_sales()
    customers = engine.customer_count()
    products = engine.product_count()
    avg_sales = engine.average_sales()

    col1.metric(
        "💰 Total Sales",
        sales.replace("Total Sales: $", "")
    )

    col2.metric(
        "👥 Customers",
        customers.replace("Total Customers: ", "")
    )

    col3.metric(
        "📦 Products",
        products.replace("Total Products: ", "")
    )

    col4.metric(
        "📈 Avg Sales",
        avg_sales.replace("Average Sales: $", "")
    )

    st.divider()

    # --------------------------------
    # Monthly Sales Chart
    # --------------------------------
    st.subheader("📈 Monthly Sales Trend")

    chart = engine.monthly_sales_chart()

    if chart is not None:
        st.plotly_chart(chart, use_container_width=True)

    st.divider()

    # --------------------------------
    # Top Products
    # --------------------------------
    st.subheader("🏆 Top Products")

    product_chart = engine.top_products_chart()

    if product_chart is not None:
        st.plotly_chart(product_chart, use_container_width=True)

    st.divider()

    # --------------------------------
    # Top Customers
    # --------------------------------
    st.subheader("👥 Top Customers")

    customers_df = engine.top_customers()

    if customers_df is not None:
        st.dataframe(customers_df, use_container_width=True)

    # IMPORTANT
    return "Dashboard displayed successfully."