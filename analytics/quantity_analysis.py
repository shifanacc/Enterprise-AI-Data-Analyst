"""
quantity_analysis.py

Shows quantity sold by category.
"""

import pandas as pd


def quantity_analysis():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    result = (
        df.groupby("Category")["Quantity"]
        .sum()
        .reset_index()
        .sort_values("Quantity", ascending=False)
    )

    return result


if __name__ == "__main__":
    print(quantity_analysis())