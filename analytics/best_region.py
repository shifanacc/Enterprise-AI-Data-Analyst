"""
best_region.py

Shows the region with the highest sales.
"""

import pandas as pd


def best_region():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    result = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
        .head(1)
    )

    return result


if __name__ == "__main__":
    print(best_region())