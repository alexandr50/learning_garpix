count = 0

while True:

    n = input()
    if n == '':
        break
    elif int(n) % 2 == 0:
        count += 1
print(count)