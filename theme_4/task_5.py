lst1 = ['Санкт-Петербург', 'Москва', 'Казань']
lst2= ['Воронеж', 'Санкт-Петербург', 'Иваново']
# список городов которые есть в обоих списках
result1 = []
for i in lst1:
    if i in lst2:
        result1.append(i)
print(result1)
# список с городами которые есть в одном из списков
result2 = lst1 + lst2
for i in result2:
    if result2.count(i) > 1:
        result2.remove(i)
print(result2)