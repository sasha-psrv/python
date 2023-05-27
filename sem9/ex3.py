# Задача 3. Задайте квадратную матрицу, состоящую
# из случайных чисел. Найдите самый часто
# встречающийся элемент в этой матрице.

import numpy as np

size = (4,4)
numbers = np.random.randint(1,10, size)
print(numbers)

# numbers = list(numbers)
# dictionary = {}
# for i in numbers:
#     dictionary[i] = numbers.count(i)
# print(dictionary)

uniq_list, uniq_count = np.unique(numbers, return_counts=True)
print(uniq_list)
print(uniq_count)
index_max = np.argmax(uniq_count)
print(index_max)
print(f' элемент {uniq_list[index_max]} встречется - {uniq_count[index_max]} раза')