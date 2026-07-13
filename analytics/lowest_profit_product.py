"""
lowest_profit_product.py

Shows the product with the lowest total profit.
"""

import pandas as pd


def lowest_profit_product():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    result = (
        df.groupby("Product Name")["Profit"]
        .sum()
        .reset_index()
        .sort_values("Profit", ascending=True)
        .head(1)
    )

    return result


if __name__ == "__main__":
    print(lowest_profit_product())