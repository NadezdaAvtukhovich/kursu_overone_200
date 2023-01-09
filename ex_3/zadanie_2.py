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
    if a.isdigit():
        return 'Строка - целое число'
    else:
        return 'Строка включает другие символы'

print(strokali('1234'))
print(strokali('123ввс4'))

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