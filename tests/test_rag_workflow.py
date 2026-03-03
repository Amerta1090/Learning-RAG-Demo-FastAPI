from app.services.rag_workflow import RagWorkflow

class FakeStore:
    def search(self, vector, query, limit=2):
        return ["Mocked context"]

class FakeEmbedding:
    def embed(self, text):
        return [0.1] * 128

def test_rag_workflow_returns_answer():
    rag = RagWorkflow(FakeStore(), FakeEmbedding())
    result = rag.ask("any question")

    assert "answer" in result
    assert "Mocked context" in result["answer"]
