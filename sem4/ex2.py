# Задача 2:
# На вход подаются два числа. Напишите метод, который вернёт
# сумму, разность, произведение и частное этих чисел.

def calculate(a, b):
    return a+b, a-b, a*b, a/b


a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
sum, razn, umn, delen = calculate(a, b)
print(sum,razn,umn,delen)
