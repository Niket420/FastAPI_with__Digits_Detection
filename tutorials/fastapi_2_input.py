from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def lestgo():
    return {"Welcome home daddy shaw"}


@app.post('/n')
def is_prime(n:int):
    if n <= 1:
        return {"isPrime":False}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return {"isPrime":False}
    return {"isPrime":True}

