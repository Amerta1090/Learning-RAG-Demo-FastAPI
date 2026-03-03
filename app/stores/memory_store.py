# stores/memory_store.py
from .base import DocumentStore

class InMemoryStore(DocumentStore):

    def __init__(self):
        self.docs = []

    def add(self, text: str, vector: list[float]) -> int:
        self.docs.append(text)
        return len(self.docs) - 1

    def search(self, vector: list[float], query: str, limit: int = 2) -> list[str]:
        results = [doc for doc in self.docs if query.lower() in doc.lower()]
        if not results and self.docs:
            results = [self.docs[0]]
        return results[:limit]
