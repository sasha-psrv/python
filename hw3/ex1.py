# Задача 1. Создайте список. Запишите в него N первых
# элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8 

def zadacha1():
    num = [0, 1]
    a = int(input('Введите число: '))
    for i in range(2, a):
        num.append(num[i - 2] + num[i - 1])
    print(num)    
    
zadacha1()

