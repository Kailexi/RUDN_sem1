import math as m
import matplotlib.pyplot as plt

def sine(a):

    return round(m.sin(m.radians(a)),5)

def cosine(a):

    return round(m.cos(m.radians(a)),5)
def CalculateMaxValues(v0,alpha):

    g = 9.8

    maxHeight = ( (v0**2) * (sine(alpha) ** 2)) / (2 * g)

    maxLength = ( (v0**2) * (sine(alpha*2) )) / g

    overallTime = ( ( 2 * v0 * sine(alpha) ) / g )

    return maxHeight, maxLength, overallTime

def CalculateCurrentPositon(v0,alpha,t):

    g = 9.8

    currentHeight = v0*sine(alpha)* t - (g * (t ** 2) / 2 )

    currentLength = v0*cosine(alpha)*t

    return currentHeight, currentLength



intro = 'Добро пожаловать в систему просчётов прыжка кота'
print(f'{intro:}')


intialSpeed = int(input('Введите начальную скорость кота в м/с : '))
angle = int(input('Введите под каким углом кот прыгает в градусах: '))


print(f'Максимальная высота прыжка кота равна: {CalculateMaxValues(intialSpeed, angle)[0]} м'
      f'\nА максимальная длина прыжка равна: {CalculateMaxValues(intialSpeed, angle)[1]} м')



maxHeightAngle = 0
maxLengthAngle = 0

for intervalAlpha in range(1,91):
    if CalculateMaxValues(intialSpeed,intervalAlpha)[0] > CalculateMaxValues(intialSpeed,intervalAlpha-1)[0]:

        maxHeightAngle= intervalAlpha

    if CalculateMaxValues(intialSpeed, intervalAlpha)[1] > CalculateMaxValues(intialSpeed, intervalAlpha - 1)[1]:

        maxLengthAngle = intervalAlpha


print(f"Начальный угол для максимальной высоты прыжка равен: {maxHeightAngle} градусов"
      f"\nА начальный угол для максимальной дальности прыжка равен: {maxLengthAngle} градусов")



x = 2
y = 3
g = 9.8
t = 1

v0x = x / t
v0y = y + ( g * (t ** 2) / 2 )
speedVectorSum = (v0x + v0y) ** 0.5
idealAlpha = m.acos(x/speedVectorSum*t) * (180/m.pi)

print(f'Также для того, чтобы попасть в т. (2,3) м через 1с требуется скорость равная {speedVectorSum:.1f} метрам в секунду'
      f' и угол равный {idealAlpha:.1f} ')


timeStep = float(input('Введите шаг точности построения для построения графика: '))

heightDependency = list()
lengthDependency = list()
initial_time = 0

while initial_time < CalculateMaxValues(intialSpeed, angle)[2] :

    heightDependency.append(CalculateCurrentPositon(intialSpeed, angle, initial_time)[0])

    lengthDependency.append(CalculateCurrentPositon(intialSpeed, angle, initial_time)[1])

    initial_time += timeStep


print(f'Создаём график')

plt.plot(lengthDependency,heightDependency,color='red')
plt.title('Траектория прыжка кота')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.show()





















'''''''''
visota_max = (nach_skorost**2)*(  * )


Максимальная высота прыжка равна 0.10533039581269836 м, а максимальная длина - 2.5105605589459934 м
'''''''''











