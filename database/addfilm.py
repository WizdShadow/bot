# addfilm.py
from peewee import *
from .models import User, Film, db


def add_film(name, description, rating, year, genre, age_rating, poster_url, user_name):
    """Добавляет фильм в базу данных и связывает его с пользователем. Если у пользователя уже есть 5 фильмов, заменяет самый старый фильм."""
    user, created = User.get_or_create(user_name=user_name)
    
    # Проверяем, сколько фильмов у пользователя
    user_films = Film.select().where(Film.user == user)
    
    if user_films.count() >= 5:
        # Находим самый старый фильм (по порядку добавления) и удаляем его
        oldest_film = user_films.order_by(Film.id).get()  # Предполагается, что поле `id` автоинкрементируется
        oldest_film.delete_instance()
        print(f"Фильм '{oldest_film.name}' удален, так как у пользователя достигнут лимит в 5 фильмов.")
    
    # Добавляем новый фильм
    Film.create(
        name=name or 'Название отсутствует',
        description=description or 'Описание отсутствует',
        rating=rating or 'Рэтинг отсутствует',
        year=year or 'Год отсутствует',
        genre=genre or 'Жанр отсутствует',
        age_rating=age_rating or 'Возрастной рейтинг отсутствует',
        poster_url=poster_url or 'Постер отсутствует',
        user=user
    )
    print(f"Фильм '{name}' успешно добавлен.")



