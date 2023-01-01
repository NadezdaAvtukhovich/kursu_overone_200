# Создать текстовый файл, записать в него построчно данные ,которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
try:
    with open('zadanie_3.txt', 'w', encoding = 'utf-8') as f:
        while True:
            a = input('Введите данные:')
            if a == '':
                break
            f.write(a + '\n')
except FileNotFoundError:
    print('Невозможно открыть файл')

