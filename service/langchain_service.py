# This is a long document we can split up.
from langchain.text_splitter import CharacterTextSplitter

with open('Apocalipsis.txt') as f:
    document = f.read()

text_splitter = CharacterTextSplitter(        
    separator = ".\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)

texts = text_splitter.create_documents([document])
metadatas = []

for text in texts:
    metadatas.append({'document':text.page_content})


documents = text_splitter.create_documents([document], metadatas=metadatas)
print(documents[1])