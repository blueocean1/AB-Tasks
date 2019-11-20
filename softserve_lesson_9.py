# 1
#  Створити клас машина з атрибутами name,  make, model та методами start та stop, які виводять
#  інформацію про те що автомобіль стартував чи зупинився відповідно.


# class Car:
#     def __init__(self, name, make, model):
#         self.name = name
#         self.make = make
#         self.model = model
#
#     def start(self):
#         if self.make == 'start':
#             print("{} {} is driving!".format(self.name, self.model))
#
#     def stop(self):
#         if self.make == 'stop':
#             print("{} {} doesn't go!".format(self.name, self.model))
#
#
# car_1 = Car('Tesla', 'start', 'Model 3')
# car_2 = Car('Mercedes', 'stop', 'Benz')
# car_1.start()
# car_2.stop()


# 2
# Створити клас особа,  в якому конструктор встановлює ім’я, а метод info виводить повідомлення “Hello, my name is
# {ім’я конкретного екземпляра класу}”, а також створити клас автомобіль,  в якому конструктор встановлює ім’я,
# а метод move виводить повідомлення {ім’я конкретного екземпляра класу}  moves at the speed {speed(цей параметр
# метод moveотримує як вхідний)} km / h

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         print("Hello, my name is {}".format(self.name))
#
#
# class Car:
#     def __init__(self, name):
#         self.name = name
#
#     def move(self, speed):
#         print("{} moves at the speed {} km/h.".format(self.name, speed))
#
#
# person_1 = Person("Andriy")
# person_1.info()
# car_1 = Car("Tesla Roadster")
# car_1.move(250)


# 3
# Створити клас особа,  в якому конструктор встановлює ім’я, вік. Використати в цьому класі геттери та сеттери, а також
# створити метод info, який виводить інформацію про ім’я та вік особи. А тоді створити клас працівник, який наслідується
# від класу особи і містить метод details, який на вхід отримує параметр про компанію, в якій працює працівник і цей
# метод виводить інформацію про те, що працівник з таким то іменем працює в такій то компанії.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def get_name(self):
#         return self.name
#
#     @property
#     def get_age(self):
#         return self.age
#
#     @get_name.setter
#     def set_name(self, name):
#         self.name = name
#
#     @get_age.setter
#     def set_name(self, age):
#         self.age = age
#
#
# class Worker(Person):
#     def __init__(self, name, age):
#         # Person.__init__(self, name, age)
#         super(Worker, self).__init__(name, age)
#
#     def details(self, company_name):
#         print("{} works in {}".format(self.name, company_name))
#
#
# worker_1 = Worker("Andriy", 21)
# worker_1.details('Tesla')


# 4
#  Створити батьківський клас Figure з методами init: ініціалізується колір, get_color: повертає колір фігури,
#  info: надає інформацію про фігуру та колір, від якого наслідуються такі класи як Rectangle, Square, які мають
#  інформацію про ширину, висоту фігури, метод square, який знаходить площу фігури.

# ??? приватні поля, getter, setter, нема доступу в похідному класі ???

# class Figure:
#     def __init__(self, height, width, colour):
#         self.height = height
#         self.width = width
#         self.colour = colour
#
#     # @property
#     # def colour(self):
#     #     return self.colour
#     #
#     # @colour.setter
#     # def colour(self, colour):
#     #     self.colour = colour
#
#     def info(self):
#         return "Height: {} \t Width: {} \t Colour: {}".format(self.height, self.width, self.colour)
#
#
# class Rectangle(Figure):
#     def __init__(self, height, width, colour):
#         super(Rectangle, self).__init__(height, width, colour)
#
#     def Square(self):
#         return 2 * self.height * self.width
#
#     def info(self):
#         print(Figure.info(self), end="\t")
#         return "Square: {}".format(Rectangle.Square(self))
#
#
# figure_1 = Figure(10, 25, 'Green')
# print(figure_1.info())
# figure_2 = Rectangle(5, 6, 'White')
# print(figure_2.info())
