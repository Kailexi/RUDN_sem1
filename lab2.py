
def happy_number(a):
    a = str(a)
    if len(a) < 4:
        a += '0' *  (4 - len(a))
        a = int(a)

    if str(a)[0] == str(a)[-1] and str(a)[1] == str(a)[-2]:
        print(f'{a} это счастливое/симметричное четырехзначное число')

    else:
        print(f'увы {a} это не симметричное четырехзначное число')

def checkLeapYear(year):
    if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
        print("YES")
    else:
        print("NO")

def cowsDojaCatReferencelol(n):

    grammar_check = ''

    if n % 10 == 1:

        grammar_check = 'корова'

    elif n % 2 == 0 or n % 3 == 0 or n % 4 == 0:

        grammar_check = 'коровы'

    elif n % 5 == 0:

        grammar_check = 'коров'

    print(f'На лугу пасётся {n} {grammar_check}')





def minDel(n):
    i = 2
    while n % i != 0:
        i += 1
    print(f'Минимальный делитель равен {i}')

def ForDelMin(vhod_chislo):
    count = 0
    for i in range(2, int(vhod_chislo ** 0.5 + 1)): # минимальный делитель всегда будет находиться в промежутке от 0 до корня из числа

        if vhod_chislo % i == 0:
             count = i
             break

    print(f'Минимальный делитель равен {count}')




