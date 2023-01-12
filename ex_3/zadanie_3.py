# 3 Создайте класс IceCream (для заказа мороженого с добавкой или без),
# принимающий 1 аргумент при инициализации (отвечающий за добавку к мороженому).
# В этом классе реализуйте метод info_about_icecream(), выводящий на печать «Мороженное и {ДОБАВКА}»
# в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое».

class IceCream:
    def __init__(self, dobavka):
        self.dobavka = dobavka

    def info_about_icecream(self):
        if self.dobavka != 'Без':
            print(f'Мороженное и добавка {self.dobavka}')
        else:
            print(f'Обычное мороженое')

a = IceCream('Без')
a.info_about_icecream()

b = IceCream('Шоколад')
b.info_about_icecream()

c = IceCream('Карамелька')
c.info_about_icecream()