import random

def zadacha0():
    lenght = 7
    num = [random.randint(0,10) for index in range(lenght)]
    print(num)
    sum = 0
    for index in range(lenght):
        sum += num[index]
    print(sum)
    if sum%2 == 0:
        print('yes')
    else:
        print('no')        
zadacha0()        