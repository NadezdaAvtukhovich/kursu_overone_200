# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
def calculator():
    a = float(input('Введите число: '))
    b = input('Введите операцию: ')
    if b != '':
        c = float(input('Введите число: '))
        if b == '+':
            print(a + c)
            calculator()
        elif b == '-':
            print(a - c)
            calculator()
        elif b == '/':
            try:
                print(a / c)
                calculator()
            except ZeroDivisionError:
                print('На ноль делить нельзя!')
        else:
            print(a * c)
            calculator()


calculator()
