# Задача 47. Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
# m = 3, n = 4.
# 0,5 7 -2 -0,2
# 1 -3,3 8 -9,9
# 8 7,8 -7,1 9
import random
from random import randint, uniform


def print_2d_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{0:0.2f}".format(matrix[i][j]), end="  ")
            # print("{:4d}".format(matrix[i][j]), end="")
        print()


def create_fill_2d_matrix(m, n, start, finish):
    matrix = [[round(random.uniform(start, finish), 2) for j in range(m)] for i in range(n)]
    return matrix


m = int(input("Введите количество строк массива: "))
n = int(input("Введите количество столбцов массива: "))
start = int(input("Введите начало диапазона элементов: "))
finish = int(input("Введите конец диапазона элементов: "))
my_matrix = create_fill_2d_matrix(m, n, start, finish)
print("Сгенерирован массив:")
print_2d_matrix(my_matrix)
