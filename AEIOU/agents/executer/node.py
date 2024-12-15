from langgraph.prebuilt import ToolNode
from langgraph.graph import END
from agents.executer.state import execState
from agents.executer.utils import tool_invoke
from agents.executer.tool import tools

tool_node = ToolNode(tools)


def Tool_caller(state: execState) -> execState:
    system_prompt = ""
    messages = [{"system": system_prompt}] + state["messages"]
    response = tool_invoke(messages)
    ai_msg = {"role": "ai", "content": response, "name": "executor"}
    return state["messages"].append(ai_msg)


def should_continue(state: execState):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END
