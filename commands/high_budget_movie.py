
import telebot
from api.apii import get_high_budget_movie
from api.im_down import down_im

from database import addfilm
from commands import history


from bot import bot
from KeyboardButton.KeyboardButton import create_buttons  # Импортируем вашу функцию создания кнопок



@bot.message_handler(commands=['high_budget_movie'])
def start(message):
    markup = create_buttons(5)
    bot.send_message(message.chat.id, 'Введите лимит вывода за страницу от 1 до 5:', reply_markup=markup)
    bot.register_next_step_handler(message, get_limit)


def get_limit(message,):
    
    try:
        if message.text == 'отмена' or message.text == "Отмена":
            bot.send_message(message.chat.id, "Вы отменили поиск, ожидаю другую команду", reply_markup=telebot.types.ReplyKeyboardRemove())
            return 
        limit_film = int(message.text)
        if 1 <= limit_film <= 5:
            bot.send_message(message.chat.id, 'Начал поиск, ожидайте...')
            page = 1
            show_movies(message.chat.id,limit_film, page)
        else:
            bot.send_message(message.chat.id, 'Лимит не может быть меньше 1 или больше 5. Попробуйте снова:')
            bot.register_next_step_handler(message, get_limit)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректное число.')
        bot.register_next_step_handler(message, get_limit)


def show_movies(chat_id,limit_film, page):
    data = get_high_budget_movie(limit_film, page)
    
    film = {}
    films_message = []
    media_group = []
    count = 1

    for i in data['docs']:
        name, description, rating, year, genres, age_rating, poster_url = i['name'], i['description'], i['rating']["kp"], i['year'], i['genres'], i['ageRating'], i.get('poster', {}).get('url', None)
        
        unique_key = f"{count}. {i.get('name', 'Неизвестно')} ({i.get('year', 'Неизвестно')})"
        film[unique_key] = {'name': name,
                            'description': description,
                            'rating': rating,
                            'year': year,
                            'genres': genres,
                            'age_rating': age_rating,
                            'poster_url': poster_url}
        films_message.append(unique_key)
        if not poster_url:
            with open("file/no_poster.png", "rb") as file:
                data = file.read()
                media_group.append(telebot.types.InputMediaPhoto(data))
                film[unique_key][poster_url] = data
        else:
            data = down_im(poster_url)
            media_group.append(telebot.types.InputMediaPhoto(data))
            film[unique_key][poster_url] = data
        count += 1

    keys_message = "\n".join(films_message)

    # Создаем клавиатуру с кнопками для выбора фильма
    markup = create_buttons(len(film))

    # Отправляем текстовое сообщение с кнопками
    bot.send_message(chat_id, "Вот список фильмов:\n\n" + keys_message, reply_markup=markup)

    # Отправляем медиагруппу, если она не пустая
    if media_group:
        try:
            bot.send_media_group(chat_id, media_group)
        except telebot.apihelper.ApiHTTPException as e:
            bot.send_message(chat_id, f"Произошла ошибка при отправке медиа: {e}")

    bot.send_message(chat_id, "Укажите номер фильма из списка, который хотите увидеть, или напишите 'еще' для следующей страницы.")
    bot.register_next_step_handler_by_chat_id(chat_id, process_user_choice, film,limit_film, page)


def process_user_choice(message, film,limit_film, page):
    text = message.text.strip()
    if text.lower() == 'еще':
        page += 1
        show_movies(message.chat.id,limit_film, page)
    elif text.isdigit() and 1 <= int(text) <= len(film):
        keys = list(film.keys())
        selected_key = keys[int(text) - 1]
        film_details = film[selected_key]
        
        # Обрабатываем жанры, если они представлены в виде словарей
        genres = [genre.get('name', 'Неизвестно') for genre in film_details['genres']]
        
        # Формируем сообщение с информацией о фильме
        details_message = (
            f"Название: {film_details['name']}\n"
            f"Описание: {film_details['description']}\n"
            f"Рейтинг: {round(film_details['rating'], 1)}\n"
            f"Год: {film_details['year']}\n"
            f"Жанры: {', '.join(genres)}\n"
            f"Возрастной рейтинг: {film_details['age_rating']}\n"
        )
        
        # Отправляем постер и информацию о фильме
        if film_details['poster_url']:
            user_id = message.from_user.id
            bot.send_photo(message.chat.id, film_details['poster_url'], caption=details_message, reply_markup=telebot.types.ReplyKeyboardRemove())
            
            # Сохраняем информацию о фильме в базе данных
            addfilm.add_film( 
                      film_details['name'], 
                      film_details['description'], 
                      film_details['rating'],
                      film_details['year'], 
                      genres, 
                      film_details['age_rating'], 
                      film_details['poster_url'],
                      user_id)
          
            
        else:
            bot.send_message(message.chat.id, details_message)
            
    elif message.text == 'отмена' or message.text == "Отмена":
        bot.send_message(message.chat.id, "Вы отменили поиск, ожидаю другую команду", reply_markup=telebot.types.ReplyKeyboardRemove())
        return
    
    else:
        bot.send_message(message.chat.id, 'Некорректный выбор. Попробуйте снова.')
        bot.register_next_step_handler(message, process_user_choice, film,limit_film, page)




if __name__ == "__main__":
    bot.polling()
