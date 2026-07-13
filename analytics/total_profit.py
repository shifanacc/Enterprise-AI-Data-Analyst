"""
total_profit.py

Calculates total profit.
"""

import pandas as pd


def total_profit():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    total = df["Profit"].sum()

    return f"Total Profit: ${total:,.2f}"


if __name__ == "__main__":
    print(total_profit())