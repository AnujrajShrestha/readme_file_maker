from langchain_mistralai import ChatMistralAI
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv

from tools import analyze_project,extract_tech_stack,extract_features,extract_structure,installation_tool,future_tool,architecture_maker,env_tool,usage_tool,author_information
from tools import ProjectAnalysis,TechStack,Features,FolderStructure,Installation,FutureIdeas,ArchitectureDiagram,EnvironmentVariables,Usage,author_info
load_dotenv()

llm_mistral= ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.6
)

llm_groq= ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.6,
)

def analyzer_agent():
    return create_agent(
        tools= [analyze_project],
        model= llm_groq,
        response_format=ProjectAnalysis
    )

def agent_extract_features():
    return create_agent(
        tools= [extract_features],
        model= llm_groq,
        response_format= Features
    )

def agent_architecture_maker():
    return create_agent(
        tools= [architecture_maker],
        model= llm_mistral,
        response_format= ArchitectureDiagram
    )

def agent_extract_structure():
    return create_agent(
        tools= [extract_structure],
        model= llm_mistral,
        response_format= FolderStructure
    )
    
def agent_techStack():
    return create_agent(
        tools= [extract_tech_stack],
        model= llm_groq,
        response_format= TechStack
    )
    
def agent_installation():
    return create_agent(
        tools= [installation_tool],
        model= llm_mistral,
        response_format= Installation
    )
    
def agent_env():
    return create_agent(
        tools= [env_tool],
        model= llm_groq,
        response_format= EnvironmentVariables
    )
    
def agent_usage():
    return create_agent(
        tools= [usage_tool],
        model= llm_mistral,
        response_format= Usage
    )
    
def agent_impovements():
    return create_agent(
        tools= [future_tool],
        model= llm_mistral,
        response_format= FutureIdeas
    )
    
def agent_author_info():
    return create_agent(
        tools= [author_information],
        model= llm_groq,
        response_format= author_info
    )