# m = 3
# n = 2
# a =[]
# for i in range(m):
#     a.append([1]*n)
# print(a)
# a = [[1, 2, 3, 4], [5,6], [7,8,9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end = ' ')
#     print()

# Создать матрицу M x N, где M и N вводятся с клавиатуры.
# Элементы матрицы заполнить случайными числами. Сделать читабельный вывод матрицы.
import random
M = int(input('Введите число строк матрицы: '))
N = int(input('Введите число строк матрицы: '))
A = []
A = [ [0]*M for i in range(N) ]
for i in range(M):
    for j in range(N):
        A[i][j] = random.randint(0, 10)
        print(A[i][j], end=' ')
    print()

