# Задача 3. Создайте двумерный массив случайного размера. Найдите индексы
# максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy as np

size = np.random.randint(2,5, size=2)
array = np.random.randint(1,100, size=(size[0],size[1]))
print(array)


max_index = np.unravel_index(np.argmax(array), array.shape)
min_index = np.unravel_index(np.argmin(array), array.shape)

print(f"Индексы максимального элемента: {max_index}")
print(f"Индексы минимального элемента: {min_index}")

print(f"Элементы главной диагонали: {np.diag(array)}")