from langchain_mistralai import ChatMistralAI
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

from tools import analyze_project,extract_tech_stack,extract_features,extract_structure,installation_tool,future_tool,architecture_maker,env_tool,usage_tool
load_dotenv()

llm_mistral= ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.3
)

llm_groq= ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
)

groq_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert software engineer.

Use only the provided repository context to answer.
Do not hallucinate.
Return Markdown.
"""
        ),
        (
            "human",
            """
Repository Context:

{context}

Task:
{input}
"""),
        ])

def agent_groq():
    return create_agent(
        model= llm_groq,
        tools= [analyze_project,extract_features,future_tool,installation_tool]
    )


mistral_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Senior Software Architect and Technical Documentation Expert.

Your responsibilities:
- Analyze the provided repository context.
- Extract the technology stack.
- Explain the project architecture.
- Explain the folder and file structure.
- Generate environment variable documentation.
- Generate the project usage section.

Guidelines:
- Use ONLY the provided repository context.
- Never hallucinate or invent information.
- If information is unavailable, explicitly state that.
- Produce clean, professional Markdown.
- Use headings, bullet points, and tables where appropriate.
- Keep explanations concise but informative.
- When generating architecture, explain the workflow between components.
"""
        ),
        (
            "human",
            """
Repository Context:

{context}

Task:
{input}
"""),
])

def agent_mistral():
    return create_agent(
        model= llm_mistral,
        tools= [extract_tech_stack,extract_structure,architecture_maker,env_tool,usage_tool]
    )
    