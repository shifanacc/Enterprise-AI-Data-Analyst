"""
router.py

Routes Transformer intents to the Generic Analytics Engine.
"""

from analytics.engine import AnalyticsEngine
from analytics.dashboard import show_dashboard


def execute_intent(intent):

    engine = AnalyticsEngine()

    INTENT_MAP = {

        # -----------------------------
        # Sales
        # -----------------------------
        "total_sales": engine.total_sales,
        "average_sales": engine.average_sales,
        "monthly_sales": engine.monthly_sales,
        "yearly_sales": engine.yearly_sales,

        # -----------------------------
        # Profit
        # -----------------------------
        "total_profit": engine.total_profit,
        "average_profit": engine.average_profit,

        # -----------------------------
        # Customer
        # -----------------------------
        "customer_count": engine.customer_count,
        "top_customers": engine.top_customers,

        # -----------------------------
        # Product
        # -----------------------------
        "product_count": engine.product_count,
        "top_products": engine.top_products,

        # -----------------------------
        # Charts
        # -----------------------------
        "monthly_sales_chart": engine.monthly_sales_chart,
        "top_products_chart": engine.top_products_chart,

        # -----------------------------
        # Dashboard
        # -----------------------------
        "dashboard_summary": show_dashboard,
    }

    if intent in INTENT_MAP:
        return INTENT_MAP[intent]()

    return f"⚠️ Intent '{intent}' is not implemented yet."