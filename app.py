from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

app = FastAPI()

origins = os.getenv("FRONTEND_URL", "http://localhost:5173")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UrlRequest(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/summary")
async def summarize(data:UrlRequest):
    try:
        if not data.url or not data:
            return {"error": "URL is required"}
        
        from chain import summarize as chain_summarize
        summary = chain_summarize(data.url)
        return {"summary": summary}
    
    except Exception as e:
        return {"error": str(e)}