# Задача 3. Создайте декоратор для метода нахождения суммы.

def our_format(fun):
    def decorator(*args):
        # print(f'{a} + {b} = ', end='' )
        for arg in args:
            print(f'{arg} + ', end='')
        print('\b\b= ', end='')
        fun(*args)
    return decorator    

@our_format
def sum(a,b):
    print(a + b)

@our_format
def sum_4(a,b,c,d):
    print(a + b + c + d)


sum(3,5)
sum_4(1,3,2,7)