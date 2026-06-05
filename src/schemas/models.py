from pydantic import BaseModel
from typing import List

class PricingProposal(BaseModel):
    product: str
    competitor_price: float
    cost: float
    target_margin: float
    suggested_price: float

class StrategyDraft(BaseModel):
    proposals: List[PricingProposal]
    notes: str