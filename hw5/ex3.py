# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в
# списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента
# совпадают
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]


import random

number = [random.randint(1,10) for _ in range(8)]
print(number)

lenght = len(number)-len(set(number))
numbers = list(set(number))
print(numbers)
print(f" {lenght} элемента")


