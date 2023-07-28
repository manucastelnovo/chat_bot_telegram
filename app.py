import logging 
import telegram
from telegram.ext import Updater, MessageHandler, Filters 

# token del bot 
TOKEN = '6431750259:AAFkqdNr4w4e_gsPlpDiS1FJq8-g6y3E6Is'
       
# lee y valida el texto 
def print_message (update, context): 
        
    # obtener el texto que envio al chat
    text = update.message.text

    print(text)
       
if __name__ == '__main__': 
    # obtener info del bot 
    myBot = telegram.Bot(token =  TOKEN)

updater = Updater(myBot.token, use_context=True) # updater: recibe mensajes y comandos 
dp = updater.dispatcher  # dispathcher: comandos que puede recibir 

# message handler 
dp.add_handler(MessageHandler (Filters.text, print_message))

# polling o sondeo 
updater.start_polling()
