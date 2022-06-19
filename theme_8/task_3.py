import requests

def get_count_repo(arr):
    response = requests.get('https://github.com/search?q=repositories+language%3AC%23&type=Repositories&ref=advsearch&l=C%23&l=')
    lst1 = [[0] for i in range(len(arr))]
    lst = list(map(list, zip(arr, lst1)))
    r = response.text
    arr = r.split()
    start, end, start2, end2 = 0, 0, 0, 0
    for i, j in enumerate(arr):
        if j == 'Languages':
            start = i
        elif j == 'C++':
            end = i + 1
        elif j == 'results' and arr[i-1] == 'repository':
            lst[-1][1] = arr[i-2]
    result = arr[start:end]


    for d, i in enumerate(lst):
        for j, k in enumerate(result):
            if k.lower() == i[0]:
                data = result[j-1]
                for x, y in enumerate(data):
                    if y == '>':
                        start2 = x+1
                    elif y == '<':
                        end2 = x
                        b = data[start2:end2]
                        lst[d][1] = b

    return lst
print(get_count_repo(['python', 'c++', 'java', 'javascript', 'ruby', 'c#']))




















