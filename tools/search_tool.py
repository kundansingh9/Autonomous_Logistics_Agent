from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool

search = DuckDuckGoSearchRun()

@tool("get_search_tool")
def get_search_tool(query: str) -> str:
    """
    Search the web for logistics-related information based on the user query.
    Returns summarized search results.
    """
    return search.run(query)