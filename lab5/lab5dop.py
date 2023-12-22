# Made by Kailexi https://github.com/Kailexi/RUDN_sem1
import random as rnd


# доп дз 1
def reverseD(dictionary):
    chars = set()
    for i in dictionary.values():
        for char in i:
            chars.add(char)
    chars = sorted(chars)
    new_dict = {}
    for i in chars:
        val = ''
        for k, v in dictionary.items():
            val += str(k) * v.count(i)
        new_dict[i] = int(val)
    return new_dict


d = {1: 'acc', 2: 'cab', 3: 'ccb'}
print(reverseD(d))


# доп дз 2

def fill_matrix(n, show=False):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    x, y = 0, 0
    start_x, start_y = x, 1
    end_x, end_y = n, n
    dir = 0
    for i in range(n ** 2):
        matrix[y][x] = rnd.randint(0, n)
        if show:
            for t in matrix:
                print('\t'.join([str(j) for j in t]))
            print()
        if not dir:
            x += 1
            if x == end_x:
                x = end_x - 1
                dir = 1
                end_x -= 1
        if dir == 1:
            y += 1
            if y == end_y:
                y = end_y - 1
                dir = 2
                end_y -= 1
        if dir == 2:
            x -= 1
            if x == start_x - 1:
                x = start_x
                dir = 3
                start_x += 1
        if dir == 3:
            y -= 1
            if y == start_y:
                y = start_y
                dir = 0
                start_y += 1
    return matrix


def find_row_and_col(matrix):
    max_count_zeros, max_sum = 0, 0
    row, col = 0, 0
    for i in range(len(matrix)):
        if matrix[i].count(0) > max_count_zeros:
            row = i
            max_count_zeros = matrix[i].count(0)
    for x in range(len(matrix)):
        current_sum = 0
        for y in range(len(matrix)):
            current_sum += matrix[y][x]
        if current_sum > max_sum:
            col = x
            max_sum = current_sum
    return row, col, max_sum


def get_matrix_excluding_row_and_col(matrix, row, col):
    matrix1 = []
    for y in range(row):
        new_row = []
        for x in range(col):
            new_row.append(matrix[y][x])
        matrix1.append(new_row)
    matrix2 = []
    for y in range(row + 1, len(matrix)):
        new_row = []
        for x in range(col):
            new_row.append(matrix[y][x])
        matrix2.append(new_row)
    matrix3 = []
    for y in range(row):
        new_row = []
        for x in range(col + 1, len(matrix[y])):
            new_row.append(matrix[y][x])
        matrix3.append(new_row)
    matrix4 = []
    for y in range(row + 1, len(matrix)):
        new_row = []
        for x in range(col + 1, len(matrix[y])):
            new_row.append(matrix[y][x])
        matrix4.append(new_row)
    return matrix1, matrix2, matrix3, matrix4


def print_matrix(matrix):
    for i in matrix:
        print('\t'.join([str(j) for j in i]))
    print()


mat = fill_matrix(int(input()))
print_matrix(mat)

row, col, summ = find_row_and_col(mat)
print(row, col)
print()

matrix1, matrix2, matrix3, matrix4 = get_matrix_excluding_row_and_col(mat, row, col)
print_matrix(matrix1)
print_matrix(matrix2)
print_matrix(matrix3)
print_matrix(matrix4)

# доп дз 3

count_div2, count_div13, count_div2and13 = 0, 0, 0
for _ in range(int(input())):
    num = int(input())
    if num % 2 == 0 and num % 13 == 0:
        count_div2and13 += 1
    elif num % 2 == 0:
        count_div2 += 1
    elif num % 13 == 0:
        count_div13 += 1
s = count_div2 * count_div13
if count_div2and13 > 1:
    print(s + count_div2and13 * (count_div2 + count_div13) + (count_div2and13 / 2) * (count_div2and13 - 1))
elif count_div2and13 == 1:
    print(s + count_div2 + count_div13)
else:
    print(s)
