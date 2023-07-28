import logging 
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 

# metodo para rastrear eventos (para ver lo que hace el bot)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,")
logger = logging.getLogger()

# token del bot 
TOKEN = '6431750259:AAFkqdNr4w4e_gsPlpDiS1FJq8-g6y3E6Is'
       
# lee y valida el texto 
def echo (update, context): 
    
    # obtener el id del mensaje 
    updateMsg = getattr(update, 'message', None) # guardamos todos los datos del mensaje 
    messageId = updateMsg.message_id 
    
    # obtener el texto que envio al chat
    text = update.message.text

    print(text)
    
# main
if __name__ == '__main__': 
    # obtener info del bot 
    myBot = telegram.Bot(token =  TOKEN)

updater = Updater(myBot.token, use_context=True) # updater: recibe mensajes y comandos 
dp = updater.dispatcher  # dispathcher: comandos que puede recibir 

# mensajes!
dp.add_handler(MessageHandler (Filters.text, echo))

# polling 
updater.start_polling()
updater.idle() 