"""
average_sales.py

Calculates average sales.
"""

from utils.data_loader import load_data


def average_sales():

    df = load_data()

    average = df["Sales"].mean()

    return f"Average Sales: ${average:,.2f}"


if __name__ == "__main__":
    print(average_sales())