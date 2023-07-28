from service.telegram_service import print_message,init_telegram_listener

TOKEN = '6431750259:AAFkqdNr4w4e_gsPlpDiS1FJq8-g6y3E6Is'

if __name__ == '__main__': 
    init_telegram_listener(TOKEN,print_message)