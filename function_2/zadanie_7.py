# Вычислить значения нижеприведенной функции в диапазоне значений x от -10 до 10 включительно с шагом,
# равным 1.
# y = 𝑥^2 при -5 <= x <= 5;
# y = 2*|x|-1 при x < -5;
# y = 2x при x > 5.
# Вычисление значения функции оформить в виде программной функции, которая принимает значение x,
# а возвращает полученное значение функции (y).
def get_result_function(x):
    print('Значение x', 'Значение функции')
    while x >= -10 and x <= 10:
        if x >= -5 and x <= 5:
            print(x, '\t\t', x ** 2)
            x += 1
        elif x < -5:
            print(x, '\t\t', 2 * abs(x) - 1)
            x += 1
        elif x > 5:
            print(x, '\t\t', 2 * x)
            x += 1


get_result_function(float(input('Введите значение переменной x: ')))

