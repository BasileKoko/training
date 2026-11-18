# from langchain.llms import OpenAI
# from langchain.chains import RetrievalQA
#
#
# llm = OpenAI(temperature=0)
# rag_chain = RetrievalQA.from_chain_type(
#     llm=llm,
#     retriever=retriever,
#     return_source_documents=True
# )
#
# retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


similar_docs = vector_store.similarity_search("your query here")