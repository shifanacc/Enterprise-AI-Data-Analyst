"""
insights.py

Generates AI-style business insights.
"""

import pandas as pd


def generate_insights(intent, result):

    insights = []

    # -----------------------------
    # Monthly Sales
    # -----------------------------
    if intent == "monthly_sales" and isinstance(result, pd.DataFrame):

        highest = result.loc[result["Sales"].idxmax()]
        lowest = result.loc[result["Sales"].idxmin()]

        insights.append(
            f"📈 Highest sales occurred in {highest.iloc[0]} (${highest['Sales']:,.2f})."
        )

        insights.append(
            f"📉 Lowest sales occurred in {lowest.iloc[0]} (${lowest['Sales']:,.2f})."
        )

    # -----------------------------
    # Top Products
    # -----------------------------
    elif intent == "top_products" and isinstance(result, pd.DataFrame):

        top = result.iloc[0]

        insights.append(
            f"🏆 Best-selling product: {top.iloc[0]}"
        )

        insights.append(
            f"💰 Sales: ${top['Sales']:,.2f}"
        )

    # -----------------------------
    # Top Customers
    # -----------------------------
    elif intent == "top_customers" and isinstance(result, pd.DataFrame):

        top = result.iloc[0]

        insights.append(
            f"👤 Best customer: {top.iloc[0]}"
        )

        insights.append(
            f"💰 Revenue generated: ${top['Sales']:,.2f}"
        )

    return insights