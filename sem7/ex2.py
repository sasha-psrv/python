# Задача 2. Создайте метод, позволяющий замерить время работы
# других методов.

import time

def stopwatch(fun):
    def decoraton():
        start_time = time.time()
        fun()
        print(f'время выполнения: {time.time()- start_time}')
    return decoraton

@stopwatch
def our_math():
    
    num = '132'
    result = int(num) + int(num*2) + int(num*3)
    print(result)
    
@stopwatch
def our_math_int():
        
        num = 132
        result = num + num*100 + num*10000 + num*1000 + num
        print(result)
        

our_math()
our_math_int()       
# stop = stopwatch(our_math)
# stop()