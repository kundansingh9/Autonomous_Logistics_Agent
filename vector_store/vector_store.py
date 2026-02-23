from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings


def save_to_vector_store(text: str):
    """
    Save research result text into FAISS vector store.
    """

    embeddings = OllamaEmbeddings(
        model="phi3",
        base_url="http://localhost:11434"
    )

    vector_store = FAISS.from_texts(
        [text],
        embeddings
    )

    vector_store.save_local("vector_store")