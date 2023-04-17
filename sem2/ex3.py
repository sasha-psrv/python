# Задача 3. Дано число N. Заполните список длиной N
# элементами 1, -3, 9, -27, 81, -243...
# N = 5 -> [1, -3, 9, -27, 81]

def zadacha3():
    n = int(input("введите число: "))
    num = []
    for el in range(n):
        # print(f'{el} -> {(-3)**el}')
        num.append((-3)**el)
    print(num)    

zadacha3()
