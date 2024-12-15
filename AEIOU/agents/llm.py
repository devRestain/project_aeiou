from langchain_openai import ChatOpenAI
from langchain_core.messages import AnyMessage

model = ChatOpenAI(model="gpt-4o")


def generate_response(messages: list[AnyMessage], target_agent_nodes: list[str]):

    json_schema = {
        "name": "Response",
        "parameters": {
            "type": "object",
            "properties": {
                "response": {
                    "type": "string",
                    "description": "A human readable response to the original question. Does not need to be a final response. Will be streamed back to the user.",
                },
                "goto": {
                    "enum": [*target_agent_nodes],
                    "type": "string",
                    "description": "The next agent to call, or '__end__' if the user's query has been resolved. Must be one of the specified values.",
                },
            },
            "required": ["response", "goto"],
        },
    }
    response = model.with_structured_output(json_schema).invoke(messages)
    return response


def select_node(messages: list[AnyMessage], target_agent_nodes: list[str]):

    json_schema = {
        "name": "Response",
        "parameters": {
            "type": "object",
            "properties": {
                "goto": {
                    "enum": [*target_agent_nodes, "finish"],
                    "type": "string",
                    "description": "The next agent to call. Must be one of the specified values.",
                },
            },
            "required": ["goto"],
        },
    }
    response = model.with_structured_output(json_schema).invoke(messages)
    return response
