from dotenv import load_dotenv
import os
from src.helper import load_pdf_file, filter_to_minimal_docs, text_split, download_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY").strip()



extracted_data = load_pdf_file(data='data/')
filter_data = filter_to_minimal_docs(extracted_data)
text_chunk = text_split(filter_data)

embeddings = download_embeddings()

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name = index_name,
        dimension = 384, # Dimension of the embeddings
        metric= "cosine", # We have to give similar metric and we are using cosine
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index("medical-chatbot")  

docsearch = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

docsearch.add_documents(text_chunk)

