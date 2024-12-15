from typing_extensions import Literal
from langgraph.types import Command
from agents.organizer.state import orgState
from agents.organizer.utils import just_invoke
from agents.utils import add_json


def Task_selector(state: orgState):
    system_prompt = ""
    messages = [{"system": system_prompt}] + state["messages"]
    response = just_invoke(messages)
    return {"subject": response["subject"]}


def Task_integrator(state: orgState) -> Command[Literal["time_limit_checker"]]:
    system_prompt = ""
    messages = [{"system": system_prompt}] + state["messages"]
    response = just_invoke(messages)
    return Command(goto="time_limit_checker", update={"integrated_task": response})


def Time_limit_checker(
    state: orgState,
) -> Command[Literal["timetable_generator", "__end__"]]:
    system_prompt = ""
    messages = [{"system": system_prompt}] + state["messages"]
    response = just_invoke(messages)
    if not response["time_limit"]:
        ai_msg = {
            "role": "ai",
            "content": "끝마쳐야할 시간 기한을 정확히 알려주세요. 답해주시면 바로 시간 계획을 진행하겠습니다.",
            "name": "organizor",
        }
        return Command(goto="__end__", update={"messages": ai_msg})
    return Command(goto="timetable_generator")


def Timetable_generator(state: orgState) -> Command[Literal["thinker"]]:
    system_prompt = ""
    messages = [{"system": system_prompt}] + state["messages"]
    response = just_invoke(messages)
    return Command(goto="thinker", update={"time_table": response})


def Thinker(state: orgState):
    system_prompt = ""
    messages = [{"system": system_prompt}] + state["messages"]
    response = just_invoke(messages)
    add_json(
        file_path=r"../../data/user/plans.json",
        key="processing",
        new_value=[response["recommend"]],
    )
    ai_msg = {"role": "ai", "content": response, "name": "organizor"}
    return state["messages"].append(ai_msg)
