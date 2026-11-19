
from pathlib import Path
import chromadb
from langchain_huggingface import HuggingFaceEmbeddings

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_PATH = BASE_DIR / "chroma_db"
COLLECTION_NAME = "rag_project_docs"

client = chromadb.PersistentClient(path=str(CHROMA_PATH))
collection = client.get_collection(name=COLLECTION_NAME)
embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")


def retrieve_documents(query_text: str, n_results: int = 3):
    query_embedding = embeddings_model.embed_query(query_text)
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )


# if __name__ == "__main__":
#     print("Count:", collection.count())
#     print(retrieve_documents("parental leave eligibility"))