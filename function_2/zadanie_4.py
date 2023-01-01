# Написать функцию и сделать так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
def get_hour_min_sek(a):
        dni = a // 3600 // 24
        a = a - dni*3600*24
        hour = a // 3600
        a = a - hour*3600
        min = a // 60
        sek = a % 60
        print(f' дни {dni}, часы {hour}, минуты {min}, секунды {sek}')

sekunda = int(input('Введите количество секунд: '))
get_hour_min_sek(sekunda)