from typing import Any

def auditor_node(state: dict[str, Any]) -> dict[str, Any]:
    draft = state.get("strategy_draft", {})
    proposals = draft.get("proposals", [])

    approved = True
    feedback = ""

    for proposal in proposals:
        if proposal.get("suggested_price", 0) < proposal.get("cost", 0):
            approved = False
            feedback = f"{proposal.get('product')} is priced below cost floor."
            break

    loop_count = state.get("loop_count", 0) + 1
    max_loops = state.get("max_loops", 5)

    return {
        "approved": approved,
        "audit_result": "approved" if approved else "rejected",
        "audit_feedback": feedback,
        "loop_count": loop_count,
        "max_loops": max_loops,
    }