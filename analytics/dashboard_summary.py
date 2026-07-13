"""
dashboard_summary.py

Returns key business KPIs.
"""

import pandas as pd


def dashboard_summary():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    summary = {
        "Total Sales": round(df["Sales"].sum(), 2),
        "Total Profit": round(df["Profit"].sum(), 2),
        "Average Sales": round(df["Sales"].mean(), 2),
        "Average Profit": round(df["Profit"].mean(), 2),
        "Total Orders": df["Order ID"].nunique(),
        "Total Customers": df["Customer ID"].nunique(),
        "Total Quantity": int(df["Quantity"].sum()),
    }

    return pd.DataFrame(summary.items(), columns=["Metric", "Value"])


if __name__ == "__main__":
    print(dashboard_summary())