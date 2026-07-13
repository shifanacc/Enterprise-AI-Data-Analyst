"""
shipping_analysis.py

Analyzes average shipping time by ship mode.
"""

import pandas as pd


def shipping_analysis():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    # Ensure dates are datetime
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Calculate shipping days
    df["Shipping Days"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    result = (
        df.groupby("Ship Mode")["Shipping Days"]
        .mean()
        .reset_index()
        .rename(columns={"Shipping Days": "Average Shipping Days"})
        .sort_values("Average Shipping Days")
    )

    return result


if __name__ == "__main__":
    print(shipping_analysis())