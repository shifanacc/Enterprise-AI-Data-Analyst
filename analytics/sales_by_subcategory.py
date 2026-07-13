"""
sales_by_subcategory.py

Shows total sales for each subcategory.
"""

import pandas as pd


def sales_by_subcategory():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    result = (
        df.groupby("Sub-Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    return result


if __name__ == "__main__":
    print(sales_by_subcategory())