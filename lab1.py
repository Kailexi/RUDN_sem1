


def exercise1():
    v0 = int(input('Enter v0: '))

    g = float(input('Enter g: '))

    t = float(input('Enter t: '))

    t_max = float((2 * v0) / g)

    y = (v0 * t - 1 / 2 * g * t ** 2)

    if 0 <= float(t) <= t_max:

        print(f'the estimate height is: {y:.5e} metres')
    else:

        print(f'Bro no way that will drop through the textures')

def dz_ex1():
    x = 2

    print(f'Initial value of x: {x}')

    x += 3

    print(f'Value after +=3 addition: {x}')

    x = (x + 1) / 2

    print(f'Value after (x+1) /2 equates to: {x}')

    x = (x + 1) / 2

    print(f'Value after (x+1) /2 equates to: {x}')

    x = x < 5

    print(f'Value after logical expression is: {x}')

    x = str(x)

    print(f'Value after conversion is: {x} \nHowever the type is: {type(x)}')



def dz_ex2():

    b = []

    print(f'Здравствуйте добро пожаловать в систему получения средних значений! \n '
          f'Примечание: чтобы закончить выполнение программы введите 0 на клавиатуре \n'
          f'Вы можете приступить к заполнению значений')




    while True:

        string_number = ''

        value = int(input())

        b.append(value)

        for evaluate in range(0, len(b)):

            string_number += str(b[evaluate])

            if evaluate != len(b) - 1:

                string_number += '+'

        the_sum = sum(b)

        intermidiate_value = float(the_sum / len(b))

        print(f'Среднее значение чисел {string_number} равно {intermidiate_value:.5f}')


        if value == 0:

            print('Программа остановлена')

            break




def dz_exdop_2():

    cifri = []


    izn = input('Введите целое число: ')

    for i in range(0, len(izn)):
        cifri.append(int(izn[i]))
        print(f'Сумма цифр числа {izn} на данный момент равна: {sum(cifri)}')

    print(f'Окончательная сумма цифр равна: {sum(cifri)}')

def dz_exdop_3():

    ok = ''

    cifri = list(map(int,input('Введите числа из которых вы хотите найти максимальное и минимальное число: ').split()))

    for i in range(0,len(cifri)):

        ok += str(cifri[i])

        if i < len(cifri) -1:

            ok += ", "

    print(f'Из данных чисел а именно {ok}, максимальное число это {max(cifri)} а минимальное {min(cifri)} ')


