"""
inventory_summary.py

Provides a summary of products and quantities sold.
"""

import pandas as pd


def inventory_summary():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    summary = {
        "Total Products": df["Product Name"].nunique(),
        "Total Categories": df["Category"].nunique(),
        "Total Sub-Categories": df["Sub-Category"].nunique(),
        "Total Quantity Sold": int(df["Quantity"].sum()),
    }

    return pd.DataFrame(summary.items(), columns=["Metric", "Value"])


if __name__ == "__main__":
    print(inventory_summary())