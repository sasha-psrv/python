# Задача 2. Дан список случайных чисел. Создайте список, в
# который попадают числа, описывающие возрастающую
# последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>
# [1, 2, 3] или [1, 7] или [1, 6, 7] и
# т.д.


import random

num = [random.randint(1,10) for _ in range(8)]
print(num)

result = [0]
while len(result) < 2:
    index = random.randint(0, 9) 
    result = [num[index]]
    for i in num[index:]:
        if i > result[len(result)-1]:
            result.append(i)    
        
print(result)    

