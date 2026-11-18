from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.loading import load_policy_documents


def get_policy_chunks() -> list:
    # 1. Load documents from the loading module
    documents = load_policy_documents()

    # 2. Configure splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
    )

    # 3. Split and return chunks
    return text_splitter.split_documents(documents)


if __name__ == "__main__":
    chunks = get_policy_chunks()
    # print(f"Successfully generated {len(chunks)} chunks.")
    # print(f"First chunk preview:\n{chunks[0].page_content[:150]}...")