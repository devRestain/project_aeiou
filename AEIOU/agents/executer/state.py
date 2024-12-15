from typing_extensions import TypedDict, Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages


class execState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
