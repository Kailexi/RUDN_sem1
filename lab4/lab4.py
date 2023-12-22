# Made by Kailexi https://github.com/Kailexi/RUDN_sem1


# 1 первое задание
def ex1(n1, n2):
    try:
        n1, n2 = input(), input()

        print(float(n1) + float(n2))

    except ValueError:
        print(n1 + n2)


# 1 кусок каждому P.S второе задание

n = int(input())
pieces_count = 1

while pieces_count < n:
    pieces_count *= 2

print(f'Если гостям нужен хотя бы 1 кусок то нужно {pieces_count} делить пирог')

# 2 куска половине гостей

pieces_count = 1

while pieces_count < n * 1.5:
    pieces_count *= 2

print(f'Если половине гостей нужно хотя бы 2 куска то нужно {pieces_count} делить пирог')

# 3 1 кусок каждому + 10 в запасе
pieces_count = 1

while pieces_count <= n + 10:
    pieces_count *= 2

print(f'Если гостям нужен хотя бы 1 кусок то нужно {pieces_count} делить пирог и ещё будет 10 в запасе :)')


# Фибонначи проверка на точность

def fib(n=10):
    for i in range(n):
        x = (((1 + 5 ** 0.5) / 2) ** (i + 1) - ((1 - 5 ** 0.5) / 2) ** (i + 1)) / 5 ** 0.5
        if x - float(int(x)) < 0.001:
            print(i)


# Кубики

x, y = int(input())
decrement = 1
pullout_count = 1

while y - decrement >= 0:
    y -= decrement

    pullout_count += 1
    decrement *= 2

    if pullout_count == x + 1:
        pullout_count = 1

    elif pullout_count > 25:
        decrement -= 25

print(f'Проиграл ребенок под номером {pullout_count}')

