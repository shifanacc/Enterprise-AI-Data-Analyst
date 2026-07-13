"""
region_profit.py

Shows total profit for each region.
"""

import pandas as pd


def region_profit():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    result = (
        df.groupby("Region")["Profit"]
        .sum()
        .reset_index()
        .sort_values("Profit", ascending=False)
    )

    return result


if __name__ == "__main__":
    print(region_profit())