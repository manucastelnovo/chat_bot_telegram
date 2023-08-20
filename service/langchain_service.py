from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import openai
import pinecone 
import telegram
from telegram.ext import Updater, MessageHandler, Filters 
import os
from dotenv import load_dotenv

load_dotenv()

open_ai_api_key = os.getenv("OPEN_AI_KEY")
pinecone_api_key=os.getenv("PINECONE_API_KEY")

mock_message = 'como calculo mi vacaciones'
namespaces = ['aguinaldo','vacaciones']
namespace_on_message = ''

def detect_namespace(message):
    for word in message.split():
        if word in namespaces:
            namespace_on_message = word
            print(namespace_on_message)




def semantic_search(message):
    embeddings_model = OpenAIEmbeddings(openai_api_key=open_ai_api_key)




    pinecone.init(api_key=pinecone_api_key, environment='asia-southeast1-gcp') 
    index = pinecone.Index('trabajo') 

  

    print(f"pregunte : {message}")
    query = message

    # create the query vector
    model = embeddings_model.embed_documents(query)
    print(model)

    # xq = model.tolist()

    # now query
    response = index.query(model[0], top_k=5, include_metadata=True)
    # print(response.matches[0].metadata)

    print('estos son los vectores de pinecone')
    print(str(response.matches))

    openai.api_key = open_ai_api_key

    prompt=f"Eres un chatbot de whatsapp, este es el contexto para tu respuesta: {response.matches[0].metadata} y este el mensaje del usuario:{query} puedes responder como si fueras abogado experto en el codigo del trabajador paraguayo"
    
    print(prompt)

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
        
   
# create_listener()

