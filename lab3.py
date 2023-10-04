
def firstStatement(n):
    return n > 0 and len(str(n)) == 3 and str(n)[2] == '0'

def secondStatement(n):
    return n % 2 == 1 and (n % 3 == 0 or n % 5 == 0)

def thirdStatement(n):
    return n in range(2,6)

def fourthStatement(n):
    try:
        return len(n) == 3 and (str(n)[0] == str(n)[1] == str(n)[2])
    except:
        return False

def logicalStatementOne(n):
    return not(n and not(n) and 3 and 5)

def logicalStatementTwo(n):
    return not logicalStatementOne(n)

a = input('Введите любое выражение: ')

print('Результат работы первой подпрограммы:', logicalStatementOne(a))
print('Результат работы второй подпрограммы:', logicalStatementTwo(a))


'''''''''
x = int(input())
print(f'Результат первой программы {firstStatement(x)}'
      f'\nРезультат второй программы {secondStatement(x)}'
      f'\nРезультат третьей программы {thirdStatement(x)},'
      f'\nРезультат четвёртой программы {fourthStatement(x)}')
'''''''''
