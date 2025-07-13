FROM python:3.9
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY prediction_fastapi.py .
COPY dense_neural_class.py .
COPY utils.py .
COPY model.pkl .
EXPOSE 5000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["uvicorn", "prediction_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]