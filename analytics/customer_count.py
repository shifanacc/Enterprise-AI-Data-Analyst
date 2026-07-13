"""
customer_count.py

Calculates total number of unique customers.
"""

import pandas as pd


def customer_count():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    count = df["Customer ID"].nunique()

    return f"Total Customers: {count:,}"


if __name__ == "__main__":
    print(customer_count())