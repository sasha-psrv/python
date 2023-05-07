# Задача 0. С помощью анонимной функции найдите в
# списке на 15 элементов числа, кратные 5. Заполните
# список случайным образом числами от 1 до 100.

def zadacha0():

    import random

    num = [random.randint(1,101) for _ in range(15)]
    print(num)
    num = filter(lambda num: not (num % 5), num)
    num = list(num)
    print(num)

zadacha0()    


