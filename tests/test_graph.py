from langgraph.checkpoint.memory import MemorySaver
from src.graphs.workflow import build_graph

def test_graph_runs():
    app = build_graph(checkpointer=MemorySaver())
    state = {
        "input_data": {"task": "competitive pricing review"},
        "loop_count": 0,
        "max_loops": 5,
        "approved": False,
        "human_approval": True,
    }
    config = {"configurable": {"thread_id": "test-thread"}}
    result = app.invoke(state, config=config)
    assert "strategy_draft" in result
    assert "audit_result" in result