from .git_clone import clone_repo
from .db import run_db,load_context
from .agents import agent_groq_20b,agent_groq_120b,mistral_prompt,groq_prompt
from .config import ProjectInput
from .readme_maker import create_readme,_extract_content

def run_pipeline(user_input: str):
    url=user_input['url']
    state = {}

    clone_repo(url)
    run_db(url)

    context = load_context("Create a README file for this repository")
    
    print("\n"+" -"*50)
    print("Step 1 - groq agent-20b is working ...")
    print("\n"+" -"*50)
    
    agent1 = agent_groq_20b()
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
    groq_content= _extract_content(response_groq)
    print(groq_content)
    
    print("\n"+" -"*50)
    print("Step 2 - groq agent-120b is working ...")
    print("\n"+" -"*50)
    
    agent2 = agent_groq_120b()
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
    state["mistral_result"] = response_mistral 
    mistral_content = _extract_content(response_mistral) 
    print(mistral_content)
    
    state['author_result']={
        'author': user_input['author_name'],
        'github_id_url': user_input['github_id_url'],
        'decs': "⭐ If you found this project useful, consider giving it a star on GitHub!"
    }
        
    readme= create_readme(state,url)

    return {
        "readme": readme,
        "project_name": user_input["project_name"],
        "repository_url": url,
        "author_name": user_input["author_name"],
        "github_id_url": user_input["github_id_url"]
    }


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