from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, START, END

from .config import llm,collection  # Ensure you have llm configured in a separate config.py file


# Define Bot State
class BotState(TypedDict):
    session_id: str
    user_id: str
    message: str
    documents: List[str]
    answer: str

def retrieve_docs(state: BotState):
    results = collection.query(
        query_texts=[state['message']], # Chroma will embed this for you
        n_results=3 # how many results to return
    )
    return {"documents":results["documents"]}

def answer_node(state: BotState):
    prompt = f"""
You are a medical Professor in MIT.
Your task is to analyze this symptom:
\"""
{state['message']}
\"""
You are provided some related facts:
\"""
{state['documents']}
\"""
Identify the issue of the patient, and give some advice based on given documents and your own knowledge.
    """
    response = llm.invoke(prompt)
    return {"answer":response.content}

# Define LangGraph workflow
graph = StateGraph(BotState)
graph.add_node("retrieve_docs",retrieve_docs)
graph.add_node("answer_node", answer_node)

graph.add_edge(START, "retrieve_docs")
graph.add_edge("retrieve_docs", "answer_node")
graph.add_edge("answer_node", END)

workflow = graph.compile()
