from peewee import SqliteDatabase, Model, CharField, IntegerField
from .models import User, Film, db
    
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
    
        
    films = Film.select(Film.name, Film.description, Film.rating, Film.year, Film.genre, Film.age_rating, Film.poster_url).where(Film.user_id == user, Film.name == name_film)    

    
    
    text = f"""Название: {films[0].name}
            Описание: {films[0].description}
            Рейтинг: {films[0].rating}
            Год: {films[0].year}
            Жанр: {films[0].genre}
            Возрастной рейтинг: {films[0].age_rating}"""
    photo = films[0].poster_url
    db.close()
    return text, photo
        
        
        

    
        
        


   
    
