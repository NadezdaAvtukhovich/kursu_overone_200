# 2 Определить функцию, которая проверяет является ли строка, введенная пользователем, целым числом.
# Решение задачи сдать ссылкой на GitHub.

#ИЛИ
#Даны две строки. Определить функцию, которая будет находить индекс второго входения второй строки в первую.
# Если подстрока ' ' вывести None. Решение сдать ссылкой на GitHub.
#Input:                                 Output:
# func('marry', 'r')            --> 3
# func('merry christmas', 's')  --> 14
# func('happy new year', ' ')   --> None

def strokali(a):
    k = a.split()
    l = 1
    for i in k:
        if not i.isdigit():
            l *= 0
    if l == 0:
        return 'Строка включает другие символы'
    else:
        return 'Строка - целое число'


print(strokali('12 34  6734'))
print(strokali('123ввс4 45'))

b = 'Mary Christmas'
c = 'r'

def vtoroe_vhogdenie(k, n):
    vx = 0
    for i in k:
        if i == n:
            vx += 1
            if vx == 2:
               return k.find(i, k.find(i)+1)
#k.find(i)+1 - начало отсчета (поиска)

print(vtoroe_vhogdenie(b, c))