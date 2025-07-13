## Handwritten Digit Classifier with FastAPI


A web application for handwritten digit recognition (0-9). Users draw digits on a UI canvas, and a machine learning model predicts the digit via a REST API. The architecture decouples the UI and model for modularity, using a FastAPI backend and a Python-based frontend.

Backend: FastAPI serving an MLP model trained on MNIST (~90% test accuracy, ~60% on user drawings).
Frontend: Python UI (e.g., Tkinter) for drawing and displaying predictions.
API: Accepts 28x28 grayscale images or flattened 784-element normalized vectors, returns predicted digit.

Prerequisites

Python 3.8+
Docker
Git

Setup

###### git clone https://github.com/<your-username>/HandwrittenDigitClassifier.git
###### cd HandwrittenDigitClassifier
###### pip install -r requirements.txt
###### docker run -p 8000:8000 fastapi_backend
###### python app.py



Usage

Draw a Digit: Use the mouse to draw a digit (0-9) on the UI canvas.
Predict: Click "Predict" to send the image to the /predict API endpoint. The predicted digit is displayed.
Clear Canvas: Click "Clear" to reset and draw again.

API Endpoint

POST /predict
Input: 28x28 grayscale image or 784-element normalized vector (0.0-1.0) as binary data.
Output: JSON, e.g., {"prediction": 7}.
Processing: Images are flattened and normalized before model inference.



Notes

Model performance varies due to drawing style differences. Consider upgrading to a CNN for better accuracy.
Ensure the Docker container is running before starting the UI.
The fastapi_backend Docker image includes the model and dependencies.

Troubleshooting

Docker Issues: Verify Docker is running and the fastapi_backend image exists (docker images).
API Connection Failure: Ensure the backend is active on http://localhost:8000.
Dependencies: Confirm all frontend packages are installed.

Acknowledgments
Based on sudarsun/HandwrittenDigitClassifier, restructured for loose coupling with a REST API.
