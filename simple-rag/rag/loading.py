from langchain_docling.loader import DoclingLoader
from pathlib import Path


def load_policy_documents() -> list:
    # 1. Point to docs directory
    DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"

    # 2. Gather all .txt  files into a list of strings
    file_paths = [str(p) for p in DOCS_DIR.glob("*.txt")]

    # 3. Pass the list to DoclingLoader
    loader = DoclingLoader(file_path=file_paths)
    # print("Loading documents...")
    # return  loader.load()

    if not file_paths:
        raise FileNotFoundError(f"No .txt files found in {DOCS_DIR}")

        # 3. Load documents
    loader = DoclingLoader(file_path=file_paths)

    print("Loading documents...")
    documents = loader.load()

    # 4. Normalise metadata for vector database compatibility
    for doc in documents:
        clean_metadata = {}

        for key, value in doc.metadata.items():
            if value is None or isinstance(value, (str, int, float, bool)):
                clean_metadata[key] = value
            else:
                clean_metadata[key] = str(value)

        doc.metadata = clean_metadata

    return documents

