from typing import Any
from src.tools.web_fetch import fetch_competitor_prices
from src.utils.logger import logger

def scout_node(state: dict[str, Any]) -> dict[str, Any]:
    competitor_data = fetch_competitor_prices()
    logger.info("Scout fetched competitor prices")

    return {
        "competitor_data": competitor_data,
        "loop_count": state.get("loop_count", 0),
        "max_loops": state.get("max_loops", 5),
    }