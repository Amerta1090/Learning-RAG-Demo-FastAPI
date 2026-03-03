# services/rag_workflow.py
from langgraph.graph import StateGraph, END

class RagWorkflow:

    def __init__(self, store, embedding_service):
        self.store = store
        self.embedding_service = embedding_service
        self.chain = self._build_graph()

    def _build_graph(self):
        workflow = StateGraph(dict)

        workflow.add_node("retrieve", self._retrieve)
        workflow.add_node("answer", self._answer)

        workflow.set_entry_point("retrieve")
        workflow.add_edge("retrieve", "answer")
        workflow.add_edge("answer", END)

        return workflow.compile()

    def _retrieve(self, state):
        query = state["question"]
        vector = self.embedding_service.embed(query)
        state["context"] = self.store.search(vector, query)
        return state

    def _answer(self, state):
        ctx = state.get("context", [])
        state["answer"] = (
            f"I found this: '{ctx[0][:100]}...'"
            if ctx else
            "Sorry, I don't know."
        )
        return state

    def ask(self, question: str) -> dict:
        return self.chain.invoke({"question": question})
