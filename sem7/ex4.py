# Задача 4. Создайте декоратор с параметрами.

def greetings(hello):
    def our_greetings(fun):
        def decorator():
            name = fun()
            print(f'{hello}, {name}')
        return decorator
    return our_greetings    

@greetings('привет')
def get_name():
    return input('как тебя зовут?\n')

get_name()