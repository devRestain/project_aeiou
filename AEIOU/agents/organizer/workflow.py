from langgraph.graph import StateGraph, START, END
from agents.organizer.state import orgState
from agents.organizer.node import (
    Task_selector,
    Task_integrator,
    Time_limit_checker,
    Timetable_generator,
    Thinker,
)


builder = StateGraph(orgState)
builder.add_node("task_selector", Task_selector)
builder.add_node("task_integrator", Task_integrator)
builder.add_node("time_limit_checker", Time_limit_checker)
builder.add_node("timetable_generator", Timetable_generator)
builder.add_node("thinker", Thinker)

builder.add_edge(START, "task_selector")
builder.add_edge("task_selector", "task_integrator")
builder.add_edge("thinker", END)

Organizer = builder.compile()
