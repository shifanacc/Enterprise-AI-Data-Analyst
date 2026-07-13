"""
dynamic_engine.py

Dynamic analytics for any business dataset.
"""

import pandas as pd
from utils.data_loader import load_data


class DynamicAnalytics:

    def __init__(self):
        self.df = load_data()

    def summary(self):
        """Return dataset summary."""

        numeric = self.df.select_dtypes(include="number").columns.tolist()
        categorical = self.df.select_dtypes(exclude="number").columns.tolist()

        return {
            "rows": len(self.df),
            "columns": len(self.df.columns),
            "numeric_columns": numeric,
            "categorical_columns": categorical,
        }

    def total(self, column):

        if column not in self.df.columns:
            return None

        return self.df[column].sum()

    def average(self, column):

        if column not in self.df.columns:
            return None

        return self.df[column].mean()

    def top(self, group_column, value_column, n=10):

        if group_column not in self.df.columns:
            return None

        if value_column not in self.df.columns:
            return None

        return (
            self.df.groupby(group_column)[value_column]
            .sum()
            .sort_values(ascending=False)
            .head(n)
            .reset_index()
        )