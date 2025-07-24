from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def get_vector_store(chunks, config):
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(chunks, embeddings)
    return vector_store 