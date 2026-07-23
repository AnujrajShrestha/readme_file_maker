from git_clone import clone_repo
from db import run_db,load_context
from agents import analyzer_agent,agent_extract_features,agent_architecture_maker,agent_extract_structure,agent_techStack,agent_installation,agent_env,agent_usage,agent_impovements,agent_author_info
from readme_maker import create_readme
from config import ProjectInput

def run_agent(agent_factory, prompt, state_key, context, state):
    print("\n" + "-" * 60)
    print(f"{state_key} agent is working...")
    print("-" * 60)

    agent = agent_factory()

    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": prompt.format(context=context)
        }]
    })

    state[state_key+"_result"] = result["structured_response"]

    print(f"\n{state_key}:\n")
    for name, value in state[state_key+"_result"].model_dump().items():
        print(f"{name}: {value}\n")


def run_pipeline(url: str):
    state = {}

    clone_repo(url)
    run_db(url)

    context = load_context("Create a README file for this repository")

    # List of all agents
    agent_steps = [
        (
            analyzer_agent,
            "Analyse the following repository:\n\n{context}",
            "analysis",
        ),
        (
            agent_extract_features,
            "Extract the key features from:\n\n{context}",
            "features",
        ),
        (
            agent_architecture_maker,
            "Generate the project architecture from:\n\n{context}",
            "architecture",
        ),
        (
            agent_extract_structure,
            "Describe the folder and file structure from:\n\n{context}",
            "structure",
        ),
        (
            agent_techStack,
            "Identify the technologies used in:\n\n{context}",
            "techstack",
        ),
        (
            agent_installation,
            "Generate installation instructions for:\n\n{context}",
            "installation",
        ),
        (
            agent_env,
            "Extract all required environment variables from:\n\n{context}",
            "env",
        ),
        (
            agent_usage,
            "Generate usage instructions for:\n\n{context}",
            "usage",
        ),
        (
            agent_impovements,
            "Suggest possible improvements for:\n\n{context}",
            "improvements",
        ),
        (
            agent_author_info,
            "Generate author information for:\n\n{context}",
            "author",
        ),
    ]

    for agent_factory, prompt, state_key in agent_steps:
        run_agent(agent_factory, prompt, state_key, context, state)
        
    create_readme(state,url)

    return state


if __name__ == "__main__":    
    url= input("Enter repository url: ")
    project_name= input("Enter project name: ")
    author_name= input("Enter author name: ")
    github_id_url= input("Enter github ID url: ")
    
    ProjectInput.append({
        'url': url,
        'author_name': author_name,
        'project_name': project_name,
        'github_id_url': github_id_url
    })
    
    run_pipeline(ProjectInput[0]['url'])