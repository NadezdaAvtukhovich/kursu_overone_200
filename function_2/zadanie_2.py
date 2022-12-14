# В зависимости от выбора пользователя вычислить площадь круга, прямоугольника или треугольника.
# Для вычисления площади каждой фигуры должна быть написана отдельная функция.
# Площадь по формуле Герона.

def get_S_circle(k):
    return 3.14 * k ** 2


def get_S_rectangle(m, n):
    return m * n


def get_S_triangle(x, y, z):
    p = (x + y + z) / 2
    return (p * (p - x) * (p - y) * (p - z)) ** (0.5)


a = input('Площадь какой фигуры хотите вычислить (круг, прямоугольник, треугольник)? ')
if a == 'круг':
    r = float(input('Введите радиус круга: '))
    print(get_S_circle(r))
elif a == 'прямоугольник':
    b = float(input('Введите длину стороны прямоугольника: '))
    c = float(input('Введите длину стороны прямоугольника: '))
    print(get_S_rectangle(b, c))
else:
    b = float(input('Введите длину стороны треугольника: '))
    c = float(input('Введите длину стороны треугольника: '))
    d = float(input('Введите длину стороны треугольника: '))
    print(get_S_triangle(b, c, d))
