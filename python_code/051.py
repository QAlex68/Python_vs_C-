# Задача 51: Задайте двумерный массив. Найдите сумму элементов, находящихся 
#  на главной диагонали (с индексами (0,0); (1;1) и т.д. 
# Например, задан массив: 
# 1 4 7 2 
# 5 9 2 3 
# 8 4 2 4 
# Сумма элементов главной диагонали: 1+9+2 = 12
import random
from random import randint, uniform


def sum_2d_matrix(matrix):
    sum_elements = 0
    for i in range(len(matrix)):
        sum_elements = sum_elements + matrix[i][i]
    return sum_elements


def print_2d_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()


def create_fill_2d_matrix(m, n, start, finish):
    matrix = [[randint(start, finish) for j in range(m)] for i in range(n)]
    return matrix


m = int(input("Введите количество строк массива: "))
n = int(input("Введите количество столбцов массива: "))
if m == n:
    start = int(input("Введите начало диапазона элементов: "))
    finish = int(input("Введите конец диапазона элементов: "))
    my_matrix = create_fill_2d_matrix(m, n, start, finish)
    print_2d_matrix(my_matrix)
    sum_elements = sum_2d_matrix(my_matrix)
    print()
    print("Сумма элементов диагонали =", sum_elements)
else:
    print("Диагонали не существует!")