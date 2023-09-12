# Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
# Например, даны 2 матрицы:
# 2 4 | 3 4
# 3 2 | 3 3
# Результирующая матрица будет:
# 18 20
# 15 18

from random import randint
import numpy as np


# import sys
# sys.exit()


def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    # перемножение матриц посредством циклов, самый неэффективный способ!!
    #     if cols1 != rows2:
    #         print("Несовместимые размеры матриц!!")
    #     else:
    #         res_matrix = [[0 for x in range(rows1)] for y in range(cols2)]
    #         for i in range(len(matrix1)):
    #             for j in range(len(matrix2[0])):
    #                 for k in range(len(matrix2)):
    #                     res_matrix[i][j] = matrix1[i][k] * matrix2[k][j]
    #         print("Результат перемножения матриц:")
    #         print_2d_matrix(res_matrix)

    # Решение с помощью сборки для обработки массивов Numpy, пакет устанавливается pip install numpy (терминал)
    # работает на три порядка быстрее
    if cols1 != rows2:
        print("Несовместимые размеры матриц!!")
    else:
        res_matrix = np.dot(matrix1, matrix2)
        print("Результат перемножения матриц:")
        print_2d_matrix(res_matrix)


def print_2d_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()


def create_fill_2d_matrix(m, n, start, finish):
    matrix = [[randint(start, finish) for j in range(m)] for i in range(n)]
    return matrix


m1 = int(input("Введите количество строк массива 1: "))
n1 = int(input("Введите количество столбцов массива 1: "))
start1 = int(input("Введите начало диапазона элементов 1: "))
finish1 = int(input("Введите конец диапазона элементов 1: "))
my_matrix1 = create_fill_2d_matrix(m1, n1, start1, finish1)
print("Сгенерирован массив 1:")
print_2d_matrix(my_matrix1)
m2 = int(input("Введите количество строк массива 2: "))
n2 = int(input("Введите количество столбцов массива 2: "))
start2 = int(input("Введите начало диапазона элементов 2: "))
finish2 = int(input("Введите конец диапазона элементов 2: "))
my_matrix2 = create_fill_2d_matrix(m2, n2, start2, finish2)
print("Сгенерирован массив 2:")
print_2d_matrix(my_matrix2)
matrix_multiplication(my_matrix1, my_matrix2)
