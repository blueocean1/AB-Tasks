# 1
# Спробуйте переписати наступний код через map. Він приймає список реальних імен і замінює їх хеш-прізвищами,
# використовуючи  більш надійний метод-хешування.

# names = ['Sam', 'Don', 'Daniel']
# for i in range(len(names)):
#     names[i] = hash(names[i])
# print(names)
#
# names = ['Sam', 'Don', 'Daniel']
# hash_names = map(hash, names)
# print(list(hash_names))

# 2
# Вивести список кольору “red”, який найчастіше зустрічається в даному списку  [“red”, “green”, “black”, “red”, “brown”,
# “red”, “blue”, “red”, “red”, “yellow” ] використовуючи функцію filter.

# colours = ['red', 'green', 'black', 'red', 'brown','red', 'blue', 'red', 'red', 'yellow']
# red_colours = filter(lambda x: x == "red", colours)
# print(list(red_colours))

# 3
# Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список
# в список, всі числа якого мають тип даних integer:
# 1)  використовуючи метод  append
# 2)  використовуючи метод  map

# lis_t = ['1', '2', '3', '4', '5', '7']
#
# # 3.1
# int_list = []
# for i in lis_t:
#     int_list.append(int(i))
# print(int_list)
#
# # 3.2
# integer_list = map(lambda x: int(x), lis_t)
# print(list(integer_list))

# 4
# Перетворити список, який містить милі, в список, який містить кілометри (1 миля=1.6 кілометра)
#    a) використовуючи функцію map
#    b) використовуючи функцію map та lambda
# Знайти найбільший елемент в списку  використовуючи функцію reduce

from functools import reduce

miles = [1.3, 5, 2.82, 3.57, 1.27]
kilometers = list(map(lambda x: x * 1.6, miles))
print(kilometers)
max_element = reduce(max, kilometers)
min_element = reduce(min, kilometers)
print("Max distance is {} miles".format(max_element))
print("Min distance is {} miles".format(min_element))

# 6
# Перепишіть наступний код, використовуючи map, reduce і filter. Filter приймає функцію і колекцію. Повертає колекцію
# тих елементів, для яких функція повертає True.
# people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}]
# height_total = 0
# height_count = 0
# for person in people:
#     if 'height' in person:
#         height_total += person['height']
#         height_count += 1
# print(height_total)


