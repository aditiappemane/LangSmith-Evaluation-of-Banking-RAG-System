def get_retriever(vector_store):
    return vector_store.as_retriever() 