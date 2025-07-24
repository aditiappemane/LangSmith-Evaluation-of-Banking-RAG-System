from langchain.document_loaders import UnstructuredFileLoader, PyPDFLoader
import os

def load_documents(data_path):
    docs = []
    for fname in os.listdir(data_path):
        fpath = os.path.join(data_path, fname)
        if fname.lower().endswith('.pdf'):
            loader = PyPDFLoader(fpath)
            docs.extend(loader.load())
        else:
            loader = UnstructuredFileLoader(fpath)
            docs.extend(loader.load())
    return docs 