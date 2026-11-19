from pathlib import Path
import chromadb
from google import genai
from google.genai import types
from dotenv import load_dotenv

from rag.retrieval import retrieve_documents

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_PATH = BASE_DIR / "chroma_db"
COLLECTION_NAME = "rag_project_docs"
GEN_MODEL="gemini-3.1-flash-lite"
SYSTEM_INSTRUCTION = (
    "You are a helpful assistant answering questions using ONLY the provided "
    "context chunks. If the context does not contain enough information to answer "
    "accurately, say that you don't know based on the provided documents. "
    "Do not invent policy rules or figures."
)

load_dotenv()


def generate_answer(llm_client: genai.Client, query: str, chunks: list[str]) -> str:
    """Sends the user query and retrieved context to Gemini."""
    context_block = "\n\n---\n\n".join(chunks) if chunks else "No relevant context found."
    prompt = f"Context:\n{context_block}\n\nUser Question:\n{query}"

    response = llm_client.models.generate_content(
        model=GEN_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.2,
        ),
    )
    return response.text or ""

def run_cli():
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    collection = client.get_collection(name=COLLECTION_NAME)

    print(f"Loaded '{COLLECTION_NAME}' ({collection.count()} chunks). Type 'exit' to quit.\n")

    with genai.Client() as llm_client:
        while True:
            try:
                user_query = input("Ask a question: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nExiting.")
                break

            if not user_query:
                continue
            if user_query.lower() in {"exit", "quit"}:
                print("Exiting.")
                break

            # 1. Get the raw dictionary from your existing retrieval function
            raw_results = retrieve_documents(user_query, n_results=3)

            # 2. Extract the list of text chunks (grab index [0] of "documents")
            chunks = raw_results["documents"][0]

            # 3. Join those strings into one clean block of text for the LLM
            # context = "\n\n---\n\n".join(chunks)
            # print(f"\nContext:\n{context}\n")
            # print(f"\nChunk:\n{chunks}\n")

            answer = generate_answer(llm_client, user_query, chunks)
            print(f"\nAnswer:\n{answer}\n")


if __name__ == "__main__":
    run_cli()



