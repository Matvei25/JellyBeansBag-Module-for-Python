# JellyBeansBag.py

# Добавляем новые элементы с объектами
new_element = "new element"

# Типы данных
integer_number = 10
floating_number = 3.14
string_value = "Hello, World!"
boolean_value = True

# Функции
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Набор других модулей
import math
import random

# Переменные
bag_capacity = 100
bag_color = "red"

# Классы
class JellyBean:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return f"A {self.color} jelly bean with {self.flavor} flavor"

class JellyBeansBag:
    def __init__(self):
        self.beans = []

    def add_bean(self, bean):
        self.beans.append(bean)

    def get_all_beans(self):
        return self.beans

if __name__ == "__main__":
    jelly_bean1 = JellyBean("red", "strawberry")
    jelly_bean2 = JellyBean("green", "lime")

    beans_bag = JellyBeansBag()
    beans_bag.add_bean(jelly_bean1)
    beans_bag.add_bean(jelly_bean2)

    all_beans = beans_bag.get_all_beans()
    for bean in all_beans:
        print(bean)
