from src.graphs.workflow import build_graph

def main():
    app = build_graph()

    initial_state = {
        "input_data": {"task": "competitive pricing review"},
        "loop_count": 0,
        "max_loops": 5,
        "approved": False,
        "human_approval": True,
    }

    result = app.invoke(initial_state)
    print(result)

if __name__ == "__main__":
    main()