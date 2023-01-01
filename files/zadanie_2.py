# Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так,
# чтобы сначала шли числа по возрастанию, а потом слова по возрастанию их длины.
f = open('zadanie_2.txt', 'r')
a = []
b = []
for line in f:
    try:
        a.append(int(line))
    except ValueError:
        b.append(line.replace('\n', ''))
a.sort()
b.sort(key = len)
print(a + b)
f.close()

