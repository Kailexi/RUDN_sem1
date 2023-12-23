# Made by Kailexi https://github.com/Kailexi/RUDN_sem1
from random import randint
import numpy as np
import os

# дз  1

nums = input().split()

try:
    with open('nums.txt') as f:
        data = [i[:-1] for i in f][:-3]

except FileNotFoundError:
    data = []

with open('nums.txt', 'w') as f:
    for i in data + nums:
        f.write(i + '\n')

try:
    with open('nums.txt') as f:
        data = [int(i[:-1]) for i in f]

    print('Сумма:', sum(data))
    print('Максимум:', max(data))
    print('Минимум:', min(data))

    with open('nums.txt', 'a') as f:
        for i in [sum(data), max(data), min(data)]:
            f.write(str(i) + '\n')

except ValueError:
    print('Ошибка чтения файла')



#дз 2
# nums = input().split()
# 
# try:
#     with open('nums.txt') as f:
#         data = [i[:-1] for i in f][:-3]
# 
# except FileNotFoundError:
#     data = []
# 
# with open('nums.txt', 'w') as f:
#     for i in data + nums:
#         f.write(i + '\n')
# 
# with open('nums.txt') as f:
#     data = [i[:-1] for i in f]
#     data_with_only_nums = [int(i[:-1]) for i in f if i[:-1].isdigit()]
# 
# print('Сумма:', sum([data_with_only_nums]))
# print('Максимум:', max(data_with_only_nums))
# print('Минимум:', min(data_with_only_nums))
# 
# with open('nums.txt', 'a') as f:
#     for i in [sum(data_with_only_nums), max(data_with_only_nums), min(data_with_only_nums)]:
#         f.write(str(i) + '\n')
# 
# 
# 
# 
# #дз 3
# 
# with open('cinema.txt') as f:
#     data = [i[:-1].split() for i in f]
# 
# choice = ''
# while choice != '0':
#     try:
#         print('1.Общее число свободных мест')
#         print('2.Общее число мест')
#         print('3.Число свободных мест в каждом ряду')
#         print('4.Проверить свободно место или занято')
#         print('0.Выйти')
#         print()
#         choice = input()
#         if not choice.isdigit() or int(choice) < 0 or int(choice) > 4:
#             raise ValueError
#         if choice == '1':
#             free_sits_count = 0
#             for i in data:
#                 free_sits_count += i.count('0')
#             print(free_sits_count)
#         if choice == '2':
#             print(sum([len(i) for i in data]))
#         if choice == '3':
#             for i in range(len(data)):
#                 print('Число свободных мест в {} ряду - {}'.format(len(data) - i, data[i].count('0')))
#         if choice == '4':
#             while 1:
#                 try:
#                     row = input('Ряд:')
#                     sit = input('Место:')
#                     if row.isdigit() is False and sit.isdigit() is False:
#                         raise ValueError
#                     print('Место свободно') if data[int(row)][int(sit)] == '0' else print('Место занято')
#                     break
#                 except ValueError:
#                     print('Ошибка ввода. Введите целое число.')
#                 except IndexError:
#                     print('Ошибка ввода. Такого места не существует.')
#     except ValueError:
#         print('Ошибка ввода. Введите целое число от 0 до 4')
#     print()
# 
# 
# 
# #дз 4
# 
# 
# 
# def print_matrix(matrix):
#     for i in matrix:
#         print('\t'.join([str(j) for j in i]))
#     print()
# 
# 
# def mult_matrices(matrix1, matrix2):
# 
#     matrix1 = np.array(matrix1)
#     matrix2 = np.array(matrix2)
#     prod_matrix = np.matmul(matrix1, matrix2)
# 
#     print_matrix(matrix1)
#     print_matrix(matrix2)
#     print_matrix(prod_matrix)
# 
#     start_m1 = (max(len(matrix1), len(matrix2)) - len(matrix1)) // 2
#     end_m1 = len(matrix1) - (max(len(matrix1), len(matrix2)) - len(matrix1)) // 2 - 1
#     start_m2 = (max(len(matrix1), len(matrix2)) - len(matrix2)) // 2
#     end_m2 = len(matrix2) - (max(len(matrix1), len(matrix2)) - len(matrix2)) // 2 - 1
#     start_m3 = (max(len(matrix1), len(matrix2)) - len(prod_matrix)) // 2
#     end_m3 = len(prod_matrix) - (max(len(matrix1), len(matrix2)) - len(prod_matrix)) // 2 - 1
# 
#     with open('matrix_things.txt', 'w') as f:
#         for i in range(max(len(matrix1), len(matrix2))):
#             s = ''
#             if start_m1 <= i <= end_m1:
#                 s += '\t'.join([str(j) for j in matrix1[i - start_m1]]) + '\t'
#             else:
#                 s += '\t ' * len(matrix1[0])
#             if i == max(len(matrix1), len(matrix2)) // 2:
#                 s += 'X\t'
#             else:
#                 s += ' \t'
#             if start_m2 <= i <= end_m2:
#                 s += '\t'.join([str(j) for j in matrix2[i - start_m2]]) + '\t'
#             else:
#                 s += '\t ' * len(matrix1[0]) + '\t'
#             if i == max(len(matrix1), len(matrix2)) // 2:
#                 s += '=\t'
#             else:
#                 s += ' \t'
#             if start_m3 <= i <= end_m3:
#                 s += '\t'.join([str(j) for j in prod_matrix[i - start_m3]])
#             print(s)
#             f.write(s + '\n')
# 
# 
# with open('matrix1.txt') as f:
#     matrix1 = [list(map(int, i.split())) for i in f]
# 
# with open('matrix2.txt') as f:
#     matrix2 = [list(map(int, i.split())) for i in f]
# 
# mult_matrices(matrix1, matrix2)
# 
# 
# #дз 5
# 
# def find_file(name):
#     hdd_names = 'qwertyuiopasdfghjklzxcvbnm'.upper()
#     all_files = []
#     for hdd in hdd_names:
#         for (r, d, f) in os.walk(hdd + ':\\'):
#             if name in f:
#                 all_files.append(os.path.join(r, name))
#     return all_files
# 
# 
# print(find_file("Laba 6.ipynb")[0])
















