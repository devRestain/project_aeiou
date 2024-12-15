from langchain_core.tools import tool


@tool
def Tool_for_internet_search(keyword: str):
    """
    인터넷에서 특정 검색어를 검색할 수 있음.
    """
    return f"The result of searching {keyword} is none."


@tool
def Tool_for_rag():
    """
    설명
    """
    pass


@tool
def Tool_for_calculation():
    """
    설명
    """
    pass


tools = [Tool_for_internet_search, Tool_for_rag, Tool_for_calculation]
