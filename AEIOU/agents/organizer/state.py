from typing_extensions import TypedDict, Annotated, Optional
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages


class orgState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    subject: str
    integrated_task: Optional[dict]
    time_limit: Optional[bool]
    time_table: Optional[dict]
