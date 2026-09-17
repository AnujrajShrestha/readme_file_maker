from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import pandas as pd

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
    repo_url: str
    project_name: str
    author_name: str
    author_repo_url: str

class modelResponse(BaseModel):
    response: dict

@app.get('/')
def home():
    return {'message': 'Readme file maker API'}

@app.post('/maker',response_model= modelResponse)
def maker(freatures: userInput):
    try:
        