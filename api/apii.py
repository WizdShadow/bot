#api.py

def ter(name,limit,page):
    import requests as rq
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