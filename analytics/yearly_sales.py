"""
yearly_sales.py

Calculates yearly sales.
"""

import pandas as pd


def yearly_sales():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    yearly = (
        df.groupby("Year")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Year")
    )

    return yearly


if __name__ == "__main__":
    print(yearly_sales())