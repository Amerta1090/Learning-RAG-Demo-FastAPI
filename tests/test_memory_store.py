from app.stores.memory_store import InMemoryStore

def test_add_and_search():
    store = InMemoryStore()
    store.add("This is a test document", [0.1]*128)
    
    results = store.search([0.1]*128, "test")
    
    assert len(results) > 0
    assert "test document" in results[0]
