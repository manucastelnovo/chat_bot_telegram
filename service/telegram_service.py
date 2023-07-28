import telegram
from telegram.ext import Updater, MessageHandler, Filters 


       
def print_message (update, context):   
    text = update.message.text
    print(text)
       

def init_telegram_listener(env_token,call_back):
    myBot = telegram.Bot(token =  env_token)
    updater = Updater(myBot.token, use_context=True)
    dp = updater.dispatcher  
    dp.add_handler(MessageHandler (Filters.text, call_back))
    updater.start_polling()