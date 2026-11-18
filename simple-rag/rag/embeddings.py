from langchain_huggingface import HuggingFaceEmbeddings
from rag.chunking import get_policy_chunks


def generate_policy_embeddings():
    # 1. Fetch chunks from your chunking module
    chunks = get_policy_chunks()

    # 2. Initialize the Hugging Face embedding model
    # (This will automatically download the model weights on first run)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

    # 3. Extract just the text content from the LangChain Document objects
    texts = [chunk.page_content for chunk in chunks]

    # 4. Generate embeddings for all chunks
    doc_embeddings = embeddings.embed_documents(texts)

    # print(f"Successfully generated embeddings for {len(doc_embeddings)} chunks.")
    # print(f"Vector dimensionality: {len(doc_embeddings[0])} dimensions")

    return chunks, doc_embeddings, embeddings


if __name__ == "__main__":
    generate_policy_embeddings()