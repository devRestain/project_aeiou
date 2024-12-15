from langchain_core.messages import AnyMessage
from agents.llm import model
from agents.executer.tool import tools


def tool_invoke(messages: list[AnyMessage]):
    tool_binded_model = model.bind_tools(tools)
    response = tool_binded_model.invoke(messages)
    return response.content
