from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from local_llm_model.model_serving import query


app = FastAPI()

class ChatMessage(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat")
def chat(message: ChatMessage):
    return {"message": query(message.query)}