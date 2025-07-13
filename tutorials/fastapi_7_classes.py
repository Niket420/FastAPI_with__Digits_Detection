from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

class Input(BaseModel):
    a:float
    b:float




@app.post('/')
def get_muliplication(item:Input):
    ans = Calculator(item.a,item.b)
    result = ans.multiply()
    return {"result":result} 



@app.post('/')
def get_sum(item:Input):
    ans = Calculator(item.a,item.b)
    result = ans.add()
    return {"result":result}


