🎯 Handwritten Digit Classifier (FastAPI + UI)

A modular web application for recognizing handwritten digits (0–9).
Users draw digits on a canvas, and a machine learning model predicts the digit via a REST API.

⸻

🚀 Overview

This project demonstrates a decoupled architecture where:
	•	🧠 Backend handles model inference using FastAPI
	•	🎨 Frontend provides a drawing interface using Python UI
	•	🔗 API connects both components seamlessly

⸻

🏗️ Architecture

[ User Drawing (UI) ] → [ FastAPI Backend ] → [ ML Model (MLP) ] → [ Prediction ]

🔧 Components
	•	Backend
	•	FastAPI server
	•	MLP model trained on MNIST
	•	~90% test accuracy (MNIST)
	•	~60% accuracy on real user drawings
	•	Frontend
	•	Python-based UI (e.g., Tkinter)
	•	Canvas for digit drawing
	•	Displays prediction results
	•	API
	•	Accepts image input
	•	Returns predicted digit in JSON format

⸻

⚙️ Features
	•	✍️ Draw digits directly on canvas
	•	⚡ Real-time prediction via REST API
	•	🔌 Clean separation between UI and backend
	•	🐳 Dockerized backend for easy deployment

⸻

📦 Prerequisites

Make sure you have:
	•	Python 3.8+
	•	Docker
	•	Git

⸻

🛠️ Setup & Installation

# Clone the repository
git clone https://github.com/<your-username>/HandwrittenDigitClassifier.git

cd HandwrittenDigitClassifier

# Install dependencies
pip install -r requirements.txt


⸻

🐳 Run Backend (Docker)

docker run -p 8000:8000 fastapi_backend

Backend will be available at:
👉 http://localhost:8000

⸻

🖥️ Run Frontend

python app.py


⸻

🎮 Usage
	1.	Draw a Digit
	•	Use your mouse to draw a number (0–9)
	2.	Predict
	•	Click “Predict”
	•	The UI sends data to /predict API
	•	Prediction is displayed
	3.	Clear Canvas
	•	Click “Clear” to reset

⸻

📡 API Documentation

🔹 Endpoint

POST /predict

🔹 Input
	•	28×28 grayscale image
OR
	•	Flattened vector (784 values)
	•	Values normalized between 0.0 – 1.0

🔹 Output

{
  "prediction": 7
}

🔹 Processing Pipeline
	•	Image → Flatten → Normalize → Model Inference → Prediction

⸻

📊 Model Performance

Dataset	Accuracy
MNIST Test Data	~90%
User Drawings	~60%

⚠️ Performance drops on real drawings due to:
	•	style variation
	•	stroke thickness
	•	alignment differences

⸻

🚧 Improvements (Future Work)
	•	🔥 Upgrade to CNN (significant accuracy boost)
	•	🎯 Better preprocessing (centering, smoothing)
	•	🌐 Web-based frontend (React/Canvas)
	•	📱 Mobile-friendly UI
	•	⚡ Model optimization for faster inference

⸻

🧪 Troubleshooting

❗ Docker Issues

docker images

	•	Ensure fastapi_backend image exists
	•	Verify Docker is running

⸻

❗ API Connection Failure
	•	Check backend is live:
👉 http://localhost:8000

⸻

❗ Dependency Errors

pip install -r requirements.txt


⸻

🙌 Acknowledgments
	•	Inspired by: sudarsun/HandwrittenDigitClassifier
	•	Refactored with a modular API-first architecture

⸻

📌 Key Takeaway

This project is not just a digit classifier —
it’s a clean example of how to design ML systems like real products:
	•	decoupled architecture
	•	API-driven design
	•	deployable backend
	•	scalable foundation
