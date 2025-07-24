import yaml
from rag.document_loader import load_documents
from rag.text_splitter import split_documents
from rag.vector_store import get_vector_store
from rag.retriever import get_retriever
from rag.chain import run_qa_chain

CONFIG_PATH = 'config/config.yaml'

if __name__ == "__main__":
    with open(CONFIG_PATH, 'r') as f:
        config = yaml.safe_load(f)

    # Load and split documents
    docs = load_documents(config['data_path'])
    chunks = split_documents(docs)

    # Vector store and retriever
    vector_store = get_vector_store(chunks, config)
    retriever = get_retriever(vector_store)

    # Run a sample query
    query = "What are the compliance requirements for loan products?"
    answer = run_qa_chain(query, retriever, config)
    print(f"Q: {query}\nA: {answer}") 