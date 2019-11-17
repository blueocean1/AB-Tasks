# import pyowm
#
# owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key
#
# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
#
# # Search for current weather in London (Great Britain)
# city = input("In which city would you like to know the weather? ")
# observation = owm.weather_at_place(city)
# w = observation.get_weather()
# print(w)  # <Weather - reference time=2013-12-18 09:20,
# # status=Clouds>
#
# # Weather details
# w.get_wind()  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()  # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#
# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)
#
# wind = w.get_wind()
# humidity = w.get_humidity()
# temperature = w.get_temperature('celsius')
# print("\nIn {} middle temperature is {}, humidity: {} units, speed of wind is {} m/s. Good luck!".format(city,
#                    temperature['temp'], humidity,  wind['speed']))


# 1
# Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 і пропонує користувачу
# вгадати це число. Програма зчитує числа, які вводить користувач і видає користувачу підказки про те чи загадане
# число більше чи менше за введене користувачем. Гра має тривати до моменту поки користувач не введе число, яке
# загадане програмою, тоді друкує повідомлення привітання. (для виконання завдання необхідно імпортувати  модуль
# random, а з нього функцію randint())

# from random import randint
# random_num = randint(1, 100)
# print(random_num)
# print("Try to guess randomly generated integer in range(1, 100).\nYour choice: ")
# while 1:
#     input_num = int(input())
#     if input_num == random_num:
#         print("You are awesome guy!")
#         break
#     else:
#         if input_num > random_num:
#             print("Integer should be smaller. Try one more time: ")
#         elif input_num < random_num:
#             print("Integer should be greater. Try one more time: ")
#         continue

# 2
# Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2.
# (для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).

# from math import pow, pi
#
#
# def circle_square():
#     print("You want to count circle_square")
#     radius = float(input("Input circle radius: "))
#     print("circle_square =", pi * pow(radius, 2))
#     return pi * radius * radius
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


# def fibo(n):
#     a, b = 0, 1
#     while b < n:
#         print(b, end=" ")
#         a, b = b, b + a
#     print()
#
# fibo(25)
#
# def fibo_seq(n):
#     f_sequence = []
#     a, b = 0, 1
#     while b < n:
#         f_sequence.append(b)
#         a, b = b, b + a
#     return f_sequence
#
#
# lis_t = fibo_seq(25)
# print(lis_t)