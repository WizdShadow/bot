from bot import bot
import commands
import database
import telebot
from telebot.types import BotCommand



commands = [
    BotCommand('start', 'Запуск бота'),
    BotCommand('movie_search', 'Поиск фильмов по названию'),
    BotCommand('history', 'История запросов'),
    BotCommand('movie_by_rating', 'Поиск фильмов по рейтингу'),
]
bot.set_my_commands(commands)



if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)