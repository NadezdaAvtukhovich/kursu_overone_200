# Размерность матрицы вводится с клавиатуры, заполнить матрицу случайными числами от 10 до 50.
# Найти наибольшую сумму элементов в столбцах матрицы.
# Вывести индекс столбца с максимальной суммой элементов на экран
import random
M = int(input('Введите число строк матрицы: '))
N = int(input('Введите число строк матрицы: '))
A = [ [0]*M for i in range(N) ]
for i in range(M):
    for j in range(N):
        A[i][j] = random.randint(10,50)
        print(A[i][j], end='\t')
    print()
maxim = 0
for j in range(N):
    summ = 0
    for i in range(M):
        summ += A[i][j]
    if summ >= maxim:
        maxim = summ
        max_stolbec = j
print(f'Столбец {max_stolbec+1} имеет максимальную сумму, равную {maxim}')