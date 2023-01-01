# Написать функцию, которая определяет количество разрядов введенного целого числа.
raz = []
kol_raz = []


def get_colichestvo_razryadov(a):
    l = len(str(a))
    while l != 0:
        raz.append(input('Введите название разряда: '))
        kol_raz.append(a % 10)
        a = a // 10
        l -= 1
    print(dict(zip(raz, kol_raz)))


get_colichestvo_razryadov(23457)
