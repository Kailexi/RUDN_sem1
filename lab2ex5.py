
array = []

print('Введите числа с которомы вы хотите совершить операции\nПримечание! 0 завершит операцию\n')

while True:
    entrance_numbers = int(input())
    if entrance_numbers == 0:
        break

    array.append(entrance_numbers)




print(f'Что вы хотите сделать с числами {array}? Выберитите из предоженных вариантов \n'
      f'1. Найти сумму введённых чисел.\n'
      f'2. Найти произведение введённых чисел.\n'
      f'3. Найти среднее значение введённых чисел.\n'
      f'4. Найти максимальное из введённых чисел.\n'
      f'5. Найти минимальное из введённых чисел.\n'
      f'6. Определить количество чётных и нечётных эллементов.  ')

option_check = int(input('Введите число выбранного вами варианта: '))

if option_check == 1:
    print(f'Сумма чисел равна {sum(array)}')

elif option_check == 2:
    j = 1

    for i in range(0, len(array)):
        j *= array[i]


    print(f'Произведение чисел равно {j}')

elif option_check == 3:
    print(f'Среднее значение введённых чисел равно {sum(array) / len(array)}')

elif option_check == 4:
    print(f'Максимальное число равно {max(array)}')

elif option_check == 5:
    print(f'Минимальное число равно {min(array)}')

elif option_check == 6:
     even_count = 0
     odd_count = 0
     for i in range(0, len(array)):

        if array[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

     print(f'Количество четных чисел {even_count}, а нечетных {odd_count}')





