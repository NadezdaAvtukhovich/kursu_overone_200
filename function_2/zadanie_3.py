# Написать функцию, которая заполняет массив длинной 10 элементов, случайными числами в диапазоне,
# указанном пользователем с клавиатуры.
# Функция должна принимать два аргумента – начало диапазона и его конец, при этом ничего не возвращать.
import random

arr = []
def get_massiv(k, m):
    # пересмотреть позже (вывод каких-то двойных квадратных скобок) arr.append([random.randrange(k, m) for i in range(0, 10)])
    for i in range(0, 10):
        arr.append(random.randrange(k, m))
    print(arr)


a = int(input('Введите начало диапазона: '))
b = int(input('Введите конец диапазона: '))
get_massiv(a, b)