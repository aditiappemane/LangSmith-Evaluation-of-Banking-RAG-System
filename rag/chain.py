from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def run_qa_chain(query, retriever, config):
    llm = OpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(query) 