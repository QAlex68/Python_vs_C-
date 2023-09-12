# Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит
# по убыванию элементы каждой строки двумерного массива.
# Например, задан массив:
# 1 4 7 2
# 5 9 2 3
# 8 4 2 4
# В итоге получается вот такой массив:
# 7 4 2 1
# 9 5 3 2
# 8 4 4 2

from random import randint, uniform


# import sys
# sys.exit()


def sort_rows_descending(matrix):
    # Сортируем каждую строку в матрице по убыванию с применением
    # sort с параметром reverse = True
    # for row in matrix:
    #     row.sort(reverse=True)
    # В виде циклов
    for row in matrix:
        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                if row[i] < row[j]:
                    row[i], row[j] = row[j], row[i]
    return matrix

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
    print("Массив с сортировкой строк по убыванию: ")
    print_2d_matrix(sort_rows_descending(my_matrix))