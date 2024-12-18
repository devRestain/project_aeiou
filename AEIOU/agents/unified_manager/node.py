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
    system_prompt = (
        "당신은 중요한 고객에게 고용된 개인 비서입니다."
        "고객의 말을 주의 깊게 파악하여, 적절한 전문가에게 도움 요청을 보내야 합니다."
        "advisor는 고객이 어떤 일을 하고자 할 때, 또는 계획을 세우려 할 때 적절한 조언을 줄 수 있는 전문가입니다."
        "executer는 인터넷 검색, 문서 처리, 숫자 계산에 탁월한 전문가입니다."
        "interpretor는 고객이 감정적이고 개인적인 표현을 나타낼 때 도움을 줄 수 있는 전문가입니다."
        "organizer는 고객의 시간 관리를 전적으로 전담하는 전문가입니다."
        "당신의 업무는 전문가에게 요청을 전달하는 것입니다."
        "그러나 고객이 위 업무에 포함되지 않는 잡담을 건넨다면 스스로 적절히 반응하십시오."
        "당신은 일을 완벽히 수행하면 보너스를 받게 될 것이지만, 나쁜 성과를 낸다면 해고될 수 있습니다."
    )
    messages = [{"role": "system", "content": system_prompt}] + state["messages"]
    target_agent_nodes = ["advisor", "executer", "interpretor", "organizer", "__end__"]
    response = generate_response(messages, target_agent_nodes)
    ai_msg = {"role": "ai", "content": response["response"], "name": "unified_manager"}
    return Command(goto=response["goto"], update={"messages": ai_msg})
