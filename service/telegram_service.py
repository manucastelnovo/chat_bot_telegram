import telegram
from telegram.ext import Updater, MessageHandler, Filters
from service.langchain_service import semantic_search 
import os
from dotenv import load_dotenv

load_dotenv()

telegram_token = os.getenv("TELEGRAM_TOKEN")

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


