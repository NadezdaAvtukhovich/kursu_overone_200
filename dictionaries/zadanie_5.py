# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами,
# а элементы второго — соответственно значениями нашего словаря.
a = ['a', 'b', 'c']
b = [1, 2, 3]
print(dict(zip(a, b)))