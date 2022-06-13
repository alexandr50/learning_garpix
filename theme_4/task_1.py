arr = [1, 2, 3, 4, 5]
result = arr[1:-1]
result.insert(0, arr[-1])
result.append(arr[0])
print(result)