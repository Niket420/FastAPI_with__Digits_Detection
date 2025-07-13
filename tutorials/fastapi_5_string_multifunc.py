from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Text(BaseModel):
    user:str
    feedback:str


def save_feedback(feedback):
    with open("feedback.txt", "a") as f:
        f.write(feedback + "\n")

def analyze_sentiment(feedback):
    return "positive" if "good" in feedback.lower() else "negative"

def handle_feedback(user, feedback):
    sentiment = analyze_sentiment(feedback)
    save_feedback(f"{user}: {feedback} [{sentiment}]")
    return {"user": user, "sentiment": sentiment}



@app.post("/get_analyze")
def get_analyze(text:Text):
    return handle_feedback(text.user,text.feedback)
