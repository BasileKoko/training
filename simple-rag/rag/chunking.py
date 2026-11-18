from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path


# Load example document
ROOT_DIR = Path(__file__).resolve().parent.parent
policy_path = ROOT_DIR / "docs" / "company_policy_handbook.txt"

with open(policy_path) as f:
    company_policy= f.read()

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)

texts = text_splitter.create_documents([company_policy])
print(texts[0])
print(texts[1])
print(texts[2])
print(texts[3])