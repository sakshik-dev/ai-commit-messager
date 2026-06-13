FROM python:3.10-slim

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy full project
COPY . .

ENV PYTHONUNBUFFERED=1

# Cloud Run uses PORT env variable
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8080"]