password = '12345qwert'
while True:
    n = input('Введите пароль: ')
    if n != password and n != 'q':
        continue
    else:
        break