from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_pipeline import get_response

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post("/chat")
def chat(query: Query):
    response = get_response(query.question)
    return {"response": response}