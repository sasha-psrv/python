# Задача 1. Задайте список случайных чисел от 1 до 10,
# выведите все элементы больше 5. Используйте для решения
# лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8


import random

num = [random.randint(1,10) for _ in range(6)]
print(num)
num = filter(lambda num: num > 5, num)
num = list(num)
print(num)