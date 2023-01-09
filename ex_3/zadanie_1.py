# 1 Реализовать Рекурсию. Возведение числа x в степень y
#ИЛИ
#Определить функцию, которая будет дублировать нули в списке и вернуть в виде итеррируемого объекта-коллекции.
#Input:                         Output:
# func([0,0,0])            --> [0,0,0,0,0,0]
# func([1,2,100,0,3,4,5,0])--> [1,2,100,0,0,3,4,5,0,0]
def stepen(a,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return stepen(a, n // 2) ** 2
    else:
        return stepen(a, n-1) * a

print(stepen(2, 5))

l = []
def dubl_null(k):
    for i in k:
        l.append(i)
        if i == 0:
            l.append(i)
    return l
a = [1, 2, 100, 0, 3, 4, 5, 0]
print(dubl_null(a))