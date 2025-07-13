from typing import Annotated
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
app = FastAPI()


class Item(BaseModel):
    name: int
    email: str 
    


@app.post('/')
def register_user(item:Item):
    if "@" not in item.email:
        return "Invalid email"
    return f"User {item.name} registered with {item.email}"

