def exercise1():
    v0 = int(input('Enter v0: '))

    g = float(input('Enter g: '))

    t = float(input('Enter t: '))

    t_max = float((2 * v0) / g)

    y = (v0 * t - 1 / 2 * g * t ** 2)

    if 0 <= float(t) <= t_max:

        print(f'the estimate height is: {y:.5e} metres')
    else:

        print(f'Bro no way that will through the textures')

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
    b= []
    print('Введите 5 значений')
    for i in range(0,5):
        value = int(input())
        b.append(value)
    the_sum = sum(b)
    intermidiate_value = float(the_sum / len(b))
    print(f'Среднее значение этих чисел равно {intermidiate_value:.5f}')
'''''''''''

    def dz_ex3():


    def dz_ex4():
'''''''''''
