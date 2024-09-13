# addfilm.py
from peewee import *

# Определяем базу данных
db = SqliteDatabase('my_database.db')

class User(Model):
    user_name = CharField(unique=True)  # Сделаем имя пользователя уникальным

    class Meta:
        database = db

class Film(Model):
    name = CharField()
    description = CharField()
    rating = CharField()
    year = CharField()
    genre = CharField()
    age_rating = CharField()
    poster_url = CharField()
    user = ForeignKeyField(User, backref='films')  # Связь с таблицей Users

    class Meta:
        database = db

def initialize_db():
    """Создает таблицы, если они еще не существуют."""
    if db.is_closed():
        db.connect()
    db.create_tables([User, Film], safe=True)

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
        name=name,
        description=description,
        rating=rating,
        year=year,
        genre=genre,
        age_rating=age_rating,
        poster_url=poster_url,
        user=user
    )
    print(f"Фильм '{name}' успешно добавлен.")


# Инициализация базы данных при импорте модуля
initialize_db()