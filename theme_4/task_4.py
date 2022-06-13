list1 = [1, 2, 3, 4, 5, 1, 3]

for i in list1:
    if list1.count(i) > 1:
        list1.remove(i)
print(list1)

# можно так
list2 = set(list1)
print(list2)