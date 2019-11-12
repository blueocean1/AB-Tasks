# 1
# Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

# lis_t = [int(input("Input lis_t[{}] element:".format(i + 1)) for x in range(int(input("Input size of list: ")))]
# print(lis_t)
# print("max =", max(lis_t))
# print("min =", min(lis_t))

# n = int(input("Input size of list: "))
# lis_t = []
# for i in range(n):
#     print("Input lis_t [", i, "]: ", end="")
#     k = int(input())
#     lis_t.append(k)
# print(lis_t)

# 2
# В інтервалі від 1 до 10 визначити числа
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3,
# •  числа, які не діляться на 2 та 3.

# even = [x for x in range(1, 11) if x % 2 == 0]
# odd = [x for x in range(1, 11) if x % 2 == 1 and x % 3 == 0]
# not_2_3 = [x for x in range(1, 11) if x % 2 != 0 and x % 3 != 0]
# print(even)
# print(odd)
# print(not_2_3)

# 3
# Написати програму, яка обчислює факторіал числа, яке користувач вводить.
# (не використовувати рекурсивного виклику функції)

# N = int(input("Input N: "))
# factorial = 1
# for i in range(1, N):
#     factorial *= i
# print("{}! = ".format(N), factorial)

# 4
#  Напишіть скрипт, який перевіряє логін, який вводить користувач.
# Якщо логін вірний (First), то привітайте користувача.
# Якщо ні, то виведіть повідомлення про помилку.
# (використайте цикл while)

# login = "First"
# while 1 > 0:
#     user_input = input("Input you login: ")
#     if user_input == login:
#         print("You are logged on!")
#         break
#     else:
#         continue

# 5
# Перший випадок.
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число.
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

# while 1 > 0:
#     k = int(input("Input an integer: "))
#     if k <= 0:
#         print("Stop program. Integer is <= 0!")
#         break
#     else:
#         continue

# 6
# Другий випадок.
# На початку на вхід подається кількість елементів послідовності, а потім самі елементи.
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

# num = int(input("Input quantity of elements: "))
# i = 0
# while i <= num:
#     k = int(input("Input an integer: "))
#     if k <= 0:
#         print("Integer is <= 0. Stop program!")
#         break
#     else:
#         continue
