from src.graphs.workflow import build_graph
from src.utils.db import init_db, log_event

def main():
    init_db()
    app = build_graph()

    thread_id = "thread-1"
    initial_state = {
        "input_data": {"task": "competitive pricing review"},
        "loop_count": 0,
        "max_loops": 5,
        "approved": False,
        "human_approval": True,
    }

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    log_event(thread_id, "main", "start", "workflow started")
    result = app.invoke(initial_state, config=config)
    log_event(thread_id, "main", "end", str(result))
    print(result)

if __name__ == "__main__":
    main()