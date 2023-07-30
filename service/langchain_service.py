from langchain.embeddings import OpenAIEmbeddings
# This is a long document we can split up.
from langchain.text_splitter import CharacterTextSplitter

with open('Apocalipsis.txt') as f:
    document = f.read()

text_splitter = CharacterTextSplitter(        
    separator = ".\n",
    chunk_size = 1000,
    chunk_overlap  = 0,
    length_function = len,
)

texts = text_splitter.create_documents(document)
metadatas = []

# print(texts)
for text in texts:

    metadatas.append(text.page_content)


# documents = text_splitter.create_documents([document], metadatas=metadatas)
# print(metadatas)


embeddings_model = OpenAIEmbeddings(openai_api_key="")


embeddings = embeddings_model.embed_documents(
    metadatas
)
# print(len(embeddings))
# print(embeddings)
