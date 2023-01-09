# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class First:
    def get_str_int(self, x):
        #self.x = x
        if type(x) == str:
            glas = []
            soglas = []
            s = 0
            k = 0
            for i in x:
                if i in 'eyuioa' or i in 'уеыаоэяию':
                    s = s + 1   #количество гласных
                    glas.append(i)
                elif i == ' ':
                    continue
                else:
                    k = k + 1   #количество согласных
                    soglas.append(i)
            if s*k <= self.get_len(x):
                print(glas)
            else:
                print(soglas)
        else:
            summa = 0
            for i in str(x):
                if int(i) % 2 == 0:
                    summa += int(i)
            print(summa * self.get_len(x))

    def get_len(self, z):
        return len(str(z))

pr = First()
pr.get_str_int('hello')
pr.get_str_int(124)
