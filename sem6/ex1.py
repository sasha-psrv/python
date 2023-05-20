# Задача 1. Дан список случайных элементов.
# Проверьте, что все его элементы уникальны.
# [7, 2, 4, 1, 6] –> да
# [7, 2, 4, 2, 6] -> нет

import random

number = [random.randint(1,10) for _ in range(8)]
print(number)


numbers = list(set(number))
if len(number) == len(numbers):
    print(f'{numbers}yes')
else:
    print(f'{numbers}no')    
