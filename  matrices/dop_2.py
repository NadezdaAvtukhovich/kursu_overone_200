# Создать квадратную матрицу:
# 0 2 4 6 8 10
# 1 3 5 7 9 11
# 2 4 6 8 10 12
# 3 5 7 9 11 13
# 4 6 8 10 12 14
# 5 7 9 11 13 15

M = int(input('Введите число строк матрицы: '))
N = int(input('Введите число строк матрицы: '))
A = []
A = [ [0]*M for i in range(N) ]
for i in range(M):
    for j in range(N):
        A[i][0] = i
        if j in range(1, N+1):
            A[i][j] = A[i][j-1]+2
        print(A[i][j], end='\t')
    print()

