"""
worst_region.py

Shows the region with the lowest sales.
"""

import pandas as pd


def worst_region():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    result = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=True)
        .head(1)
    )

    return result


if __name__ == "__main__":
    print(worst_region())