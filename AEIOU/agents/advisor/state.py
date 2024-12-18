from typing_extensions import TypedDict, Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages


class adviceState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    focusedPlan: str
    related: str
    plans: list
