from dotenv import load_dotenv
load_dotenv()
from crewai import Task, Crew
from agents.research_agent import create_research_agent
from agents.analysis_agent import create_analysis_agent
from agents.doc_agent import create_doc_agent


# 1️⃣ Get user query
query = input("Enter logistics research query: ")

# 2️⃣ Create agents
research_agent = create_research_agent()
analysis_agent = create_analysis_agent()
doc_agent = create_doc_agent()

# 3️⃣ Create tasks

research_task = Task(
    description=f"Research the following topic in detail: {query}",
    agent=research_agent,
    expected_output="Detailed research findings including relevant sources and insights."
)

analysis_task = Task(
    description="""
    Analyze the research findings and extract:
    - Key trends
    - Technologies
    - Challenges
    - Opportunities
    """,
    agent=analysis_agent,
    expected_output="Structured analysis including trends, technologies, challenges, and opportunities.",
    context=[research_task]
)

doc_task = Task(
    description=f"""
    Format the analysis into this structure:

    Title:
    Date:
    Query: {query}
    Key Trends:
    Technologies:
    Challenges:
    Opportunities:
    Sources:
    Summary:
    """,
    agent=doc_agent,
    expected_output="Well-formatted structured research report.",
    context=[analysis_task]
)

# 4️⃣ Create Crew (IMPORTANT: include all agents & tasks)

crew = Crew(
    agents=[research_agent, analysis_agent, doc_agent],
    tasks=[research_task, analysis_task, doc_task],
    verbose=True
)

# 5️⃣ Run crew
result = crew.kickoff()

# 6️⃣ LAST STEP — Save to knowledge repository
with open("knowledge_repository.txt", "a", encoding="utf-8") as f:
    f.write(f"{result}\n\n---\n\n")

print("\n✅ Research saved successfully.")

