from agents.llm import model
from langchain_core.messages import AnyMessage


def just_invoke(messages: list[AnyMessage]):
    response = model.invoke(messages)
    return response.content
