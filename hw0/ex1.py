# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

n = int(input("Введите число: "))
if n == 1:
    print("Понедельник")
if n == 2:
    print("Вторник")
if n == 3:
    print("Среда")
if n == 4:
    print("Четверг")
if n == 5:
    print("Пятница")
if n == 6:
    print("Суббота")
if n == 7:
    print("Воскресенье")
if n > 7 or n == 0:
    print("Нет такого дня")
