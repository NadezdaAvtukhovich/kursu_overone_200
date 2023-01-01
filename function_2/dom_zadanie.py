# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
def get_koluchestvo(a):
    if type(a) == tuple:  # кортеж
        for i in a:
            if type(i) == str:
                print(f'Количество символов в {i} равно {len(i)}')
    elif type(a) == list:  # список
        chisla = 0
        strk = 0
        for i in a:
            nechet = 0
            if type(i) == int:
                chisla += len(str(i))
                for j in str(i):
                    if int(j) % 2 != 0:
                        nechet += 1
                print(f'Количество нечетных цифр в числе {i} равно {nechet}')
            else:
                strk += len(i)
                print(f'В строке {i} количество букв равно {len(i)}')
        print(f'Количество цифр в {a} равно {chisla} и букв {strk}')
    else:
        print('Неверный тип')


b = ('Mum', 12, 3, 'Hello', 'Love')
d = ['Привет', 345, 10, 'World']
get_koluchestvo(b)
get_koluchestvo(d)
