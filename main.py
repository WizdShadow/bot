from bot import bot
import commands
import database



if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)