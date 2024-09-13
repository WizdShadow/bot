import telebot
from bot import bot
from database import zapros


def get_history(message, user_id,spisoc):
            number = int(message.text)
            if 1 <= number <= 1:
                name_film = spisoc[number-1]
                text = zapros.info_check2(user_id,name_film)
                bot.send_message(message.chat.id, text)
                
            else:
                bot.send_message(message.chat.id, 'Неверно введено число. Попробуйте снова.')
            # Повторите запрос числа, если это необходимо
                bot.send_message(message.chat.id, 'Укажите цифру фильма, который вы хотите посмотреть снова.')
                bot.register_next_step_handler(message, get_history, user_id)
            
    

@bot.message_handler(commands=['history'])
def start(message):
    user_id = message.from_user.id
    filsm , spisoc = zapros.info_check(user_id)
    if not filsm:
        bot.send_message(message.chat.id, 'Вы пока не запросили ни одного фильма')
    else:
        bot.send_message(message.chat.id, 'Ваш список запросов\n ' + filsm)
        
    
        bot.send_message(message.chat.id, 'Укажите цифру фильма, который вы хотите посмотреть')
        bot.register_next_step_handler(message, get_history, user_id, spisoc)
        
        