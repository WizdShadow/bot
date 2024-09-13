from peewee import SqliteDatabase, Model, CharField, IntegerField

# Подключение к базе данных SQLite
db = SqliteDatabase('my_database.db')

# Базовая модель
class BaseModel(Model):
    class Meta:
        database = db

# Модель User
class User(BaseModel):
    user_name = CharField()
    id = IntegerField(primary_key=True)  
    
class Film(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    description = CharField()
    rating = CharField()
    year = CharField()
    genre = CharField()
    age_rating = CharField()
    user_id = CharField()
    
def info_check(id_user):

    db.connect()
    db.create_tables([User])

    user = User.select(User.id).where(User.user_name == id_user).first()
    
    if user:
        spisoc_film  = []
        films = Film.select(Film.name).where(Film.user_id == user)
        for i in films:
            spisoc_film.append(i.name)
        
        history_film = "\n".join(spisoc_film)
        db.close()
        return history_film ,spisoc_film
       
def info_check2(id_user,name_film):   
    db.connect()
    db.create_tables([User])

    user = User.select(User.id).where(User.user_name == id_user).first()
    
        
    films = Film.select(Film.name, Film.description, Film.rating, Film.year, Film.genre, Film.age_rating).where(Film.user_id == user, Film.name == name_film)    

    
    
    text = f"""Название: {films[0].name}
            Описание: {films[0].description}
            Рейтинг: {films[0].rating}
            Год: {films[0].year}
            Жанр: {films[0].genre}
            Возрастной рейтинг: {films[0].age_rating}"""
    db.close()
    return text
        
        
        

    
        
        


   
    
