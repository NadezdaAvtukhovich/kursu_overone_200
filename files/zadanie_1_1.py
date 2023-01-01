# В файле, в одну строку записаны слова и числа через пробел или _ найти сумму всех чисел.
f = open('zadanie_1.txt', 'r')
str1 = ((f.readline()).replace('_', ' ')).split(' ')
summa = 0
for i in str1:
    try:
        summa += int(i)
    except ValueError:
        print(f'Слово {i} не возможно привести к типу integer')
print(f'Сумма всех чисел в строке: {summa}')
f.close()

