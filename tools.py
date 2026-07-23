from langchain.tools import tool
from pydantic import BaseModel,Field
from typing import List,Optional
from config import ProjectInput

class ProjectAnalysis(BaseModel):
    project_name: str
    description: str
    category: str
    purpose: str
    
@tool
def analyze_project(question: str)-> ProjectAnalysis:
    """Analyzes the repository and extracts project overview."""
    
class TechStack(BaseModel):
    languages: list[str]
    frameworks: list[str]
    databases: list[str]
    vector_databases: list[str]
    llms: list[str]
    libraries: list[str]
    
@tool
def extract_tech_stack(question: str)-> TechStack:
    """Extract all technologies used in the project."""
    
class Features(BaseModel):
    features: list[str]
    
@tool
def extract_features(question: str) -> Features:
    """Extract project features."""
    
class FolderStructure(BaseModel):
    folders: list[str]
    important_files: list[str]
    
@tool
def extract_structure(question: str) -> FolderStructure:
    """Extract repository folder structure."""
    
class Installation(BaseModel):
    install_steps: list[str]
    requirements: list[str]
    
@tool
def installation_tool(question: str) -> Installation:
    """Generate installation instructions."""
    
class FutureIdeas(BaseModel):
    improvements: list[str]
    
@tool
def future_tool(question: str) -> FutureIdeas:
    """Suggest future improvements based on repository."""
    
class ArchitectureStep(BaseModel):
    step: int = Field(..., description="Execution order")
    component: str = Field(..., description="Component or module name")
    description: str = Field(..., description="What this component does")


class ArchitectureDiagram(BaseModel):
    title: str = Field(..., description="Architecture title")

    entry_point: str = Field(
        ...,
        description="Main starting point of the application"
    )

    architecture_type: str = Field(
        ...,
        description="Examples: RAG, Agentic AI, REST API, ML Pipeline, Streamlit App"
    )

    workflow: List[ArchitectureStep] = Field(
        ...,
        description="Ordered execution flow"
    )

    external_services: List[str] = Field(
        default_factory=list,
        description="External APIs, LLMs, Vector Databases, Cloud services"
    )

    inputs: List[str] = Field(
        default_factory=list,
        description="Application inputs"
    )

    outputs: List[str] = Field(
        default_factory=list,
        description="Application outputs"
    )
    
class ArchitectureInput(BaseModel):
    question: str = Field(
        ...,
        description="Ask the AI to analyze the repository architecture."
    )
    
@tool
def architecture_maker(question: str) -> ArchitectureDiagram:
    """
    Analyze the repository and generate the complete software architecture,
    execution workflow, major components, external services, inputs, and outputs.
    """

class EnvironmentVariables(BaseModel):
    variables: list[str]
    
@tool
def env_tool(question: str):
    """Find required environment variables."""
    
class Usage(BaseModel):
    commands: list[str]
    workflow: list[str]
    
@tool
def usage_tool(question: str):
    """Generate usage instructions."""
    
class author_info(BaseModel):
    author: Optional[str]= Field(description="Author name")
    github_id_url: Optional[str]= Field(description="github ID url")
    decs: str
    
@tool
def author_information(question: str) -> author_info:
    "Fill author infotmation"
    
    return author_info(
        author=ProjectInput[0]['author_name'],
        github_id_url=ProjectInput[0]['github_id_url'],
        decs="⭐ If you found this project useful, consider giving it a star on GitHub!"
    )