# Создайте класс Example. В нём пропишите 3 (метода) функции.
# Две переменные задайте статически, две динамически.
# Первая функция: создайте переменную и выведите её
# Вторая функция: верните сумму 2-ух глобальных переменных
# Третья функция: верните результат возведения первой динамической переменной во вторую динамическую переменную
# Создайте объект класса.
# Напечатайте обе функции
# Напечатайте переменную a

class Example():
    a = 2
    b = 6

    def __init__(self, d, g):
        self.d = d
        self.g = g

    def func1(self, s = 15):
        # self.r = 7
        #print(self.r)
        print(s)

    def func2(self):
        return self.a + self.b
        #print(self.a + self.b)


    def func3(self):
        return self.d**self.g

ex = Example(3, 2)
ex.func1()
#ex.func2()
print(ex.func2())
print(ex.func3())
print(ex.a)
