from typing import Any
from src.schemas.models import StrategyDraft, PricingProposal

def strategist_node(state: dict[str, Any]) -> dict[str, Any]:
    cleaned_data = state.get("cleaned_data", [])
    internal_data = state.get("internal_data", [])

    proposals = []
    for item in cleaned_data:
        product = item.get("product")
        competitor_price = float(item.get("price", 0))

        internal_match = next((x for x in internal_data if x.get("product") == product), {})
        cost = float(internal_match.get("cost", 0))
        target_margin = float(internal_match.get("target_margin", 0))

        suggested_price = round(cost * (1 + target_margin), 2)
        proposals.append(PricingProposal(
            product=product,
            competitor_price=competitor_price,
            cost=cost,
            target_margin=target_margin,
            suggested_price=suggested_price,
        ))

    draft = StrategyDraft(
        proposals=proposals,
        notes="Draft pricing proposal generated from market and internal data."
    )

    return {"strategy_draft": draft.model_dump()}