from typing import Any
def analyst_node(state: dict[str, Any]) -> dict[str, Any]:
    competitor_data = state.get("competitor_data", [])

    cleaned_data = []
    for item in competitor_data:
        cleaned_data.append({
            "product": item.get("product"),
            "competitor": item.get("competitor"),
            "price": float(item.get("price", 0)),
        })

    internal_data = [
        {"product": "Widget A", "cost": 12.00, "target_margin": 0.25},
        {"product": "Widget B", "cost": 18.00, "target_margin": 0.20},
    ]

    return {
        "cleaned_data": cleaned_data,
        "internal_data": internal_data,
    }