count = 0
fail_count = 0
data = []


def askValue():
    x1 = int(input())
    return x1


def checkValue(x1):
    check = True

    if x1 == chisla[0] * chisla[1]:

        print('Ответ правильный!')
        global count
        count += 1
        return check

    else:
        print(f'Ответ не правильный,правильный ответ {chisla[0] * chisla[1]} ')

        global fail_count
        fail_count += 1

        return check == False


for i in range(1, 5 + 1):
    chisla = list(map(int, input(f'Введите 2 числа\nПример: 5 6\n ').split()))
    print(f'Сколько будет {chisla[0]} * {chisla[1]} ?')

    user_answer = askValue()
    checkValue(user_answer)

    if count == 3:
        print('Офигеть ты молодец, умножать умеешь!')

    if fail_count == 3:
        print('Нифига ты зачем в универ пришёл инжнерный тогда ХД')

print('Игра закончена спасибо за игру!')
