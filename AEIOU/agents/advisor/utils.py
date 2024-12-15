from agents.llm import model
from langchain_core.messages import AnyMessage


def just_invoke(messages: list[AnyMessage]):
    response = model.invoke(messages)
    return response.content


def focused_plan(messages: list[AnyMessage], target_plans: list[str]):
    json_schema = {
        "name": "Plan",
        "parameters": {
            "type": "object",
            "properties": {
                "focusedOn": {
                    "enum": [*target_plans, "new_plan"],
                    "type": "string",
                    "description": "The plan to be focused now on by the user, or 'new_plan' if the user wanted to make a new plan. Must be one of the specified values.",
                },
            },
            "required": ["focusedOn"],
        },
    }
    response = model.with_structured_output(json_schema).invoke(messages)
    return response


def generate_5_details(messages: list[AnyMessage]):
    json_schema = {
        "name": "Details",
        "parameters": {
            "type": "object",
            "properties": {
                "detail_1": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of plan or task for achieving the user's plan",
                        },
                        "info": {
                            "type": "string",
                            "description": "The breif infomation about plan or task for achieving the user's plan",
                        },
                    },
                    "required": ["name", "info"],
                    "description": "The first detailed plan or task proposed to achieve the user's plan.",
                },
                "detail_2": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of plan or task for achieving the user's plan",
                        },
                        "info": {
                            "type": "string",
                            "description": "The breif infomation about plan or task for achieving the user's plan",
                        },
                    },
                    "required": ["name", "info"],
                    "description": "The second detailed plan or task proposed to achieve the user's plan.",
                },
                "detail_3": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of plan or task for achieving the user's plan",
                        },
                        "info": {
                            "type": "string",
                            "description": "The breif infomation about plan or task for achieving the user's plan",
                        },
                    },
                    "required": ["name", "info"],
                    "description": "The third detailed plan or task proposed to achieve the user's plan.",
                },
                "detail_4": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of plan or task for achieving the user's plan",
                        },
                        "info": {
                            "type": "string",
                            "description": "The breif infomation about plan or task for achieving the user's plan",
                        },
                    },
                    "required": ["name", "info"],
                    "description": "The fourth detailed plan or task proposed to achieve the user's plan.",
                },
                "detail_5": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of plan or task for achieving the user's plan",
                        },
                        "info": {
                            "type": "string",
                            "description": "The breif infomation about plan or task for achieving the user's plan",
                        },
                    },
                    "required": ["name", "info"],
                    "description": "The fifth detailed plan or task proposed to achieve the user's plan.",
                },
            },
            "required": ["detail_1", "detail_2", "detail_3", "detail_4", "detail_5"],
        },
    }
    response = model.with_structured_output(json_schema).invoke(messages)
    return response