from typing_extensions import Literal
from langgraph.types import Command
from agents.interpretor.state import itpState
from agents.interpretor.utils import just_invoke
from agents.utils import add_json


def Subject_selector(state: itpState):
    system_prompt = ""
    messages = [{"system": system_prompt}] + state["messages"]
    response = just_invoke(messages)
    subject = response["subject"]
    private = response["private"]
    return {"subject": subject, "private": private}


def Sentiment_interpretor(
    state: itpState,
) -> Command[Literal["secret_keeper", "sentimental_counselor"]]:
    system_prompt = ""
    messages = [{"system": system_prompt}] + state["messages"]
    response = just_invoke(messages)
    user_response = {
        "polarity": response["1_llm"],
        "emotion": response["2_llm"],
        "preference": response["3_llm"],
    }
    if state["private"]:
        return Command(goto="sentimental_counselor", update={"response": user_response})
    return Command(goto="secret_keeper", update={"response": user_response})


def Secret_keeper(state: itpState):
    add_json(
        file_path=r"../../data/user/preferences.json",
        key="preference",
        new_value=[{"subject": state["subject"], "response": state["response"]}],
    )
    return Command(goto="sentimental_counselor")


def Sentimental_counselor(state: itpState):
    system_prompt = ""
    messages = [{"system": system_prompt}] + state["messages"]
    response = just_invoke(messages)
    ai_msg = {"role": "ai", "content": response, "name": "executor"}
    return state["messages"].append(ai_msg)
