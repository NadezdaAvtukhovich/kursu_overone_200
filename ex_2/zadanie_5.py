# Есть файл text.txt. Вывести слово, имеющее минимальную длину. Обработать исключения.
try:
    f = open('txt.txt', 'r')
    str1 = (f.readline()).split()
    maxim = ''
    for i in str1:
        if len(i) > len(maxim):
            maxim = i
        elif len(i) == len(maxim):
            print(f'Найдены одинаковы по длине слова: {i} и {maxim}')
    print(f'Первое слово, имеющее максимальную длину: {maxim}')
    f.close()
except FileNotFoundError:
    print('Файл не был найден!')
    # pass - если прописать команду, то ошибка обработается все равно, но пользователю ничего не сообщится
except Exception:
    print("Something gone wrong!")


