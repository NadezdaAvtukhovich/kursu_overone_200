# Заполните один кортеж десятью случайными целыми числами от 0 до 5
# включительно. Также заполните второй кортеж числами от -5 до 0.
# Объедините два кортежа с помощью оператора +, создав тем самым третий
# кортеж. С помощью метода кортежа count() определите в нем количество
# нулей. Выведите на экран третий кортеж и количество нулей в нем.
import random
# a = tuple([random.randint(0, 5) for a in range(10)])
# b = tuple([random.randint(-5, 0) for b in range(10)])
i = 0
a = []
b = []
while i <= 10:
    a.append(random.randint(0, 5))
    b.append(random.randint(-5, 0))
    i += 1
c = tuple(a) + tuple(b)
print(c)
print(c.count(0))


