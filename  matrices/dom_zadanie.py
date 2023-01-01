# Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.


import random
M = 5
N = 5
A = [ [0]*M for i in range(N) ]
sum = 0
max = 0
for i in range(M):
    for j in range(N):
        A[i][j] = random.randint(0, 10)
        print(A[i][j], end=' ')
        sum += A[i][j]
    print()
    if sum > max:
        max = sum
        indexmax = i
    sum = 0
print(f'В строке {indexmax+1} максимальная сумма элементов')


# Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое на второе.
# Обработать ошибку деления на ноль. Если второе число 0, то программа запрашивает ввод чисел заново.
# Также если были введены буквы, то обработать исключение.
a = input()
b = input()
try:
    a1 = int(a)
    b1 = int(b)
    print('Были введены числа и их частное равно: ',a1/b1)
except ValueError:
    print('Введены были строки, а не числа, деление невозможно!')
except ZeroDivisionError:
    a = int(input('Введите число заново: '))
    b = int(input('Введите число заново: '))
    print(a/b)