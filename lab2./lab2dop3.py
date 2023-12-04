def getInfo(guess):
    print(f'Загаданное число - {guess}?')
    print('1. Да')
    print('2. Нет, мое число меньше')
    print('3. Нет, мое число больше')
    return int(input('Ответ: '))

length = int(input('Введите длину списка натуральных чисел, из которого вы загадали число: '))

left = 1
right = length
popitka = 1

while True:

    current_guess = (right + left) // 2
    question_answer = getInfo(current_guess)

    if question_answer == 1:
        print(f'Фига я мегамозг угадал за {popitka} попытки!')
        break

    if left == right:
        print('ЭЭЭ БРАТ ТАК НЕЛЬЗЯ')
        break

    if question_answer == 2:
        right = current_guess - 1
        popitka += 1

    elif question_answer == 3:
        left = current_guess + 1
        popitka += 1





































