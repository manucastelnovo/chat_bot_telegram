import telegram
from telegram.ext import Updater, MessageHandler, Filters 

class TelegramService(): 

    def __init__(self, env_token): 
        self.msj = None 
        self.my_bot = telegram.Bot(token =  env_token)
        self.create_listener()
       
    def create_listener(self): 
        updater = Updater(self.my_bot.token, use_context=True)
        dp = updater.dispatcher  
        dp.add_handler(MessageHandler (Filters.text, self.print_message))
        updater.start_polling()
       
    def print_message (self, update, context):   
        self.msj = update.message.text
        print(self.msj) 
        
   