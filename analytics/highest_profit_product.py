"""
highest_profit_product.py

Shows the product with the highest total profit.
"""

import pandas as pd


def highest_profit_product():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    result = (
        df.groupby("Product Name")["Profit"]
        .sum()
        .reset_index()
        .sort_values("Profit", ascending=False)
        .head(1)
    )

    return result


if __name__ == "__main__":
    print(highest_profit_product())