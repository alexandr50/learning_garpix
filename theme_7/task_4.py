def calc_count_word(file, word):
    with open(file, 'r') as f:
        res = f.read().strip()
        res = [i for i in res.split()]
        count = 0
        for i in res:
            if word == i:
                count += 1
    return count

print(calc_count_word('folder/file.txt', 'here'))