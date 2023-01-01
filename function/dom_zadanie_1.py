def get_plus(): return a + c
def get_minus(): return a - c
def get_mulepl(): return a * c
def get_devesion(): return a / c

while True:
    a = float(input('Введите число: '))
    b = input('Введите операцию: ')
    c = float(input('Введите число: '))
    if b == '+':
        print(get_plus())
    elif b == '-':
        print(get_minus())
    elif b == '/':
        try:
            print(get_devesion())
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
            break
    elif b == '*':
        print(get_mulepl())
    else:
        break