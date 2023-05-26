# Задача 1. Создайте пользовательский аналог метода map()


from random import randint

def create_iterable(length):
    return [randint(1,100) for _ in range(length)]

def custom_map(func, iterable):
    return [ func(x) for x in iterable]

print(custom_map(lambda x: x*5, create_iterable(10)))
