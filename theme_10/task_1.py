class MyError(Exception):
    def __init__(self, text):
        self.text = text

def check_name(name):
    arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    try:
        for i in name:
            if i in arr:
                raise MyError('Имя не может содержать цифры')
    except MyError as e:
        return e
    else:
        return name
print(check_name(input()))