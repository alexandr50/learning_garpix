temp_in_room = int(input('Введите текущую температуру в комнате: '))
desired_temp = int(input('Введите желаемую температуру в комнате: '))
desired_humidity = int(input('Введите желаемую влажность в комнате: '))

if desired_temp < temp_in_room and desired_humidity <= 80:
    print('on')
else:
    print('off')