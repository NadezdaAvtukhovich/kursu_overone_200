# Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(True)
            else:
                print(False)
        else:
            print(True)
    else:
        print(False)


is_year_leap(2022)

