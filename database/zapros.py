from peewee import SqliteDatabase, Model, CharField, IntegerField
from .models import User, Film, db
    
def info_check(id_user):

    db.connect()
    db.create_tables([User])

    user = User.select(User.id).where(User.user_name == id_user).first()
    
    if user:
        spisoc_film  = []
        spisoc_film_db = []
        films = Film.select(Film.name).where(Film.user_id == user)
        for v, i in enumerate(films):
            spisoc_film.append(f"{v + 1}) {i.name}")
            spisoc_film_db.append(i.name)
        
        history_film = "\n".join(spisoc_film)
        db.close()
        return history_film, spisoc_film, spisoc_film_db
       
def info_check2(id_user,name_film):   
    db.connect()
    db.create_tables([User])

    user = User.select(User.id).where(User.user_name == id_user).first()
    
        
    films = Film.select(Film.name, Film.description, Film.rating, Film.year, Film.genre, Film.age_rating, Film.poster_url).where(Film.user_id == user, Film.name == name_film).get()    

    text = (
        f"Название:{films.name}\n"
        f"Описание: {films.description}\n"
        f"Рейтинг: {films.rating}\n"
        f"Год: {films.year}\n"
        f"Жанры: {films.genre}\n"
        f"Возрастной рейтинг: {films.age_rating}\n"
    )
    
    # text = f"""Название: {films[0].name}\n
    #         Описание: {films[0].description}\n
    #         Рейтинг: {films[0].rating}\n
    #         Год: {films[0].year}\n
    #         Жанр: {films[0].genre}\n
    #         Возрастной рейтинг: {films[0].age_rating}\n"""
    photo = films.poster_url
    db.close()
    return text, photo
        
        
        

    
        
        


   
    
