from langgraph.graph import StateGraph, START, END
from agents.interpretor.state import itpState
from agents.interpretor.node import (
    Subject_selector,
    Sentiment_interpretor,
    Secret_keeper,
    Sentimental_counselor,
)


builder = StateGraph(itpState)
builder.add_node("subject_selector", Subject_selector)
builder.add_node("sentiment_interpretor", Sentiment_interpretor)
builder.add_node("secret_keeper", Secret_keeper)
builder.add_node("sentimental_counselor", Sentimental_counselor)

builder.add_edge(START, "subject_selector")
builder.add_edge("subject_selector", "sentiment_interpretor")
builder.add_edge("sentimental_counselor", END)

Interpretor = builder.compile()
