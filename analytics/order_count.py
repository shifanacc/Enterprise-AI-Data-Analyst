"""
order_count.py

Calculates total number of unique orders.
"""

import pandas as pd


def order_count():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    count = df["Order ID"].nunique()

    return f"Total Orders: {count:,}"


if __name__ == "__main__":
    print(order_count())