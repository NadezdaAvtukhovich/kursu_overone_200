# Задание №1
# Найти самое длинное слово в строке.
a = str(input('Введите строку через пробел: ')).split()
print(max(a, key = len))


# Задание №2
# Преобразовать текст в список слов с удалением знаков препинания.
b = str(input('Введите строку через пробел: '))
с = ''
for i in b:
    if i != '!' and i != '.' and i != ',' and i != '?':
        с +=i
print(с.split())
