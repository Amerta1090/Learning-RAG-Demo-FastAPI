# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.embedding import EmbeddingService
from services.rag_workflow import RagWorkflow
from stores.memory_store import InMemoryStore
from stores.qdrant_store import QdrantStore

app = FastAPI(title="Learning RAG Demo")

# Dependency wiring
embedding_service = EmbeddingService()

try:
    store = QdrantStore("http://localhost:6333")
except Exception:
    store = InMemoryStore()

rag = RagWorkflow(store, embedding_service)


class QuestionRequest(BaseModel):
    question: str


class DocumentRequest(BaseModel):
    text: str


@app.post("/add")
def add_document(req: DocumentRequest):
    vector = embedding_service.embed(req.text)
    doc_id = store.add(req.text, vector)
    return {"id": doc_id, "status": "added"}


@app.post("/ask")
def ask_question(req: QuestionRequest):
    try:
        result = rag.ask(req.question)
        return {
            "question": req.question,
            "answer": result["answer"],
            "context_used": result.get("context", [])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/status")
def status():
    return {
        "store_type": type(store).__name__,
        "documents_count": getattr(store, "docs", None) and len(store.docs),
        "graph_ready": rag is not None
    }
