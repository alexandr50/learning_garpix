def get_max_lenght(file):

    with open(file, 'r') as f:
        res = f.read().strip()
        res = [i for i in res.split()]
        result = sorted(res, key=len)
        max_len = len(result[-1])
        arr = []
        for i in result:
            if len(i) == max_len:
                arr.append(i)
        return arr if len(arr) > 1 else arr[0]
print(get_max_lenght('folder/file.txt'))