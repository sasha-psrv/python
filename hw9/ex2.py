# Задача 2. Создайте двумерный массив, размером 5х5. Определите, есть ли в нём
# одинаковые строки.

import numpy as np

size = (5, 5)
numbers = np.random.randint(1, 10, size)
print(numbers)

unique_rows = np.unique(numbers, axis=0)
unique_rows_len=unique_rows.shape[0]
matrix_len=numbers.shape[0]
if unique_rows_len == matrix_len:
    print("Нет одинаковых строк")
else:
    print("Есть одинаковые строки")
