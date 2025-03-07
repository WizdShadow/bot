from peewee import * 

db = SqliteDatabase('database/film_db.db')

class User(Model):
    user_name = CharField(unique=True)  # Сделаем имя пользователя уникальным

    class Meta:
        database = db

class Film(Model):
    name = CharField(null=True, default='Название отсутствует')
    description = CharField(null=True, default='Описание отсутствует')
    rating = CharField(null=True, default='Рейтинг отсутствует')
    year = CharField(null=True, default='Год отсутствует')
    genre = CharField(null=True, default='Жанр отсутствует')
    age_rating = CharField(null=True, default='Возрастной рейтинг отсутствует')
    poster_url = BlobField()
    user = ForeignKeyField(User, backref='films')  # Связь с таблицей Users

    class Meta:
        database = db