
# # 1
# Роздрукувати всі парні числа менші 100 (написати два варіанти коду:
# один використовуючи цикл while, а інший з використанням циклу for).
#
# # for
# for i in range(1, 100):
#     if i % 2 == 0:
#         print(i, end=' ')
# print()
#
# # while
# i = 1
# while i < 100:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1
# print()
#
# # no loop
# print(list(range(0, 100, 2)))
#
# # 2
# Роздрукувати всі непарні числа менші 100 (написати два варіанти коду:
# один використовуючи оператор continue, а інший без цього оператора).
#
# # for
# for i in range(1, 100):
#     if i % 2 == 1:
#         print(i, end=' ')
# print()
#
# # while
# i = 1
# while i < 100:
#     if i % 2 == 1:
#         print(i, end=" ")
#     i += 1
# print()
#
# # 3
# Перевірити чи список містить непарні числа.
#           (Підказка: використати оператор break)
#
# l = [2, 4, 3, 6, 10, 17, -5, -8, -9, 0]
# for i in l:
#     if abs(i % 2) == 1:
#         break
# print("This list includes odd numbers!")
#
# # 4
# Створити список, який містить елементи цілочисельного типу, потім за допомогою
# циклу перебору змінити тип даних елементів на числа з плаваючою крапкою.
# (Підказка: використати вбудовану функцію float ()).
#
# l1 = [1, 3, 2, 6, 4, 8, -2, 5, -8]
# print(l1)
# for i in range(len(l) - 1):
#     l1[i] = float(l1[i])
# print(l1)
#
# # 5
#
# Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли.
# (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
#
# num = int(input("Input num: "))
# fib_0 = 0
# fib_1 = 1
# print(fib_0, end=' ')
# print(fib_1, end=' ')
# for i in range(num):
#     fib_sum = fib_0 + fib_1
#     fib_0 = fib_1
#     fib_1 = fib_sum
#     if fib_sum in range(num):
#         print(fib_sum, end=' ')

# n = int(input("Input an integer: "))
# fib_sequence = [0, 1]
# for i in range(2, n):
#     fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
#     if fib_sequence[i] == n:  ??? для чого ця умова ???
#         break
# print(fib_sequence)

# # recursion_function
# print(end='')
# def fibonacci(num):
#     if num < 0:
#         print("Incorrect input!")
#     elif num == 0:
#         return 0
#     elif num == 1 or num == 2:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)
#
#
# n = int(input("Input an integer: "))
# print("The", n, "number of fibonacci sequence is", fibonacci(n))

# 6
# Створити список, що складається з чотирьох елементів типу string.
# Потім, за допомогою циклу for, вивести елементи по черзі на екран.
#
# lis_t = []
# n = int(input("Input size of list: "))
# for i in range(n):
#     print("Input lis_t [", i, "]: ", end='')
#     temp = str(input())
#     lis_t.append(temp)
# for i in range(n):
#     print("lis_t [", i, "] = ", lis_t[i])

# # 7
# Змінити попередню програму так, щоб в кінці кожної букви елементів
# при виводі додавався певний символ, наприклад “#”. (Підказка: цикл for може
# бути вкладений в інший цикл, а також  треба використати функцію print(“ ”, end=”%”)).
#
# lis_t = []
# n = int(input("Input size of list: "))
# for i in range(n):
#     print("Input lis_t [", i, "]: ", end='')
#     temp = str(input())
#     lis_t.append(temp)
# for i in range(n):
#     st_r = ' '.join(lis_t)
# words = st_r.split()
# for i in words:
#     word = i
#     for char in word:
#         if char.isalpha():
#             print(char, end='#')
#         else:
#             print(char, end='')
#     print(end=" ")

# 8
# Юзер вводить число з клавіатури, написати скріпт,
# який визначає чи це число просте чи складне.
#
# import math
#
# N = int(input("Input an integer: "))
# for i in range(2, int(math.sqrt(N))):
#     if N % i == 0:
#         print("This is complex number!")
#         break
# else:
#     print("This is prime number!")

# # 9
# Знайти максимальну цифру дійсного числа. Дійсне число генеруємо випадковим чином за
# допомогою методу random() з модуля random (для цього підключаємо модуль random наступним чином:
# (from random import random)
#
# import random
# n = random.random() * 1000
# print(n)
# st_r = str(n)
# lis_t = []
# for i in range(len(st_r)):
#     if st_r[i].isdigit():
#         k = int(st_r[i])
#         lis_t.append(k)
# ma_x = lis_t[0]
# for i in range(1, len(lis_t)):
#     if ma_x < lis_t[i]:
#         ma_x = lis_t[i]
# print(ma_x)

# 10
# Визначити чи введене слово паліндром, тобто чи воно читається однаково зліва направо і навпаки.
#
# slovo = input("Please, input a word: ")
# k = 0
# for i in range(len(slovo)):
#     if slovo[i] == slovo[-(i + 1)]:
#         continue
#     else:
#         k += 1
#         break
# if k == 0:
#     print("Word {} is a palindrom".format(slovo.upper()))
# elif k == 1:
#     print("Word {} isn't a palindrom".format(slovo.upper()))
