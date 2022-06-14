def read_last(lines, file):
    with open(file, 'r') as f:
        res = f.readlines()
        result  = [i.strip() for i in res]
        return result[:lines:-1]
print(read_last(5, 'folder/file.txt'))
