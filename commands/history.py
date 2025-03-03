import telebot
from bot import bot
from database import zapros
from KeyboardButton.KeyboardButton import create_buttons


def get_history(message, user_id,spisoc):
            number = int(message.text)
            if 1 <= number <= len(spisoc):
                name_film = spisoc[number-1]
                text, photo = zapros.info_check2(user_id,name_film)
                bot.send_photo(message.chat.id, photo, caption=text, reply_markup=telebot.types.ReplyKeyboardRemove())
                
            else:
                bot.send_message(message.chat.id, 'Неверно введено число. Попробуйте снова.')
            # Повторите запрос числа, если это необходимо
                bot.send_message(message.chat.id, 'Укажите цифру фильма, который вы хотите посмотреть снова.')
                bot.register_next_step_handler(message, get_history, user_id)
            
    

@bot.message_handler(commands=['history'])
def historys(message):
    user_id = message.from_user.id
    filsm , spisoc = zapros.info_check(user_id)
    if not filsm:
        bot.send_message(message.chat.id, 'Вы пока не запросили ни одного фильма')
    else:
        bot.send_message(message.chat.id, 'Ваш список запросов\n ' + filsm)
        marky = create_buttons(len(spisoc))
        
        bot.send_message(message.chat.id, 'Укажите цифру фильма, который вы хотите посмотреть', reply_markup=marky)
        bot.register_next_step_handler(message, get_history, user_id, spisoc)
        
        