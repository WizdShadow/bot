from bot import bot
import commands
from database.models import db, User, Film
import telebot
from telebot.types import BotCommand



commands = [
    BotCommand('start', 'Запуск бота'),
    BotCommand('movie_search', 'Поиск фильмов по названию'),
    BotCommand('movie_by_rating', 'Поиск фильмов по рейтингу'),
    BotCommand('low_budget_movie', 'Поиск фильмов низкого бюджета'),
    BotCommand('high_budget_movie', 'Поиск фильмов высокого бюджета'),
    BotCommand('history', 'История запросов'),
]
bot.set_my_commands(commands)



if __name__ == '__main__':
    db.connect()
    db.create_tables([User, Film], )
    db.close()
    print("Бот запущен...")
    bot.polling(none_stop=True)