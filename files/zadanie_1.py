f = open('example.txt', 'r') #открыть файл в режиме чтения
#print(f.read(7))
print(f.readline(2)) # если указать число, то прочитает конкретный символ строки!
#print(f.readline())
#f.seek(0)
#print(f.read())
#f.write('Hello \nWorld')
#print(*f) # выводим содержимое файла
#print(f) # выводим объект
f.close()