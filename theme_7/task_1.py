
with open('folder/file.txt', 'r', encoding='utf-8') as f:
    res = f.readlines()
    result = [i.strip() for i in res]
    print(*result[:6], sep='\n')
