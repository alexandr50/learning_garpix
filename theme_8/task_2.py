import requests
def get_response(url, params):

    res = requests.get(url, params=params)
    return res.url

print(get_response('https://market.yandex.ru/search', {'from_global': 'true', 'sorting': 'price', 'text': 'd3*'}))

