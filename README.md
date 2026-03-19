# Handwritten Digit Classifier API

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi"/>
  <img src="https://img.shields.io/badge/MLP-MNIST-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge&logo=docker"/>
  <img src="https://img.shields.io/badge/UI-Tkinter-lightgrey?style=for-the-badge"/>
</p>



⸻

🚀 Overview

A production-style machine learning application for handwritten digit recognition (0–9).
	•	🎨 Draw digits on a canvas
	•	⚡ Predict instantly via FastAPI
	•	🔗 Clean UI–backend separation
	•	🧠 ML model trained on MNIST

⸻

🧠 Tech Stack

Layer	Technology
Backend	FastAPI
Model	MLP (MNIST)
Frontend	Tkinter
Deployment	Docker
Language	Python


⸻

🏗️ System Architecture

[ UI Canvas ] → [ FastAPI API ] → [ ML Model ] → [ Prediction ]


⸻

⚙️ Features
	•	✍️ Interactive drawing canvas
	•	⚡ REST API-based prediction
	•	🧩 Modular architecture (decoupled UI + backend)
	•	🐳 Dockerized backend
	•	📦 Lightweight and easy to run

⸻

📊 Model Performance

Dataset	Accuracy
MNIST Test	~90%
User Drawings	~60%

⚠️ Lower accuracy on real drawings due to style variation

⸻

🛠️ Quick Start

1️⃣ Clone Repository

git clone https://github.com/<your-username>/HandwrittenDigitClassifier.git
cd HandwrittenDigitClassifier


⸻

2️⃣ Install Dependencies

pip install -r requirements.txt


⸻

3️⃣ Run Backend (Docker)

docker run -p 8000:8000 fastapi_backend

📍 API running at:
http://localhost:8000

⸻

4️⃣ Run Frontend

python app.py


⸻

🎮 Usage
	•	Draw a digit on canvas
	•	Click Predict
	•	View result instantly
	•	Click Clear to reset

⸻

📡 API Reference

🔹 Endpoint

POST /predict

🔹 Input
	•	28×28 grayscale image
OR
	•	Flattened vector (784 values, normalized)

🔹 Output

{
  "prediction": 7
}


⸻

🔄 Processing Pipeline

Image → Resize → Normalize → Flatten → Model → Prediction


⸻

🚧 Future Improvements
	•	🔥 CNN upgrade (→ 98%+ accuracy)
	•	🌐 Web UI (React + Canvas)
	•	📱 Mobile-friendly interface
	•	⚡ Faster inference optimization
	•	☁️ Cloud deployment (AWS/Azure)

⸻

🧪 Troubleshooting

Docker not working?

docker images

✔ Ensure fastapi_backend exists
✔ Docker is running

⸻

API not connecting?

👉 Check: http://localhost:8000

⸻

Dependency issues?

pip install -r requirements.txt


⸻

🙌 Acknowledgments

Inspired by:
	•	sudarsun/HandwrittenDigitClassifier

Refactored into a modular API-based system

⸻

⭐ Why This Project Matters

This is not just a digit classifier—it demonstrates:
	•	API-first ML system design
	•	Decoupled architecture
	•	Real-world deployability
	•	Clean engineering practices
