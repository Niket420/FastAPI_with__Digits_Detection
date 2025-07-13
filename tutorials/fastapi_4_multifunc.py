from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Input(BaseModel):
    name : str
    marks : List[int]




def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"

def generate_report(name, marks):
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    return name,avg,grade


@app.post("/report")
def get_student_report(inputs:Input):
    name,avg,grade = generate_report(inputs.name,inputs.marks)
    return {"name":name ,"avg":avg,"grade":grade}

