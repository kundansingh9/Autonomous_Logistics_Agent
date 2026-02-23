from crewai import Agent
from langchain_ollama import ChatOllama
from tools.search_tool import get_search_tool


def create_research_agent():
    llm = ChatOllama(
        model="ollama/phi3",
        base_url="http://localhost:11434"
    )

    return Agent(
    role="Logistics Research Specialist",
    goal="Research latest logistics and warehousing innovations",
    backstory="Expert in AI, supply chain, and automation research.",
    tools=[get_search_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=3
)