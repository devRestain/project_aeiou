from langgraph.graph import StateGraph, START, END
from agents.executer.state import execState
from agents.executer.node import tool_node, Tool_caller, should_continue

builder = StateGraph(execState)
builder.add_node("tool_caller", Tool_caller)
builder.add_node("tools", tool_node)

builder.add_edge(START, "tool_caller")
builder.add_conditional_edges("tool_caller", should_continue, ["tools", END])
builder.add_edge("tools", "tool_caller")

Executer = builder.compile()
