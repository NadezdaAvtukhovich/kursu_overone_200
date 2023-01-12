# 5 Создать класс Animal и определить в нем метод make_a_sound().
# Метод должен вывоводить строку "Издает звук"
# Cоздать классы Cat и Dog с методами scratch() и dig() соответственно.
# Метод scratch должен выводить строку "Царапать мебель".
# Метод dig должен выводить строку "Рыть землю".
# в классах Cat и Dog переопределите метод make_a_sound() базового класса Animal.
# (Cat: make_a_sound() -> '<...>', Dog: make_a_sound() -> '<...>')

class Animal:
    def make_a_sound(self):
        print("Издает звук:")

class Cat(Animal):

    def make_a_sound(self):
        print('Царапать мебель')


class Dog(Animal):

    def make_a_sound(self):
        print('Рыть землю')

cat1 = Cat()
cat1.make_a_sound()
dog1 = Dog()
dog1.make_a_sound()

