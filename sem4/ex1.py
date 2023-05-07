# Задача 1:
# Создайте кортеж, заполненный случайными числами.
# Напишите метод, который заменяет элемент в
# кортеже по заданному индексу другим случайным
# числом.

import random


def change_element(num, index):
    return num[:index] + (random.randint(1, 100), ) + num[index+1:]


num = tuple(random.randint(1, 100) for _ in range(10))
index = 2

print(num)
num_new = change_element(num, index)
print(num_new)
