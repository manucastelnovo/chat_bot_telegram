from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import openai
import pinecone 
import time
import os
from dotenv import load_dotenv

load_dotenv()

open_ai_api_key = os.getenv("OPEN_AI_KEY")
pinecone_api_key=os.getenv("PINECONE_API_KEY")



with open('codigo_del_trabajador.txt') as f:
    document = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    separators= ["\nARTÍCULO"],
    chunk_size=1500,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False
)

texts = text_splitter.create_documents([document])
metadatas = []

for text in texts:
    metadata = {
        'document': text.page_content,
    }
    metadatas.append(metadata)


documents = text_splitter.create_documents([document], metadatas=metadatas)




embeddings_model = OpenAIEmbeddings(openai_api_key=open_ai_api_key)

# print(len(embeddings[0]))
# print(embeddings)

contador= 1
pinecone.init(api_key=pinecone_api_key, environment='asia-southeast1-gcp') 
index = pinecone.Index('trabajo') 
for indice, document_index in enumerate(documents):

    embeddings = embeddings_model.embed_documents(
        document_index.page_content
    )
    upsert_response = index.upsert(
        vectors=[{
            'id':str(contador), 
            'values':embeddings[0], 
            'metadata':{'page_content': documents[indice].page_content,
               }}],
               namespace='example-namespace')
    contador=contador+1
    print(upsert_response)
    print(documents[indice].page_content)
    # print(embeddings)
    # print(indice)




