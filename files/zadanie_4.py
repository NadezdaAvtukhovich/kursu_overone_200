# В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество в ней символов.
f = open('zadanie_4.txt', 'r')
s = 0
for line in f:
    k = line.replace('\n', '')
    print(f"Длина строки {k} равна {len(k)}")
    s += 1
print(f'Количество строк в файле равно: {s}')
f.close()