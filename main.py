from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crewai import Crew

from agents.research_agent import create_research_agent
from tasks.research_task import create_research_task
from vector_store.vector_store import save_to_vector_store

app = FastAPI(
    title="Autonomous Logistics Researcher Agent",
    description="LLM-powered autonomous logistics research system using CrewAI and LangChain",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For development (allow all)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Request Schema
# ----------------------------
class ResearchRequest(BaseModel):
    query: str


# ----------------------------
# Research Endpoint
# ----------------------------
@app.post("/research")
def research_topic(request: ResearchRequest):

    try:
        query = request.query

        # ✅ Create Agent Object
        research_agent = create_research_agent()

        # ✅ Create Task
        research_task = create_research_task(research_agent, query)

        # ✅ Create Crew
        crew = Crew(
            agents=[research_agent],
            tasks=[research_task],
            verbose=True
        )

        # ✅ Execute Workflow

        result = crew.kickoff()

        final_result = result.raw   # ✅ extract only text



        # ✅ Save to Vector Store
        save_to_vector_store(str(final_result))
        with open("knowledge_repository.txt", "a", encoding="utf-8") as file:
            file.write("\n" + "="*80 + "\n")
            file.write(f"QUERY: {query}\n\n")
            file.write(str(final_result))
            file.write("\n" + "="*80 + "\n")

        return {
            "status": "success",
            "query": query,
            "result": final_result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ----------------------------
# Health Check Endpoint
# ----------------------------
@app.get("/")
def root():
    return {
        "message": "Autonomous Logistics Research Agent is running successfully 🚀"
    }

# @app.post("/research")
# async def research(request: ResearchRequest):
#     try:
#         agent = create_research_agent()
#         task = create_research_task(agent, request.query)

#         crew = Crew(
#             agents=[agent],
#             tasks=[task]
#         )

#         result = crew.kickoff()   # ✅ Correct way

#         return {
#             "status": "success",
#             "result": str(result)
#         }

#     except Exception as e:
#         return {
#             "status": "error",
#             "message": str(e)
#         }



# from dotenv import load_dotenv
# load_dotenv()
# from crewai import Task, Crew
# from agents.research_agent import create_research_agent
# from agents.analysis_agent import create_analysis_agent
# from agents.doc_agent import create_doc_agent
# from fastapi.middleware.cors import CORSMiddleware

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# # 1️⃣ Get user query
# query = input("Enter logistics research query: ")

# # 2️⃣ Create agents
# research_agent = create_research_agent()
# analysis_agent = create_analysis_agent()
# doc_agent = create_doc_agent()

# # 3️⃣ Create tasks

# research_task = Task(
#     description=f"Research the following topic in detail: {query}",
#     agent=research_agent,
#     expected_output="Detailed research findings including relevant sources and insights."
# )

# analysis_task = Task(
#     description="""
#     Analyze the research findings and extract:
#     - Key trends
#     - Technologies
#     - Challenges
#     - Opportunities
#     """,
#     agent=analysis_agent,
#     expected_output="Structured analysis including trends, technologies, challenges, and opportunities.",
#     context=[research_task]
# )

# doc_task = Task(
#     description=f"""
#     Format the analysis into this structure:

#     Title:
#     Date:
#     Query: {query}
#     Key Trends:
#     Technologies:
#     Challenges:
#     Opportunities:
#     Sources:
#     Summary:
#     """,
#     agent=doc_agent,
#     expected_output="Well-formatted structured research report.",
#     context=[analysis_task]
# )

# # 4️⃣ Create Crew (IMPORTANT: include all agents & tasks)

# crew = Crew(
#     agents=[research_agent, analysis_agent, doc_agent],
#     tasks=[research_task, analysis_task, doc_task],
#     verbose=True
# )

# # 5️⃣ Run crew
# result = crew.kickoff()

# # 6️⃣ LAST STEP — Save to knowledge repository
# with open("knowledge_repository.txt", "a", encoding="utf-8") as f:
#     f.write(f"{result}\n\n---\n\n")

# print("\n✅ Research saved successfully.")

