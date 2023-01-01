# Введите два числа с клавиатуры. Поделите одно на другое.
# Обработайте деления на ноль, преобразования и общее исключение.

try:
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
    print(a/b)
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except ValueError:
    print('Что-то пошло не так!')
except Exception:
    print('Общее исключение')

