# Функцию которая при заданном целом числе n посчитает n + nn + nnn
def get_result(a):
    return a + a**2 + a**3

print(get_result(2.5))

def get_result_str(a):
    return a + int(str(a)*2) + int(str(a)*3)

print(get_result_str(1))
