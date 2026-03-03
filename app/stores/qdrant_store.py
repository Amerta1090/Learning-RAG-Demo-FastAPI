# stores/qdrant_store.py
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from .base import DocumentStore

class QdrantStore(DocumentStore):

    def __init__(self, url: str):
        self.client = QdrantClient(url)
        self.collection = "demo_collection"
        self.client.recreate_collection(
            collection_name=self.collection,
            vectors_config=VectorParams(size=128, distance=Distance.COSINE)
        )

    def add(self, text: str, vector: list[float]) -> int:
        doc_id = hash(text)
        self.client.upsert(
            collection_name=self.collection,
            points=[PointStruct(id=doc_id, vector=vector, payload={"text": text})]
        )
        return doc_id

    def search(self, vector: list[float], query: str, limit: int = 2) -> list[str]:
        hits = self.client.search(
            collection_name=self.collection,
            query_vector=vector,
            limit=limit
        )
        return [hit.payload["text"] for hit in hits]
