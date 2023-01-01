# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.
import random


def is_prime(a):
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    else:
        return True


print(is_prime(random.randint(0, 1000)))

