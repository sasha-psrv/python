# Задача 1. Создайте пользовательский аналог метода
# filter().

def our_filter(fun, num):
    return (el for el in num if fun(el))

num = [1, 3, 67, 8, 22]

# print(list(filter(lambda x: x > 5, num)))

print(list(our_filter(lambda x: x > 5, num)))