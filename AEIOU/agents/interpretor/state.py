from typing_extensions import TypedDict, Annotated, Optional
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages


class itpState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    subject: str
    private: bool
    response: Optional[dict]
