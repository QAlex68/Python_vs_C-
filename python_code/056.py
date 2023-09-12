# Задача 56: Задайте прямоугольный двумерный массив.
# Напишите программу, которая будет находить строку с наименьшей суммой элементов.
# Например, задан массив:
# 1 4 7 2
# 5 9 2 3
# 8 4 2 4
# 5 2 6 7
# Программа считает сумму элементов в каждой строке и выдаёт номер строки
# с наименьшей суммой элементов: 1 строка

from random import randint, uniform


# import sys
# sys.exit()


def row_with_smallest_sum(matrix):
    sum_min = sum(matrix[0])
    sum_row = sum_min
    num_row = 0
    for i in range(1, len(matrix)):
        sum_row = sum(matrix[i])
        if sum_min > sum_row:
            sum_min = sum_row
            num_row = i
    print(f"Номер строки с наименьшей суммой элементов {num_row}, сумма = {sum_min}")



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
start = int(input("Введите начало диапазона элементов: "))
finish = int(input("Введите конец диапазона элементов: "))
my_matrix = create_fill_2d_matrix(m, n, start, finish)
print("Сгенерирован массив:")
print_2d_matrix(my_matrix)
if m == 0 or n == 0:
    print("Массив пуст!!")
else:
    row_with_smallest_sum(my_matrix)