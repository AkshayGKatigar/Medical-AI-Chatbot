from dotenv import load_dotenv
import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from src.helper import load_pdf_file, filter_to_minimal_docs, text_split, download_embeddings

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

def get_vector_store():
    embeddings = download_embeddings()

    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index("medical-chatbot")

    vector_store = PineconeVectorStore(
        index=index,
        embedding=embeddings
    )

    return vector_store


def setup_vector_store():
    extracted_data = load_pdf_file(data='data/')
    filter_data = filter_to_minimal_docs(extracted_data)
    text_chunk = text_split(filter_data)

    embeddings = download_embeddings()

    pc = Pinecone(api_key=PINECONE_API_KEY)

    index_name = "medical-chatbot"

    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )

    index = pc.Index(index_name)

    vector_store = PineconeVectorStore(
        index=index,
        embedding=embeddings
    )

    vector_store.add_documents(text_chunk)