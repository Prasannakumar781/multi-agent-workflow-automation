from src.utils.retry import retry_on_failure

@retry_on_failure()
def fetch_competitor_prices():
    return [
        {"product": "Widget A", "competitor": "Store X", "price": 19.99},
        {"product": "Widget B", "competitor": "Store Y", "price": 24.50},
    ]