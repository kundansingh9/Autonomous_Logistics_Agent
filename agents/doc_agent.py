from crewai import Agent
from langchain_ollama import ChatOllama


def create_doc_agent():
    llm = ChatOllama(
        model="ollama/phi3",
        base_url="http://localhost:11434"
    )

    return Agent(
        role="Logistics Documentation Specialist",
        goal="Generate structured logistics reports and documentation",
        backstory="Expert in converting research and analysis into structured business reports.",
        llm=llm,
        verbose=True
    )