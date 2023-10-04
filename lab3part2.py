
def firstGraphCheck(x, y):
    return (x >= 4 and y >= 3) or (x < 4 and y < 3 and x + y <= 0)

def secondGraphCheck(x,y):
        return (3 - abs(x) >= 0) and (3 - abs(y) >= 0) and (x ** 2 + y ** 2 >= 9)

def thirdGraphCheck(x,y):
        return (0 <= x <= 5) and (0 <= y <= 5) and ((x - 5) ** 2 + (y - 5) ** 2 >= 25)

def positive(x):
    return print('Положительное')
def negative(x):
    return print('Отрицательное')
def test():
    number = int(input('Введите целое число:'))
    if number > 0:
        positive(number)
    else:
        negative(number)

def getInput():
    x = input()
    return x

def testInput(x):
    try:
        int(x)
    except ValueError:
        return False
    else:
        return True

def strToInt(x):
    if testInput(x):
        x = int(x)
        return x

def printInt(x):
    if testInput(x):
        print(x, type(x))
    else:
        print('Не число мейт!')









'''''''''
#Расскомментите если хотите проверить упраженение 5
x = getInput()
testInput(x)
strToInt(x)
printInt(x)
'''''''''

'''''''''
#Расскомментите если хотите проверить упраженение 4
x = int(input())
y = int(input())

print(f'Проверка на принадлежность к первому графику x,y {x}, {y}, {firstGraphCheck(x,y)}\n'
      f'Проверка на принадлежность к второму графику x, y {x}, {y}, {secondGraphCheck(x,y)}'
      f'\nПроверка на принадлежность к третьему графику x,y {x}, {y}, {thirdGraphCheck(x,y)}')
'''''''''''
