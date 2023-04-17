# Задача 2. Напишите программу, в которой
# пользователь будет задавать две строки, а программа
# - определять количество вхождений одной строки в
# другую.
# «qwe» «qwertyqwe» -> 2
def zadacha2():
    a = str(input('первую строку: '))
    b = str(input('вторую строку: '))
    lenght_a = len(a)
    lenght = len(b)
    count = 0
    for i in range(lenght):
        if b[i:i+lenght_a] == a:
            count +=1
    print(f' в фразе {b} \подстрока {a} встречается {count} раз')        
zadacha2()  