# Задача 2. В зоопарк отправили отчёт о новом поступлении
# зверей с ошибкой, в результате которой некоторые данные не
# расшифровались. Расшифруйте данные. Определите, в какой
# клетке находится лев. Номер клетки совпадает с номером
# строки.
# абвгдеёжзийклмнопрстуфхцчшщъыьэюя

def ToBinary(num):
    result = ''
    while num > 0:
        result = str(num%2) + result
        num //= 2
    return '0' * (6-len(result))+ result

def decoder(code):
    animal = [code[i:i+6] for i in range(0, len(code), 6)]    


animals = ['010100001100001001010011001011000000',
           '000001011100001011',
           '001011001111010011',
           '010010010011001111010001001111000111',
           '001100000101000010',
           '001011010001001111001100001001001011',
           '001101010100001100',
           '000001000000010001010010010100001011',
           '000011000101010000000000010001000100',
           '010010001111001101',
           '010010001111000001000000001011000000',
           '011000001001000111']
alphobet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

alphobet = list(alphobet)
d= {}
for i in range(len(alphobet)):
    d[ToBinary(i)] = alphobet[i]
print(d)

result = list(map(lambda x: [d[x[i:i+6]] for i in range(0, len(x), 6)] ,animals))
result = list(map(lambda x: ''.join(x), result))
print(result)
# animals_list = [list(alphobet[int(animal[x: x+6], 2)] for x in range(0, len(animal),6)) for animal in animals]
# print(animals_list)
