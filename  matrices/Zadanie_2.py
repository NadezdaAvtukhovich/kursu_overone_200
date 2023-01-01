# Матрица N x M, можно задать статически. Элементы заполняются случайными числами.
# Вводить с клавиатуры число и если оно есть в матрице, то вывести индекс строки и колонки в которой оно находится.
import random
M = 5
N = 5
A = []
A = [ [0]*M for i in range(N) ]
for i in range(M):
    for j in range(N):
        A[i][j] = random.randint(0, 10)
        print(A[i][j], end=' ')
    print()
c = int(input('Введите число искомое число: '))
for i in range(M):
    for j in range(N):
        if A[i][j] == c:
            print (f'Число {c} находится в матрице в строке {i+1} и столбце {j+1}')

