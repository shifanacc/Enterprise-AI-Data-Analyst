"""
dynamic_router.py

Routes parsed queries to the Dynamic Analytics Engine.
"""

from analytics.dynamic_engine import DynamicAnalytics


def execute_dynamic_query(parsed):

    engine = DynamicAnalytics()

    operation = parsed.get("operation")
    metric = parsed.get("metric")
    dimension = parsed.get("dimension")

    # Mapping normalized metric names to dataframe columns
    metric_map = {
        "sales": "Sales",
        "profit": "Profit",
        "quantity": "Quantity",
    }

    value_column = metric_map.get(metric)

    # Total
    if operation == "total" and value_column:
        return engine.total(value_column)

    # Average
    if operation == "average" and value_column:
        return engine.average(value_column)

    # Top Products
    if operation == "top" and dimension == "product" and value_column:
        return engine.top("Product", value_column)

    # Top Customers
    if operation == "top" and dimension == "customer" and value_column:
        return engine.top("Customer", value_column)

    return None