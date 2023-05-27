# Задача 2. Дан массив случайных чисел. Создайте
# его с помощью NumPy. Определите его среднее
# арифметическое.
# На ввод подаётся число. Определите ближайший по
# значению к нему элемент массива.
# [1.2, 4.2, 5.6, 7.1] -> 4.525
# 6.1 -> 5.6
import numpy as np

size = 10
numbers = np.random.randint(10, 100, size)
# numbers = list(numbers)
print(numbers)
# numbers.sort()
# print(numbers)


# mean =sum(numbers)/len(numbers)
# print(f'ср ариф: {mean}')


mean =np.mean(numbers)
print(f'ср ариф: {mean}')

num = int(input('введите число: '))
dist = [np.abs(el - num) for el in numbers]
# print(dist)
min_dist = np.min(dist)
# print(min_dist)
index_min_dist = dist.index(min_dist)
print(f' ближащий элемент - {numbers[index_min_dist]}')
