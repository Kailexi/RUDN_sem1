# Made by Kailexi https://github.com/Kailexi/RUDN_sem1


n, start, finish = map(int,
                       input(
                           "Введите количество дисков, начальный стержень, и итоговый стержень через пробел: ").split())


def recurrent_hanoi_towers(n, start, finish):
    if n <= 0: return

    temp_pillar = 6 - (start + finish)

    recurrent_hanoi_towers(n - 1, start, temp_pillar)

    print(f"Перенести диск {n} со стержня {start}, на стержень {finish}")

    recurrent_hanoi_towers(n - 1, temp_pillar, finish)


def cyclic_hanoi_towers(n, start, finish):
        disks = [0] * n  # где диск а главное где ДИСК стоп а их ваще сколько
        counter = [0] * n  # сколько раз мы заюзали перемещения
        cords = {0: start, 1: finish, 2: 6 - start - finish}

        for i in range(2 ** n):
            for disk in range(n):
                if 2 ** disk + 2 ** (disk + 1) * counter[disk] == i:

                    counter[disk] += 1
                    old = disks[disk]
                    disks[disk] = (disks[disk] + 1 + (n - 1 - disk) % 2) % 3

                    print("%i: %i --> %i" % (disk + 1, cords[old], cords[disks[disk]]))
                    break


print("Решение через рекурсию")
print(recurrent_hanoi_towers(n, start, finish))

print("Решение через цикл")
print(cyclic_hanoi_towers(n, start, finish))
