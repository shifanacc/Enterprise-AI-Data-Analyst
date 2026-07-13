"""
discount_analysis.py

Shows discount statistics by category.
"""

import pandas as pd


def discount_analysis():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    result = (
        df.groupby("Category")["Discount"]
        .agg(["mean", "max", "min"])
        .reset_index()
        .rename(columns={
            "mean": "Average Discount",
            "max": "Maximum Discount",
            "min": "Minimum Discount"
        })
    )

    return result


if __name__ == "__main__":
    print(discount_analysis())