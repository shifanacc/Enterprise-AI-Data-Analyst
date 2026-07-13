"""
bottom_customers.py

Shows the bottom 10 customers by sales.
"""

import pandas as pd


def bottom_customers():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    result = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=True)
        .head(10)
    )

    return result


if __name__ == "__main__":
    print(bottom_customers())