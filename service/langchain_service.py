from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import openai
import pinecone 
import telegram
from telegram.ext import Updater, MessageHandler, Filters 



with open('Apocalipsis.txt') as f:
    document = f.read()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)

# texts = text_splitter.create_documents([document])
# metadatas = []

# for text in texts:
#     metadata = {
#         'document': text.page_content,
#     }
#     metadatas.append(metadata)

# documents = text_splitter.create_documents([document], metadatas=metadatas)
# print(documents[0])


def semantic_search(message):
    embeddings_model = OpenAIEmbeddings(openai_api_key="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")




    # embeddings = embeddings_model.embed_documents(
    #     documents[0].page_content
    # )
    # print(len(embeddings[0]))
    # print(embeddings)




    pinecone.init(api_key='f39718d6-40ba-465c-87bc-78678de8bb52', environment='asia-southeast1-gcp') 
    index = pinecone.Index('apocalipsis') 

    # upsert_response = index.upsert(
    #     vectors=[{
    #         'id':'vec1', 
    #         'values':embeddings[0], 
    #         'metadata':{'page_content': documents[0].page_content,

    #            }}])

    print(f"pregunte : {message}")
    query = message

    # create the query vector
    model = embeddings_model.embed_documents(query)


    # xq = model.tolist()

    # now query
    response = index.query([model[0]], top_k=5, include_metadata=True)
    # print(response.matches[0].metadata)

    print('estos son los vectores de pinecone')
    print(str(response.matches))

    openai.api_key = "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"

    prompt=f"Eres un chatbot de whatsapp, este es el contexto de mi respuesta: {response.matches[0].metadata} y este el mensaje del usuario:{query} puedes responder como si fueras un narrador que esta contando la historia del apocalipsis"
    
    response_openai = openai.Completion.create(
          model="text-davinci-003",
          prompt=prompt,
          temperature=0,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
      )

    print(response_openai.choices[0].text)
    return response_openai.choices[0].text


my_bot = telegram.Bot(token =  '6519212683:AAHpcXNJ_9YuIv1sKRVErfRZtU7BWGKMzAI')
updater = Updater(my_bot.token, use_context=True)


def create_listener(): 
    dp = updater.dispatcher  
    dp.add_handler(MessageHandler (Filters.text, print_message))
    updater.start_polling()
       
def print_message (update,context):
    
    msj = update.message.text
    print(msj)
    toTelegram=semantic_search(msj)
    my_bot.send_message(update.message.chat.id,toTelegram)
    return msj
        
   
create_listener()

