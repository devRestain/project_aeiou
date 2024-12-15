from langgraph.graph import MessagesState
from langgraph.types import Command
from typing_extensions import Literal
from agents.llm import generate_response

"""
계획 tagging에 없는 사항 있으면 답변에 해당 부분 질문하도록 유도
"""


def Unified_manager(
    state: MessagesState,
) -> Command[Literal["advisor", "executer", "interpretor", "organizer", "__end__"]]:
    system_prompt = ""
    messages = [{"role": "system", "content": system_prompt}] + state["messages"]
    target_agent_nodes = ["advisor", "executer", "interpretor", "organizer", "__end__"]
    response = generate_response(messages, target_agent_nodes)
    ai_msg = {"role": "ai", "content": response["response"], "name": "unified_manager"}
    return Command(goto=response["goto"], update={"messages": ai_msg})
