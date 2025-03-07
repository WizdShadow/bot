import requests as rq

def down_im(url):
    response = rq.get(url)
    return response.content
