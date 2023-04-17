# Задача 1. В списке хранятся сведения о количестве
# осадков, выпавших за каждый день июня.
# Определите в какой период выпало больше осадков:
# в первой или второй половине июня.
# Примечание: список заполняется
# случайными числами от 0 до 25.

import random


def zadacha1():
    lenght = 30
    i = [random.randint(0, 25) for _ in range(lenght)]
    print(i)
    print(i[:15])
    print(i[15:])
    if sum(i[:15])>sum(i[15:]):
        print(f'{sum(i[:15])} {sum(i[15:])} в первой половине')
    else:
        print(f'{sum(i[15:])} {sum(i[:15])} во второй половине')
    # sum1 = 0
    # sum2 = 0
    # for i in range(15):
    #     sum1 += num[i]
    # for j in range(15, len(num)):
    #     sum2 += num[i]  
    # if sum1 > sum2:
    #     print('в первой')
    # else:
    #     print('во второй')        


zadacha1()
