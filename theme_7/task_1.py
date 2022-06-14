
with open('folder/file.txt', 'r', encoding='utf-8') as file:
    res = file.readlines()
    result = [i.strip() for i in res]
    print(*result[:6], sep='\n')
