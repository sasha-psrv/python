data =  open("text.txt",encoding='utf-8')
data.write('новая запись')
print(data.readlines())
data.close()

