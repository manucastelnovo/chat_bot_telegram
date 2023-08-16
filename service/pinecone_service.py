from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import openai
import pinecone 




with open('Apocalipsis.txt') as f:
    document = f.read()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)

texts = text_splitter.create_documents([document])
metadatas = []

for text in texts:
    metadata = {
        'document': text.page_content,
    }
    metadatas.append(metadata)

documents = text_splitter.create_documents([document], metadatas=metadatas)
print(documents[0])



embeddings_model = OpenAIEmbeddings(openai_api_key="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")

# print(len(embeddings[0]))
# print(embeddings)

contador= 1
pinecone.init(api_key='f39718d6-40ba-465c-87bc-78678de8bb52', environment='asia-southeast1-gcp') 
index = pinecone.Index('apocalipsis') 
for indice, document_index in enumerate(documents):

    embeddings = embeddings_model.embed_documents(
        document_index.page_content
    )
    upsert_response = index.upsert(
        vectors=[{
            'id':str(contador), 
            'values':embeddings[0], 
            'metadata':{'page_content': documents[indice].page_content,
               }}])
    contador=contador+1
    print(upsert_response)
    # print(embeddings)
    # print(indice)




