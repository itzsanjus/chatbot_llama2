from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DATA_PATH = "data/"
DB_FAISS_PATH = "vectorstores/db_faiss"

def create_vectorDB():
    # Loading the Data of .pdf
    loader = DirectoryLoader(DATA_PATH, glob = '*.pdf', loader_cls= PyPDFLoader)
    documents = loader.load()

    # Splitting the into texts from data
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
    texts = text_splitter.split_documents(documents)

    # Creating Embeddings
    embeddings = HuggingFaceEmbeddings(model_name = 'obrizum/all-MiniLM-L6-v2', 
                                       model_kwargs = {'device' : 'cpu'})
    '''
        To run on gpu, just change the device : cpu to
        device : gpu
        '''
    db = FAISS.from_documents(texts, embeddings)
    
    # Saving Locally
    db.save_local(DB_FAISS_PATH)


if __name__ == "__main__":
    create_vectorDB()
