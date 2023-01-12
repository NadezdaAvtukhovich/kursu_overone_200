# 4 Инкапсуляция. Определить класс Car, который будет содержать конструктор,
# в котором будет инициализироваться private переменная maxprice,
# а также методы изменения и вывода максимальной стоимости машины.

class Car:
    def __init__(self, maxprice):
        self.__maxprice = maxprice

    def get_summa(self):
        return self.__maxprice
    def set_summa(self, amount):
        self.__maxprice += amount


car1 = Car(5000)
car1.set_summa(4000)
print(car1.get_summa())
