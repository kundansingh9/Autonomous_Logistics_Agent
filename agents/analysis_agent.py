from crewai import Agent
from langchain_ollama import ChatOllama


def create_analysis_agent():
    llm = ChatOllama(
        model="ollama/phi3",
        base_url="http://localhost:11434"
    )

    return Agent(
        role="Logistics Strategy Analyst",
        goal="Analyze research and create actionable logistics insights",
        backstory="Specialist in supply chain optimization and AI deployment.",
        llm=llm,
        verbose=True
    )
