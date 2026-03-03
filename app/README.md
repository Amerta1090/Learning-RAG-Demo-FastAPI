# Learning RAG Demo (Refactored)

This project demonstrates a refactored Retrieval-Augmented Generation (RAG) service
built with FastAPI, LangGraph, and Qdrant (with in-memory fallback).

## Architecture Overview

The application is structured into clear layers:

- API Layer (HTTP handling)
- Service Layer (Embedding & RAG workflow)
- Storage Layer (Qdrant or in-memory)
- Dependency Wiring Layer

This design improves:
- Separation of concerns
- Testability
- Extensibility

## Setup

### 1. Create Virtual Environment

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

### 2. Install Dependencies

cd app
pip install -r requirements.txt

### 3. Run Application

uvicorn app.main:app --reload

API will be available at:
http://127.0.0.1:8000

Swagger docs:
http://127.0.0.1:8000/docs

---

## Endpoints

POST /add
{
  "text": "example document"
}

POST /ask
{
  "question": "example query"
}

GET /status

---

## Running with Qdrant

Make sure Qdrant is running locally:

docker run -p 6333:6333 qdrant/qdrant

If Qdrant is unavailable, the app automatically falls back to in-memory storage.

---

## Running Tests

pytest
