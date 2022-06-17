import requests

def get_response(url, *args):
    count = 0
    for i in url:
        if i == '@':
            url = url.replace(i, args[count], 1)
            count += 1

    return requests.get(url)

print(get_response('https://www.ozon.ru/search/?from_global=@&sorting=@&text=@', 'true', 'price', 'd3'))
