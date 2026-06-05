from langgraph.graph import StateGraph, START, END
from src.schemas.state import WorkflowState
from src.agents.scout import scout_node
from src.agents.analyst import analyst_node
from src.agents.strategist import strategist_node
from src.agents.auditor import auditor_node
from src.utils.persistence import get_checkpointer

def route_after_audit(state: WorkflowState):
    if not state.get("approved"):
        return "strategist"
    if state.get("human_approval"):
        return "end"
    return "human_review"

def route_after_human(state: WorkflowState):
    return "end" if state.get("human_approval") else "strategist"

def human_review_node(state: WorkflowState):
    return state

def build_graph(checkpointer=None):
    graph = StateGraph(WorkflowState)

    graph.add_node("scout", scout_node)
    graph.add_node("analyst", analyst_node)
    graph.add_node("strategist", strategist_node)
    graph.add_node("auditor", auditor_node)
    graph.add_node("human_review", human_review_node)

    graph.add_edge(START, "scout")
    graph.add_edge("scout", "analyst")
    graph.add_edge("analyst", "strategist")
    graph.add_edge("strategist", "auditor")

    graph.add_conditional_edges(
        "auditor",
        route_after_audit,
        {
            "strategist": "strategist",
            "human_review": "human_review",
            "end": END,
        }
    )

    graph.add_conditional_edges(
        "human_review",
        route_after_human,
        {
            "strategist": "strategist",
            "end": END,
        }
    )

    if checkpointer is None:
        with get_checkpointer() as cp:
            return graph.compile(checkpointer=cp)
    return graph.compile(checkpointer=checkpointer)