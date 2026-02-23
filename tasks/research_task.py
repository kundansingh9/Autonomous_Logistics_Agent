from crewai import Task

def create_research_task(agent, query):

    return Task(
        description=f"""
        Research the following logistics topic:

        {query}

        Use the search tool if needed.
        After gathering information, provide a complete final answer.

        Provide:
        - Key insights
        - Emerging trends
        - Real-world applications
        - Future predictions

        Return ONLY the final research summary.
        Do NOT return tool actions.
        """,
        expected_output="A complete detailed research summary in paragraph format.",
        agent=agent
    )