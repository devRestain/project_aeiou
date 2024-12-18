from langgraph.graph import MessagesState, StateGraph, START, END
from agents.advisor.workflow import Advisor
from agents.executer.workflow import Executer
from agents.interpretor.workflow import Interpretor
from agents.organizer.workflow import Organizer
from agents.unified_manager.node import Unified_manager


def call_Advisor(state: MessagesState) -> MessagesState:
    input = {"messages": state["messages"]}
    output = Advisor.invoke(input)
    return {"messages": output["messages"]}


def call_Executer(state: MessagesState) -> MessagesState:
    input = {"messages": state["messages"]}
    output = Executer.invoke(input)
    return {"messages": output["messages"]}


def call_Interpretor(state: MessagesState) -> MessagesState:
    input = {"messages": state["messages"]}
    output = Interpretor.invoke(input)
    return {"messages": output["messages"]}


def call_Organizer(state: MessagesState) -> MessagesState:
    input = {"messages": state["messages"]}
    output = Organizer.invoke(input)
    return {"messages": output["messages"]}


builder = StateGraph(MessagesState)
builder.add_node("advisor", call_Advisor)
builder.add_node("executer", call_Executer)
builder.add_node("interpretor", call_Interpretor)
builder.add_node("organizer", call_Organizer)
builder.add_node("unified_manager", Unified_manager)


builder.add_edge(START, "unified_manager")
builder.add_edge("advisor", END)
builder.add_edge("executer", END)
builder.add_edge("interpretor", END)
builder.add_edge("organizer", END)

ChaeUm = builder.compile()
