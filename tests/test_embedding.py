from app.services.embedding import EmbeddingService

def test_embedding_is_deterministic():
    service = EmbeddingService()
    vec1 = service.embed("hello")
    vec2 = service.embed("hello")
    assert vec1 == vec2
    assert len(vec1) == 128
