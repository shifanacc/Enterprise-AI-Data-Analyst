import pandas as pd


def monthly_sales():

    df = pd.read_csv("datasets/business/Global Superstore.csv")

    # Parse dates
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=False,
        errors="coerce"
    )

    monthly = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
        .sum()
        .reset_index()
    )

    monthly["Order Date"] = monthly["Order Date"].astype(str)

    return monthly


if __name__ == "__main__":
    print(monthly_sales())