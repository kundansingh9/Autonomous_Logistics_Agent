from langchain.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="phi3",
    base_url="http://localhost:11434"
)

vector_store = FAISS.from_texts(
    [result],
    embeddings
)

vector_store.save_local("vector_store")