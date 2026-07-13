"""
engine.py

Generic Analytics Engine
Works with normalized datasets.
"""

import pandas as pd
import plotly.express as px

from utils.data_loader import load_data


class AnalyticsEngine:

    def __init__(self):
        self.df = load_data()

    # ---------------------------------
    # Total Sales
    # ---------------------------------
    def total_sales(self):

        if "Sales" not in self.df.columns:
            return "❌ Sales column not found."

        total = self.df["Sales"].sum()

        return f"Total Sales: ${total:,.2f}"

    # ---------------------------------
    # Average Sales
    # ---------------------------------
    def average_sales(self):

        if "Sales" not in self.df.columns:
            return "❌ Sales column not found."

        avg = self.df["Sales"].mean()

        return f"Average Sales: ${avg:,.2f}"

    # ---------------------------------
    # Total Profit
    # ---------------------------------
    def total_profit(self):

        if "Profit" not in self.df.columns:
            return "❌ Profit data not available."

        total = self.df["Profit"].sum()

        return f"Total Profit: ${total:,.2f}"

    # ---------------------------------
    # Average Profit
    # ---------------------------------
    def average_profit(self):

        if "Profit" not in self.df.columns:
            return "❌ Profit data not available."

        avg = self.df["Profit"].mean()

        return f"Average Profit: ${avg:,.2f}"

    # ---------------------------------
    # Customer Count
    # ---------------------------------
    def customer_count(self):

        if "Customer" not in self.df.columns:
            return "❌ Customer column not found."

        count = self.df["Customer"].nunique()

        return f"Total Customers: {count}"

    # ---------------------------------
    # Product Count
    # ---------------------------------
    def product_count(self):

        if "Product" not in self.df.columns:
            return "❌ Product column not found."

        count = self.df["Product"].nunique()

        return f"Total Products: {count}"

    # ---------------------------------
    # Top Customers
    # ---------------------------------
    def top_customers(self):

        if "Customer" not in self.df.columns:
            return "❌ Customer column not found."

        if "Sales" not in self.df.columns:
            return "❌ Sales column not found."

        return (
            self.df.groupby("Customer")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )
        # ---------------------------------
    # Top Products
    # ---------------------------------
    def top_products(self):

        if "Product" not in self.df.columns:
            return "❌ Product column not found."

        if "Sales" not in self.df.columns:
            return "❌ Sales column not found."

        return (
            self.df.groupby("Product")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

    # ---------------------------------
    # Monthly Sales
    # ---------------------------------
    def monthly_sales(self):

        if "Date" not in self.df.columns:
            return "❌ Date column not found."

        if "Sales" not in self.df.columns:
            return "❌ Sales column not found."

        df = self.df.copy()

        df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M").astype(str)

        return (
            df.groupby("Month")["Sales"]
            .sum()
            .reset_index()
        )

    # ---------------------------------
    # Yearly Sales
    # ---------------------------------
    def yearly_sales(self):

        if "Date" not in self.df.columns:
            return "❌ Date column not found."

        if "Sales" not in self.df.columns:
            return "❌ Sales column not found."

        df = self.df.copy()

        df["Year"] = pd.to_datetime(df["Date"]).dt.year

        return (
            df.groupby("Year")["Sales"]
            .sum()
            .reset_index()
        )

    # ---------------------------------
    # Monthly Sales Chart
    # ---------------------------------
    def monthly_sales_chart(self):

        if "Date" not in self.df.columns:
            return "❌ Date column not found."

        if "Sales" not in self.df.columns:
            return "❌ Sales column not found."

        df = self.df.copy()

        df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M").astype(str)

        monthly = (
            df.groupby("Month")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.line(
            monthly,
            x="Month",
            y="Sales",
            title="Monthly Sales Trend",
            markers=True,
        )

        return fig

    # ---------------------------------
    # Top Products Chart
    # ---------------------------------
    def top_products_chart(self):

        if "Product" not in self.df.columns:
            return "❌ Product column not found."

        if "Sales" not in self.df.columns:
            return "❌ Sales column not found."

        top = (
            self.df.groupby("Product")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            top,
            x="Product",
            y="Sales",
            color="Sales",
            title="Top 10 Products",
        )

        return fig

        # ---------------------------------
    # Dashboard Summary
    # ---------------------------------
    def dashboard_summary(self):

        summary = {}

        if "Sales" in self.df.columns:
            summary["Total Sales"] = self.df["Sales"].sum()

        if "Profit" in self.df.columns:
            summary["Total Profit"] = self.df["Profit"].sum()

        if "Customer" in self.df.columns:
            summary["Customers"] = self.df["Customer"].nunique()

        if "Product" in self.df.columns:
            summary["Products"] = self.df["Product"].nunique()

        return pd.DataFrame(
            summary.items(),
            columns=["Metric", "Value"]
        )