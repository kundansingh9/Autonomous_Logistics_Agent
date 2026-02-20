from crewai.tools import tool

@tool("get_search_tool")
def get_search_tool(query: str) -> str:
    """
    Search the web for logistics-related information.
    """
    # Your search logic here
    return f"Search results for: {query}"