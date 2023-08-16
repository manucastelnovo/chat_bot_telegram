import telegram
from telegram.ext import Updater, MessageHandler, Filters 

my_bot = telegram.Bot(token =  '6519212683:AAHpcXNJ_9YuIv1sKRVErfRZtU7BWGKMzAI')
updater = Updater(my_bot.token, use_context=True)


def create_listener(): 
    dp = updater.dispatcher  
    dp.add_handler(MessageHandler (Filters.text, print_message))
    updater.start_polling()
       
def print_message (update,context):
       
    msj = update.message.text
    print(msj)
    return msj
        
   
create_listener()


