# Задача 2. Даны два случайных пятизначных числа.
# Определить, состоят ли они из одних и тех же цифр.
# 20 мин
# 72426, 27624 –> да
# 44444, 44441 -> нет

a = 44444
b = 44441
 
a_dict = dict((i, str(a).count(i)) for i  in set(str(a))) 
print(a_dict)

b_dict = dict((i, str(b).count(i)) for i  in set(str(b))) 
print(b_dict)

if a_dict == b_dict:
    print('yes')
else:
    print('no')    