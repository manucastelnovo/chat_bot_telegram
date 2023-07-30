from service.telegram_service import TelegramService
from service.langchain_service import embeddings,texts
from service.pinecone_service import index

TOKEN = ''

if __name__ == '__main__': 
    listener = TelegramService(TOKEN)

# hacer el split

# embedizar

vectors=[]
print(texts)

for embedding,i in enumerate(embeddings):
   
    vectors.append({
            'id':i, 
            'values':embedding, 
            'metadata':{'page_content': texts[i]},
            })

print(vectors)
upsert_response = index.upsert(vectors)