# Есть массив состоящий из слов и чисел,
# нужно записать в файл сначала слова в порядке их длины, а после слов цифры в порядке возрастания.
arr = ['love', 5, 'cat', 23, 'house', -8, 'music']
a = []
b = []
[a.append(i) if type(i) == str else b.append(i) for i in arr]
b.sort()
a.sort(key = len)
f = open('dom_zadanie.txt', 'w')
[f.write(i + '\n') for i in a]
[f.write(str(i) + '\n') for i in b]
f.close()

