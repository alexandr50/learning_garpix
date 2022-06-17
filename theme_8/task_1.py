import requests
def get_response(url):
    res = requests.get(url)
    return res, url

print(get_response('https://study.garpix.com'))
