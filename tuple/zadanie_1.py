# создайте кортеж из случайных 10 чисел. Найдите его максимальный минимальный элемент.
import random
# i = 0
a = [random.randint(0, 10) for i in range(1, 10)]
# while i <= 10:
#     a.append(random.randint(0, 10))
#     i += 1
b = tuple(a)
print(f'Кортеж {b} с минимальным элементом {min(b)} и максимальным элементом {max(b)}')