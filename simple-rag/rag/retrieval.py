from langchain.llms import OpenAI
from langchain.chains import RetrievalQA


llm = OpenAI(temperature=0)
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)