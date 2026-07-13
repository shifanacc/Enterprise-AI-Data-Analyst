"""
top_cities.py

Shows the top 10 cities by sales.
"""

import pandas as pd


def top_cities():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    result = (
        df.groupby("City")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    return result


if __name__ == "__main__":
    print(top_cities())