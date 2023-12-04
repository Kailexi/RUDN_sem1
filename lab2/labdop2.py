


power_of_the_grill = int(input('Введите количество котлет, которые можно положить одновременно на гриль: '))
time_of_roasting = float(input('Введите количество минут, требуемое для обжарки одной стороны котлеты: '))
amount_of_cutlets = int(input('Введите количество котлет: '))

if amount_of_cutlets <= power_of_the_grill:
    time = 2 * time_of_roasting
elif (amount_of_cutlets * 2) % power_of_the_grill == 0:
    time = time_of_roasting * ((amount_of_cutlets * 2) // power_of_the_grill)
else:
    time = time_of_roasting * (1 + ((amount_of_cutlets * 2) // power_of_the_grill))

print(f'Понадобится минут: {time:.2f}.')





