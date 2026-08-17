from typing import Union
from fastapi import FastAPI
from chat import get_response
from pydantic import BaseModel

app = FastAPI()


class Chat(BaseModel):
    msg: str

@app.get("/")
def read_root(chat: Chat):
    return {"reply": get_response(str(chat))}