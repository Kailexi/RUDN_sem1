

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

    all_znach = []

    print(f'Здравствуйте добро пожаловать в систему получения средних значений! \n '
          f'Примечание: чтобы закончить выполнение программы введите 0 на клавиатуре \n'
          f'Вы можете приступить к заполнению значений')




    while True:

        string_number = ''

        value = int(input())

        all_znach.append(value)

        for evaluate in range(0, len(all_znach)):

            string_number += str(all_znach[evaluate])

            if evaluate != len(all_znach) - 1:

                string_number += '+'

        the_sum = sum(all_znach)

        intermidiate_value = float(the_sum / len(all_znach))

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

    spisok_chicel = ''

    cifri = list(map(int,input('Введите числа из которых вы хотите найти максимальное и минимальное число: ').split()))

    for i in range(0,len(cifri)):

        spisok_chicel += str(cifri[i])

        if i < len(cifri) -1:

            spisok_chicel += ", "

    print(f'Из данных чисел а именно {spisok_chicel}, максимальное число это {max(cifri)} а минимальное {min(cifri)} ')


