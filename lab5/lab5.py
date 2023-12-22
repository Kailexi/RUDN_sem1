# Made by Kailexi https://github.com/Kailexi/RUDN_sem1
from random import randint


# дз 1
def lower_or_upper_print(string):
    upper_count, lower_count = len([0 for i in string if i.isupper()]), len([0 for i in string if i.islower()])

    if upper_count > lower_count:
        return string.upper()

    if upper_count < lower_count:
        return string.lower()

    return string


print(lower_or_upper_print(input()))

# дз 2
word = 'объектно-ориентированный'

requirement = ('объект', 'ориентир', 'тир', 'кот', 'рента')

for i in range(len(word) - 1):

    for j in range(i + 1, len(word)):
        if word[i:j] in requirement:
            print(word[i:j], i, j - 1)

print('Кот:')
num_combs = []
for i in range(len(word)):
    for j in range(len(word)):
        for k in range(len(word)):

            combined = word[i] + word[j] + word[k]

            if 'к' in combined and 'о' in combined and 'т' in combined and i + j + k not in num_combs:
                print(i, j, k)
                num_combs.append(i + j + k)

# дз 3
while True:
    nums = [input() for i in range(int(input('Введите количество чисел: ')))]
    digits_included = False
    summa = 0

    for i in nums:
        num = i
        chars = set([j for j in i])

        for char in chars:
            if not char.isdigit():
                num = num.replace(char, '')

        if num != '':
            summa += int(num)
            digits_included = True

    if digits_included:
        print(summa)
        break


# дз 4
def reverse_dict(dictionary):
    new_dict = {}

    for k, i in dictionary.items():
        if i not in new_dict.keys():
            new_dict[i] = [k]
        else:
            new_dict[i].append(k)
    return new_dict


dict1 = {1: 'adaw', 2: 'dawdad', 3: 'adawd', 4: 'adawd'}
dict2 = reverse_dict(dict1)

for k, i in dict2.items():
    print(k + ":", ', '.join([str(j) for j in i]))


# дз 5

def func(school, print_data=False, class_name='', new_count=0, delete=False):
    if not delete and class_name:
        school[class_name] = new_count

    elif class_name:
        count = school.pop(class_name)

        for k, v in school.items():
            school[k] = v + (count - count % len(school))

        if count:
            for k, v in school.items():

                school[k] = v + 1
                count -= 1

                if not count:
                    break
    if print_data:

        print('Общее кол-во учащихся:', sum([i for i in school.values()]))
        print('Общее кол-во классов:', len(school))

        for k, v in school.items():
            if 21 <= v <= 24:
                print('Класc {} имеет {} ученика'.format(k, v))

            else:
                print('Класc {} имеет {} учеников'.format(k, v))

    return school

nums = [str(i) for i in range(1, 12)]


letters = 'абвгдежзилкмн'

classes = [nums[randint(0, 9)] + letters[randint(0, len(letters) - 1)] for _ in range(randint(3, 10))]

students = [randint(10, 30) for _ in range(len(classes))]

school = {k: v for (k, v) in zip(classes, students)}

#no dynamic cast sucks
#WHY NO MALLOC AND CALLOC IT GENERATES FUN
#also where is memory manipulation in python i want pointers and bit casting





















