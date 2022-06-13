list1 = [5, 10, 15, 20, 25, 20, 50]

for i in range(len(list1)):
    if list1[i] == 20:
        list1.pop(i)
        list1.insert(i, 200)
print(list1)