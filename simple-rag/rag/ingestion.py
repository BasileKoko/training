from pathlib import Path
import chromadb
from langchain_huggingface import HuggingFaceEmbeddings
from rag.chunking import get_policy_chunks

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_PATH = BASE_DIR / "chroma_db"
COLLECTION_NAME = "rag_project_docs"


def store_policy_embeddings():
    chunks = get_policy_chunks()
    embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

    texts = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]
    ids = [f"policy_chunk_{i}" for i in range(len(chunks))]
    doc_embeddings = embeddings_model.embed_documents(texts)

    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=doc_embeddings,
        metadatas=metadatas,
    )

    print(f"Stored {collection.count()} items in '{COLLECTION_NAME}' at {CHROMA_PATH}")
    return collection


if __name__ == "__main__":
    store_policy_embeddings()