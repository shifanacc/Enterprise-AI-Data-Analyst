"""
category_profit.py

Shows total profit for each category.
"""

import pandas as pd


def category_profit():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    result = (
        df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
        .sort_values("Profit", ascending=False)
    )

    return result


if __name__ == "__main__":
    print(category_profit())