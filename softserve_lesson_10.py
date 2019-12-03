# 1
# Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне,
# чи введені дані коректні.

# while 1:
#     try:
#         n = int(input("Please, input an integer: "))
#         if n % 2 == 0:
#             print("This is even number!")
#         elif n % 2 == 1:
#             print("This is odd number!")
#     except ValueError:
#         print("It's not an integer!")


# 2
#  Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення про те чи вік є парним
#  чи непарним числом. Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати власну
#  виняткову ситуацію. Головний код має викликати функцію, яка обробляє введену інформацію.

# class NegativeAge(Exception):
#     def __init__(self, data):
#         self.data = data
#
#     def __str__(self):
#         return repr(self.data)
#
#
# def IsAgeNegative():
#     try:
#         n = int(input("Input your age: "))
#         if n < 1:
#             raise NegativeAge("Your age cannot be negative or equal to zero!")
#         if n % 2 == 0:
#             print("Your age is even number!")
#         elif n % 2 == 1:
#             print("Your age is odd number!")
#     except NegativeAge as e:
#         print(e.data)
#
#
# IsAgeNegative()


# 3
# Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, передбачити
# випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій. Використати блоки else та
# finally.

# TypeError - 3 + 'd', ValueError - неправильні значення

# try:
#     x, y = int(input("Input x: ")), int(input("Input y:"))
#     result = x / y
# except ZeroDivisionError:
#     print("Division by zero!")
# except ValueError:
#     print("Value Error!")
# finally:
#     print("End of the program!")


# 4
# Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, який відповідає цьому
# числу (1 це Понеділок, 2 це Вівторок і т.д.) . Врахувати випадки введення чисел від 8 і більше, а також випадки
# введення не числових даних.

# class OutOfDayIndex(Exception):
#     def __init__(self, data):
#         self.data = data
#
#     def __str__(self):
#         return self.data
#
#
# class NotNegativeDays(Exception):
#     def __init__(self, data):
#         self.data = data
#
#     def __str__(self):
#         return repr(self.data)
#
#
# try:
#     n = int(input("Input an integer between 1 and 7: "))
#     days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     if n in range(1, 8):
#         print("Today is {}".format(days_of_week[n - 1]))
#     if n > 7:
#         raise OutOfDayIndex("There are only seven days!")
#     if n < 1:
#         raise NotNegativeDays("Day index cannot be negative or equal to zero!")
#
# except OutOfDayIndex as e:
#     print(e.data)
# except NotNegativeDays as e:
#     print(e.data)
# except ValueError:
#     print("Value Error")
# finally:
#     print("End of the program.")
