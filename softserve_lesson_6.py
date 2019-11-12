import math

 # 1
# Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.

# def ser_aryf(*args):
#     return sum(args) / len(args)
#
#
# mass = [1, 2, 3, 4, 5]
# print(ser_aryf(*mass))

# 2
# Написати функцію, яка повертає абсолютне значення числа

# def modul(n):
#     return abs(n)
#
#
# print(modul(-5))

# 3
# Написати функцію, яка знаходить максимальне число з двох чисел,
# а також в функції використати рядки документації DocStrings.

# def ma_x(a, b):
#     """Функція повертає максимум двох чисел"""
#     return max(a, b)
#
#
# print(ma_x(3, -6))
# print(ma_x.__doc__)

# 4
# Написати програму, яка обчислює площу прямокутника, трикутника та кола
# (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)

# def circle_square():
#     print("You want to count circle_square")
#     radius = float(input("Input circle radius: "))
#     print("circle_square =", math.pi * radius * radius )
#     return math.pi * radius * radius
#
#
# def triangular_square():
#     print("You want to count triangular_square")
#     h = float(input("Input h: "))
#     a = float(input("Input a: "))
#     print("triangle_square =", 0.5 * a * h)
#     return 0.5 * a * h
#
#
# def rectangle_square():
#     print("You want to count rectangle_square")
#     a = float(input("Input a: "))
#     b = float(input("Input b: "))
#     print("rectangle_square =", a * b)
#     return a * b
#
#
# def square_counter(n):
#     if n == 1:
#         circle_square()
#     elif n == 2:
#         triangular_square()
#     elif n == 3:
#         rectangle_square()
#
#
# print("1 - circle_square \n2 - triangular_square \n3 - rectangle_square")
# key = int(input("Your choice: "))
# square_counter(key)

# 5
# Написати функцію, яка обчислює суму цифр введеного числа.

# def numbers_multiplication():
#     N = input("Input an integer: ")
#     lis_t = []
#     d = 1
#     for i in N:
#         lis_t.append(int(i))
#         d *= int(i)
#     print(lis_t)
#     return d
#
#
# print(numbers_multiplication())

# 6 (!!!недороблена!!!)
# Написати програму калькулятор, яка складається з наступних функцій:
# головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, калькулятор працює доти,
# поки ми не виберемо дію вийти з калькулятора, після виходу, користувач отримує повідомлення з подякою за
# вибір нашого програмного продукту!!!

# def add():
#     x = float(input("Input x: "))
#     y = float(input("Input y: "))
#     print("x + y =", x + y)
#     return x + y
#
#
# def calculator(unit):
#     while 1 > 0:
#         if unit == 1:
#             add()
#         if unit == 0:
#             print("Thank you for using our product!")
#             break
#
#
# print("1 - add \n2 - multiplication \n3 - division \n0 - quit")
# key = int(input("Your choice: "))
# calculator(key)

# 7
# Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем.

# def fibonacci(N):
#     if N < 0:
#         return "Incorrect input! Integer should be >= 0!"
#     elif N == 0:
#         return 0
#     elif N == 1 or N == 2:
#         return 1
#     else:
#         return fibonacci(N - 1) + fibonacci(N - 2)
