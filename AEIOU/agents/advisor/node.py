from typing_extensions import Literal
from langgraph.types import Command
from agents.llm import select_node
from agents.utils import load_json, add_json
from agents.advisor.state import adviceState
from agents.advisor.utils import focused_plan, just_invoke, generate_5_details

"""
{
"작업 진행 중" : [{"이름":"어쩌구", "위계" : "장기"}]
"작업 완료" : [{"이름" : "어쩌구", "위계" : "세부", "종속" : "관련 하위 tasks", "상위" : "관련 장기 계획"}]
}

+예상 소요 시간 더하기?
"""


def Advise_selector(state: adviceState) -> adviceState:
    """
    유저가 기존 계획의 세부 계획을 세우고 싶은 건지 감지.
    """
    plans = load_json(file_path=r"../../data/user/plans.json")
    find_prompt = (
        "당신은 중요한 고객에게 고용된 분석가입니다."
        "당신은 고객의 말을 듣고, 고객이 어떤 주제에 대해 계획하려 하는지 파악해야 합니다."
        "당신은 일을 완벽히 수행하면 보너스를 받게 될 것이지만, 나쁜 성과를 낸다면 해고될 수 있습니다."
    )
    find_messages = [{"role": "system", "content": find_prompt}] + state["messages"][-1]
    focusedPlan = focused_plan(messages=find_messages, target_plans=plans["processing"])
    if focusedPlan == "new_plan":
        detect_prompt = (
            "당신은 중요한 고객에게 고용된 분석가입니다."
            "고객의 말에서 그가 새로이 계획하려는 주제를 단어 그대로 추출하세요."
            "당신은 일을 완벽히 수행하면 보너스를 받게 될 것이지만, 나쁜 성과를 낸다면 해고될 수 있습니다."
        )
        detect_messages = [{"role": "system", "content": detect_prompt}] + state[
            "messages"
        ][-1]
        focusedPlan = just_invoke(message=detect_messages)
    output = {"focusedPlan": focusedPlan, "plans": plans}
    return output


def Advise_distributor(
    state: adviceState,
) -> Command[
    Literal["assigner_for_long_term", "assigner_for_short_term", "assigner_for_task"]
]:
    system_prompt = (
        "당신은 중요한 고객에게 고용된, 결단력 있는 중간 관리자입니다."
        "당신은 고객이 집중하고 있는 계획을 확인하고, 계획의 내용에 따라 적절한 동료에게 전달해야 합니다."
        "만약 고객의 계획이 추상적이며 달성을 위해 몇 주 동안의 노력이 필요하다면, 'assigner_for_long_term'에게 전달하세요."
        "만약 고객의 계획이 구체적이며 달성을 위해 며칠 동안의 노력이 필요하다면, 'assigner_for_short_term'에게 전달하세요."
        "만약 고객의 계획이 확고하고 간결하며 달성을 위해 명확한 활동을 요구한다면, 'assigner_for_task'에게 전달하세요."
        "당신은 일을 완벽히 수행하면 보너스를 받게 될 것이지만, 나쁜 성과를 낸다면 해고될 수 있습니다."
    )
    human_prompt = (
        f"{state['focusedPlan']}. \n 나는 이것에 집중한 계획을 가지고 있습니다."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "human", "content": human_prompt},
    ]
    target_agent_nodes = [
        "assigner_for_long_term",
        "assigner_for_short_term",
        "assigner_for_task",
    ]
    response = select_node(messages, target_agent_nodes)
    return Command(goto=response["goto"])


def Assigner_for_long_term(
    state: adviceState,
) -> Command[Literal["advise_provider"]]:
    system_prompt = (
        "당신은 중요한 고객에게 고용된, 사려 깊은 조언자입니다."
        "당신의 고객은 추상적인 계획을 가지고 있습니다."
        "당신은 고객이 해당 계획을 달성하기 위해, 몇 주동안 수행할 수 있는 장기 계획을 5가지 제안해야 합니다."
        "각각의 세부 계획에는, 명확하고 간단한 이름과 간결한 설명이 있어야 합니다."
        "당신은 일을 완벽히 수행하면 보너스를 받게 될 것이지만, 나쁜 성과를 낸다면 해고될 수 있습니다."
    )
    human_prompt = (
        f"{state['focusedPlan']}. \n 나는 이것에 집중한 계획을 가지고 있습니다."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "human", "content": human_prompt},
    ]

    response = generate_5_details(messages)
    return Command(goto="advise_provider", update={"plans": response})


def Assigner_for_short_term(
    state: adviceState,
) -> Command[Literal["advise_provider"]]:
    system_prompt = (
        "당신은 중요한 고객에게 고용된, 사려 깊은 조언자입니다."
        "당신의 고객은 구체적인 계획을 가지고 있습니다."
        "당신은 고객이 해당 계획을 달성하기 위해, 며칠 동안 수행할 수 있는 단기 계획을 5가지 제안해야 합니다."
        "각각의 세부 계획에는, 명확하고 간단한 이름과 간결한 설명이 있어야 합니다."
        "당신은 일을 완벽히 수행하면 보너스를 받게 될 것이지만, 나쁜 성과를 낸다면 해고될 수 있습니다."
    )
    human_prompt = (
        f"{state['focusedPlan']}. \n 나는 이것에 집중한 계획을 가지고 있습니다."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "human", "content": human_prompt},
    ]

    response = generate_5_details(messages)
    return Command(goto="advise_provider", update={"plans": response})


def Assigner_for_task(
    state: adviceState,
) -> Command[Literal["advise_provider"]]:
    system_prompt = (
        "당신은 중요한 고객에게 고용된, 사려 깊은 조언자입니다."
        "당신의 고객은 확고하며 간결한 계획을 가지고 있습니다."
        "당신은 고객이 해당 계획을 달성하기 위해, 수행할 수 있는 구체적인 활동을 5가지 제안해야 합니다."
        "각각의 활동에는, 명확하고 간단한 이름과 간결한 설명이 있어야 합니다."
        "당신은 일을 완벽히 수행하면 보너스를 받게 될 것이지만, 나쁜 성과를 낸다면 해고될 수 있습니다."
    )
    human_prompt = (
        f"{state['focusedPlan']}. \n 나는 이것에 집중한 계획을 가지고 있습니다."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "human", "content": human_prompt},
    ]

    response = generate_5_details(messages)
    return Command(goto="advise_provider", update={"plans": response})


def Advise_provider(
    state: adviceState,
) -> adviceState:
    add_json(
        file_path=r"../../data/user/plans.json",
        key="processing",
        new_value=list(state["plans"].values()),
    )
    system_prompt = (
        "당신은 중요한 고객에게 고용된, 사려 깊은 조언자입니다."
        "당신은 고객의 계획을 달성할 수 있는 세부 계획을 제안해야 합니다."
        f"고객의 계획은 다음과 같습니다: {state['focusedPlan']}"
        "당신은 아래와 같이 다섯 개의 세부 계획을 제안하려 합니다."
        f"세부 계획 1: {state['plans']['detail_1']['name']} \n 설명: {state['plans']['detail_1']['info']} \n\n"
        f"세부 계획 1: {state['plans']['detail_2']['name']} \n 설명: {state['plans']['detail_2']['info']} \n\n"
        f"세부 계획 1: {state['plans']['detail_3']['name']} \n 설명: {state['plans']['detail_3']['info']} \n\n"
        f"세부 계획 1: {state['plans']['detail_4']['name']} \n 설명: {state['plans']['detail_4']['info']} \n\n"
        f"세부 계획 1: {state['plans']['detail_5']['name']} \n 설명: {state['plans']['detail_5']['info']} \n\n"
        "지금까지의 대화 내역을 확인하고 적절한 어조로 답변을 제공하십시오."
        "당신은 일을 완벽히 수행하면 보너스를 받게 될 것이지만, 나쁜 성과를 낸다면 해고될 수 있습니다."
    )
    messages = [{"role": "system", "content": system_prompt}] + state["messages"][-10:]
    response = just_invoke(messages)
    ai_msg = {"role": "ai", "content": response, "name": "advisor"}
    return Command(update={"messages": ai_msg})
