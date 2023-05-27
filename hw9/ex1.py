# Задача 1. Дан список элементов. Используя библиотеку NumPy, подсчитайте количество
# уникальных элементов в нём.

import numpy as np

size = 10
numbers = np.random.randint(1, 10, size)
print(numbers)


uniq_list = np.unique(numbers)
print(f'Уникальные элементы: {uniq_list}')
print(f'Количество уникальных элементов: {len(uniq_list)}')
