
#KeyboardButton\KeyboardButton.py
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def create_buttons(num_buttons):
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    buttons = [KeyboardButton(f"{i + 1}") for i in range(num_buttons)]
    markup.add(*buttons)
    return markup
