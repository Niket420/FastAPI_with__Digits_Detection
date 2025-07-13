from fastapi import FastAPI,Path
from pydantic import BaseModel
app = FastAPI()

class Input(BaseModel):
    query:str
    author:str


books = [
    {"title": "Harry Potter", "author": "J.K. Rowling"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"title": "Atomic Habits", "author": "James Clear"}
]

def search_books(query="", author=""):
    result = []
    for book in books:
        if query.lower() in book["title"].lower() and author.lower() in book["author"].lower():
            result.append(book)
    return result


@app.post("/")
def get_answer(item : Input):
    result = search_books(item.query,item.author)
    return {"result":result}
