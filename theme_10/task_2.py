def sum_two_numbers():
    try:
        num1, num2 = int(input()), int(input())
        res = num1 + num2
    except ValueError:
        return f'Ожидаемый тип данных — число'
    else:
        return res

print(sum_two_numbers())
