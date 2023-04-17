# Задача 3. Напишите скрипт генератора паролей
# заданной длины, состоящих из латинских букв и
# чисел.

from random import randint
lenght = int(input('введите длину пароля: '))
letters = 'abcdefghijklmnoprqrstyuvwxyz0123456789'
password = [letters[randint(0, len(letters))] for x in range(lenght)]
print(*password)