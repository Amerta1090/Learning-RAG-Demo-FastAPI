## Running Tests

hasil pytest
<img width="1628" height="323" alt="image" src="https://github.com/user-attachments/assets/cd045691-0020-4db7-ba3b-39c6d7cdb9f0" />

The test suite successfully processed three key test files—test_embedding.py, test_memory_store.py, and test_rag_workflow.py—achieving a **100%** pass rate in under one second. This confirms that the embedding generation, memory storage, and Retrieval-Augmented Generation (RAG) workflows are functioning correctly within the local environment. While the tests are successful, the output notes a minor compatibility warning regarding Pydantic V1 and Python 3.14, which is currently managed by the langchain_core dependency and does not impact the current test validity.
