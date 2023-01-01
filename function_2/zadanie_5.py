# Написать функцию, которая считает сколько гласных и согласных в строке. Строку вводить с клавиатуры.
def get_koluchestvo(a):
    s = 0
    k = 0
    for i in a:
        if i in 'eyuioa' or i in 'уеыаоэяию':
            s = s + 1
        elif i == ' ':
            continue
        else:
            k = k + 1
    print(f'Количество гласных {s}, количество согласных {k}')


get_koluchestvo(input('Stroka: '))
