# Задача 1. Выведите таблицу истинности для
# выражения ¬ X ∨ Y.

def zadacha2():
    for x in range(0, 2):
        for y in range(0, 2):
            print(f'{x} | {y} | {int(not x or y) }')
       
zadacha2()