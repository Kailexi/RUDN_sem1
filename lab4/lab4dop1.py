# Made by Kailexi https://github.com/Kailexi/RUDN_sem1

def convert_base_R(num, to_base=10, from_base=10):

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)

    if n < to_base:
        return alphabet[n]
    else:
        return convert_base_R(n // to_base, to_base) + alphabet[n % to_base]




choice = 1
while choice:
    try:
        A, B, base = input('Первое число: '), input('Второе число: '), int(input('Система счисления чисел: '))

        print('1.Вывести сумму')
        print('2.Вывести разницу')
        print('3.Вывести произведение')
        print('4.Вывести частное')
        print('0.Выйти')

        choice = input()

        print('Итог:', end=' ')
        if choice == '1':
            print(convert_base_R(int(convert_base_R(A, 10, base)) + int(convert_base_R(B, 10, base)), base, 10))
        if choice == '2':
            print(convert_base_R(int(convert_base_R(A, 10, base)) - int(convert_base_R(B, 10, base)), base, 10))
        if choice == '3':
            print(convert_base_R(int(convert_base_R(A, 10, base)) * int(convert_base_R(B, 10, base)), base, 10))
        if choice == '4':
            if B == '0':
                raise ZeroDivisionError
            print(convert_base_R(int(convert_base_R(A, 10, base)) // int(convert_base_R(B, 10, base)), base, 10))
    except ZeroDivisionError:
        print('Ошибка. Деление на ноль')














