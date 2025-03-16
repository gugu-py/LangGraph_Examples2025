import os

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key="your-key",
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    # other params...
)

import chromadb
chroma_client = chromadb.PersistentClient()
# chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="my_collection")
