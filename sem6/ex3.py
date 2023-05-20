# Задача 3. Напишите программу вычисления арифметического
# выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.
# а) Решите задачу для одного действия;
# б) Дополнительное задание. Решите задачу для нескольких
# действий;
# в) Решите задачу средствами python.
# 25 мин
# 2+2 => 4
# 1+2*3 => 7

def task_a():
    expresstion = input()

    if '+' in expresstion:
        expresstion = expresstion.split('+')
        print(int(expresstion[0]) + int(expresstion[1]))
    if '-' in expresstion:
        expresstion = expresstion.split('-')
        print(int(expresstion[0]) - int(expresstion[1]))
    if '*' in expresstion:
        expresstion = expresstion.split('*')
        print(int(expresstion[0]) * int(expresstion[1]))
    if '/' in expresstion:
        expresstion = expresstion.split('/')
        print(int(expresstion[0]) / int(expresstion[1]))

def task_b():
    expression = input()
    

  