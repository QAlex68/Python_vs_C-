# Задача 62. Напишите программу, которая заполнит спирально массив 4 на 4.
# Например, на выходе получается вот такой массив:
# 01 02 03 04
# 12 13 14 05
# 11 16 15 06
# 10 09 08 07

from random import randint, uniform


# import sys
# sys.exit()


def fill_spiral_matrix(m, n):
    matrix = [[0] * n for _ in range(m)]

    top, bottom, left, right = 0, m - 1, 0, n - 1
    num = 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix


def print_2d_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()


m = int(input("Введите количество строк массива: "))
n = int(input("Введите количество столбцов массива: "))
my_matrix = fill_spiral_matrix(m, n)
print("Сгенерирован массив заполненный спирально:")
print_2d_matrix(my_matrix)
