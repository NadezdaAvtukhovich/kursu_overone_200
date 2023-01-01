# Функция, вычисляющая среднее арифметическое элементов массива.
# Массив должен состоять из случайных чисел, длинной 10 элементов.
import random
from statistics import mean


def sr_arefmet(a):
    return round(mean(a))


b = []
# for i in range(0, 11):
#     c = random.randint(0, 10)
#     b.append(c)
# print(b)
[b.append(random.randint(0, 10)) for i in range(0, 11)]
print(sr_arefmet(b))


