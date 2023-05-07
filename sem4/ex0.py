# Задача 0. Создайте кортеж. Запишите в него 10
# случайных чисел.

import random
num = tuple(random.randint(1,10) for _ in range(6))
print(num)
print(type(num))
