from typing import TypedDict, Any, Optional

class WorkflowState(TypedDict, total=False):
    input_data: dict[str, Any]
    competitor_data: list[dict[str, Any]]
    cleaned_data: list[dict[str, Any]]
    internal_data: list[dict[str, Any]]
    strategy_draft: dict[str, Any]
    audit_result: str
    audit_feedback: str
    loop_count: int
    max_loops: int
    approved: bool
    error: Optional[str]
    human_approval: bool