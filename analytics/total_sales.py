"""
total_sales.py

Calculates total sales from the dataset.
"""

import pandas as pd
from utils.data_loader import load_data


def total_sales():

    df = load_data()

    total = df["Sales"].sum()

    return f"Total Sales: ${total:,.2f}"


if __name__ == "__main__":

    print(total_sales())