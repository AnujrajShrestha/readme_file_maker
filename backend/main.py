from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,HttpUrl
from dotenv import load_dotenv

from RAG.rag_engine import run_pipeline

load_dotenv()

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class userInput(BaseModel):
    url: HttpUrl
    project_name: str
    author_name: str
    github_id_url: HttpUrl

class modelResponse(BaseModel):
    message: str 
    project_name: str 
    repository_url: str 
    result: dict

@app.get('/')
def home():
    return {'message': 'Readme file maker API'}

@app.post('/maker',response_model= modelResponse)
def maker(features: userInput):
    try:
        user_input = { "url": str(features.url),
                      "project_name": features.project_name,
                      "author_name": features.author_name,
                      "github_id_url": str(features.github_id_url)
                      }
        result= run_pipeline(user_input)
        
        return { "message": "README generated successfully",
                "project_name": features.project_name,
                "repository_url": str(features.url),
                "result": result }
    except Exception as e:
        raise HTTPException(
            status_code= 500,
            detail=f'Something went wrong form our site {str(e)}'
        )