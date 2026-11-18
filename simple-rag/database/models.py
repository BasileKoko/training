from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from rag.chunking import get_policy_chunks

chunks = get_policy_chunks()
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
