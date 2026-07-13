"""
sales_by_segment.py

Shows total sales for each customer segment.
"""

import pandas as pd


def sales_by_segment():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    result = (
        df.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    return result


if __name__ == "__main__":
    print(sales_by_segment())