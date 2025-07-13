from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os
import sys
import pickle
from dense_neural_class import Dense_Neural_Diy  # Needed for unpickling
from utils import *  # If model uses anything from utils during inference

app = FastAPI()

# Define input schema
class ImageInput(BaseModel):
    image: List[float]
sys.modules['__main__'].Dense_Neural_Diy = Dense_Neural_Diy
# Load the model from disk
def load_model(filename: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, filename + '.pkl')
    with open(filepath, 'rb') as file:
        model_loaded = pickle.load(file)
    return model_loaded

# Load model at startup
model = load_model('model')

# Prediction endpoint
@app.post("/predict")
def predict(image_vector: ImageInput):
    result = model.predict([image_vector.image])[0]  # Wrap input in list if model expects batch
    return {"prediction": int(result)}