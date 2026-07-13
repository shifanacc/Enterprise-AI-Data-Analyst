"""
average_profit.py

Calculates average profit.
"""

from utils.data_loader import load_data


def average_profit():

    df = load_data()

    average = df["Profit"].mean()

    return f"Average Profit: ${average:,.2f}"


if __name__ == "__main__":
    print(average_profit())