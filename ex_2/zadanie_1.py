#1 Написать программу для получения списка словарей из списков.

color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
a = dict(zip(color_name, color_code))
c = []
for k, v in a.items():
    b = dict(color_name=k, color_code=v)
    c.append(b)
print(c)