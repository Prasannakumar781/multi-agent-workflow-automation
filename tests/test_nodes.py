from src.agents.scout import scout_node
from src.agents.analyst import analyst_node
from src.agents.strategist import strategist_node
from src.agents.auditor import auditor_node

def test_scout_node():
    result = scout_node({})
    assert "competitor_data" in result
    assert len(result["competitor_data"]) > 0

def test_analyst_node():
    state = {
        "competitor_data": [{"product": "Widget A", "competitor": "Store X", "price": 19.99}]
    }
    result = analyst_node(state)
    assert "cleaned_data" in result
    assert "internal_data" in result

def test_strategist_node():
    state = {
        "cleaned_data": [{"product": "Widget A", "competitor": "Store X", "price": 19.99}],
        "internal_data": [{"product": "Widget A", "cost": 12.0, "target_margin": 0.25}]
    }
    result = strategist_node(state)
    assert "strategy_draft" in result
    assert "proposals" in result["strategy_draft"]

def test_auditor_node():
    state = {
        "strategy_draft": {
            "proposals": [{"product": "Widget A", "cost": 12.0, "suggested_price": 15.0}]
        }
    }
    result = auditor_node(state)
    assert "approved" in result