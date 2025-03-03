#api.py
import requests as rq
def ter(name,limit,page):
    
    token_cite = "WQCHH9E-5CW440P-Q4X9VMD-32T4C9P"
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
    
    token_cite = "WQCHH9E-5CW440P-Q4X9VMD-32T4C9P"
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