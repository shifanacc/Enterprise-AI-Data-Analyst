"""
smart_router.py

Executes analytics using the parsed query.
"""

from analytics.engine import AnalyticsEngine


def execute_parsed_query(parsed):

    engine = AnalyticsEngine()

    operation = parsed.get("operation")
    metric = parsed.get("metric")
    dimension = parsed.get("dimension")

    # -----------------------------
    # Sales
    # -----------------------------
    if metric == "sales":

        if operation == "total":
            return engine.total_sales()

        elif operation == "average":
            return engine.average_sales()

        elif operation == "top" and dimension == "product":
            return engine.top_products()

        elif operation == "top" and dimension == "customer":
            return engine.top_customers()

        elif dimension == "month":
            return engine.monthly_sales()

        elif dimension == "year":
            return engine.yearly_sales()

    # -----------------------------
    # Profit
    # -----------------------------
    if metric == "profit":

        if operation == "total":
            return engine.total_profit()

        elif operation == "average":
            return engine.average_profit()

    return None