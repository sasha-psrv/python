# Задача 4. Дан двумерный массив, заполненный
# нулями и единицами. Определите, есть ли в нём
# нулевые столбцы.

import numpy as np

size = (4, 4)
numbers = np.random.randint(0, 2, size)
print(numbers)

# result = np.any(numbers != 1)
result = numbers.any(axis=0)
result = ~result
print(result)
if True in result:
    print('есть')
else:
    print('нет')