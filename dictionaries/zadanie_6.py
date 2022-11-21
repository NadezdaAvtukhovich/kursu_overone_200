# A = dict(zip('abc', range(3)))
# for k, v in A.items():
#     print(k, v)

# Создайте словарь из строки 'pythonist' следующим образом:
# в качестве ключей возьмите буквы строки,
# а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
a = 'pythonist'
b = []
c = []
for i in a:
    #print(a.count(i))
    c.append(i)
    b.append(a.count(i))
print(dict(zip(c, b)))

