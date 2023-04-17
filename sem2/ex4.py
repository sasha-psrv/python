# Задача 4. Найдите все числа до 10000, у который
# количество делителей равно 10.

def zadacha4():
    count1 = 0
    for i in range(1, 10001):
        count = 0
        for d in range(1, i+1):
            if i % d == 0:
                count += 1
        if count == 10:
            count1 +=1
            print(i)   
    print(f'количество - {count1}')    
zadacha4()