#api.py
import requests as rq
import os

def ter(name,limit,page):
    os.getenv("token")
    token_cite = os.getenv("token_api")
    URL = 'https://api.kinopoisk.dev/v1.4/movie/search'

    name = name
    limit = limit
    page = page

    params = {
        'token': token_cite,
        'query': name,
        "limit": limit,
        "page": page,
        
        
    }
    
    response = rq.get(URL, params=params)
    data = response.json()
    page += 1  # следующая странци
    params["page"] = page
    
    return data

def ter2(limit,page):
    
    token_cite = os.getenv("token_api")
    URL = 'https://api.kinopoisk.dev/v1.4/movie'

    
    limit = limit
    page = page

    params = {
        'token': token_cite,
        "page": page,
        "limit": limit,
        'notNullFields': "name",
        "sortField": "rating.kp",
        "sortType": -1
        
    }

    response = rq.get(URL, params=params)
    data = response.json()
    page += 1  # следующая странци
    params["page"] = page
    
    return data

def get_low_budget_movie(limit,page):
    
    token_cite = os.getenv("token_api")
    URL = 'https://api.kinopoisk.dev/v1.4/movie'

    
    limit = limit
    page = page

    params = {
        'token': token_cite,
        "page": page,
        "limit": limit,
        'notNullFields': "name",
        "sortField": "budget.value",
        "sortType": 1
        
    }

    response = rq.get(URL, params=params)
    data = response.json()
    page += 1  # следующая странци
    params["page"] = page
    
    return data

def get_high_budget_movie(limit,page):
    
    token_cite = os.getenv("token_api")
    URL = 'https://api.kinopoisk.dev/v1.4/movie'

    
    limit = limit
    page = page

    params = {
        'token': token_cite,
        "page": page,
        "limit": limit,
        'notNullFields': "name",
        "sortField": "budget.value",
        "sortType": -1
        
    }

    response = rq.get(URL, params=params)
    data = response.json()
    page += 1  # следующая странци
    params["page"] = page
    
    return data