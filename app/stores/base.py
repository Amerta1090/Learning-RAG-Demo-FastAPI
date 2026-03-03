# stores/base.py
from abc import ABC, abstractmethod

class DocumentStore(ABC):

    @abstractmethod
    def add(self, text: str, vector: list[float]) -> int:
        pass

    @abstractmethod
    def search(self, vector: list[float], query: str, limit: int = 2) -> list[str]:
        pass
