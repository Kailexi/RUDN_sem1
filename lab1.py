

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

    znachenia = []

    print(f'Здравствуйте добро пожаловать в систему получения средних значений! \n '
          f'Примечание: чтобы закончить выполнение программы введите 0 на клавиатуре \n'
          f'Вы можете приступить к заполнению значений')




    while True:

        vse_chisla = ''

        value = int(input())

        znachenia.append(value)

        for evaluate in range(0, len(znachenia)):

            vse_chisla += str(znachenia[evaluate])

            if evaluate != len(znachenia) - 1:

                vse_chisla += '+'

        the_sum = sum(znachenia)

        intermidiate_value = float(the_sum / len(znachenia))

        print(f'Среднее значение чисел {vse_chisla} равно {intermidiate_value:.5f}')


        if value == 0:

            print('Программа остановлена')

            break




def dz_exdop_2():

    cifri = []


    vhodchislo = input('Введите целое число: ')

    for i in range(0, len(vhodchislo)):
        cifri.append(int(vhodchislo[i]))
        print(f'Сумма цифр числа {vhodchislo} на данный момент равна: {sum(cifri)}')

    print(f'Окончательная сумма цифр равна: {sum(cifri)}')

def dz_exdop_3():

    spisok_chicel = ''
    cifri = list(map(int,input('Введите числа из которых вы хотите найти максимальное и минимальное число: ').split()))

    for i in range(0,len(cifri)):

        spisok_chicel += str(cifri[i])

        if i < len(cifri) -1:

            spisok_chicel += ", "

    print(f'Из данных чисел а именно {spisok_chicel}, максимальное число это {max(cifri)} а минимальное {min(cifri)} ')


''''''
