from git_clone import clone_repo
from db import run_db,load_context
from agents import agent_groq,agent_mistral,mistral_prompt,groq_prompt
from config import ProjectInput
from readme_maker import create_readme

def run_pipeline(user_input: str):
    url=user_input['url']
    state = {}

    clone_repo(url)
    run_db(url)

    context = load_context("Create a README file for this repository")
    
    print("\n"+" -"*50)
    print("Step 1 - groq agent is working ...")
    print("\n"+" -"*50)
    
    agent1 = agent_groq()
    response_groq = agent1.invoke(
    {
        "messages": groq_prompt.invoke(
            {
                "context": context,
                "input": "Generate installation instructions."
            }
        ).messages
    }
)
    state['groq_result']= response_groq
    print(response_groq)
    
    print("\n"+" -"*50)
    print("Step 2 - mistral agent is working ...")
    print("\n"+" -"*50)
    
    agent2 = agent_mistral()
    response_mistral = agent2.invoke(
    {
        "messages": mistral_prompt.invoke(
            {
                "context": context,
                "input": "Explain the project architecture."
            }
        ).messages
    }
)
    state['mistral_result']= response_mistral
    print(response_mistral)


    state['author_result']={
        'author': user_input['author_name'],
        'github_id_url': user_input['github_id_url'],
        'decs': "⭐ If you found this project useful, consider giving it a star on GitHub!"
    }
        
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
    
    run_pipeline(ProjectInput[0])