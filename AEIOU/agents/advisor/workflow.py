from langgraph.graph import StateGraph, START, END
from agents.advisor.state import adviceState
from agents.advisor.node import (
    Advise_selector,
    Advise_distributor,
    Assigner_for_long_term,
    Assigner_for_short_term,
    Assigner_for_task,
    Advise_provider,
)


builder = StateGraph(adviceState)
builder.add_node("advise_selector", Advise_selector)
builder.add_node("advise_distributor", Advise_distributor)
builder.add_node("assigner_for_long_term", Assigner_for_long_term)
builder.add_node("assigner_for_short_term", Assigner_for_short_term)
builder.add_node("assigner_for_task", Assigner_for_task)
builder.add_node("advise_provider", Advise_provider)

builder.add_edge(START, "advise_selector")
builder.add_edge("advise_selector", "advise_distributor")
builder.add_edge("advise_provider", END)

Advisor = builder.compile()
