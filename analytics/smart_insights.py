"""
smart_insights.py

Generate intelligent business insights from analytics results.
"""

from unittest import result

import pandas as pd

from analytics import insights


def generate_smart_insights(intent, result):

    insights = []

    # -----------------------------
    # DataFrame Results
    # -----------------------------
    if isinstance(result, pd.DataFrame):

        if result.empty:
            return ["No records found."]

        insights.append(f"Returned {len(result)} records.")

        # Sales column
        if "Sales" in result.columns:

            total = result["Sales"].sum()
            avg = result["Sales"].mean()

            insights.append(f"Total Sales: ${total:,.2f}")
            insights.append(f"Average Sales: ${avg:,.2f}")

            if len(result) > 0:
                top = result.iloc[0]
                first_col = result.columns[0]

                insights.append(
                    f"Top {first_col}: {top[first_col]} (${top['Sales']:,.2f})"
                )

        # Profit column
        if "Profit" in result.columns:

            profit = result["Profit"].sum()

            insights.append(
                f"Total Profit: ${profit:,.2f}"
            )

            if profit < 0:
                insights.append(
                    "⚠️ Overall profit is negative."
                )

    # -----------------------------
    # Text Results
    # -----------------------------
    elif isinstance(result, str):

        insights.append(result)

    # -----------------------------
    # Intent-specific Recommendations
    # -----------------------------
    if intent == "top_customers":

        insights.append(
            "💡 Consider rewarding top customers with loyalty programs."
        )

    elif intent == "top_products":

        insights.append(
            "💡 Keep high-demand products well stocked."
        )

    elif intent == "monthly_sales":

        insights.append(
            "📈 Monitor seasonal trends to improve forecasting."
        )

    elif intent == "category_profit":

        insights.append(
            "📊 Focus marketing on high-profit categories."
        )
    # -----------------------------
    # Numeric Results
    # -----------------------------
    elif isinstance(result, (int, float)):

        insights.append(f"Computed Value: {result:,.2f}")

    # -----------------------------
    # Default Insight
    # -----------------------------
    if not insights:
        insights.append(
            "No specific business insights could be generated."
        )

    return insights