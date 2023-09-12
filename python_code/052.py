# Задача 52. Задайте двумерный массив из целых чисел.
# Найдите среднее арифметическое элементов в каждом столбце.
# Например, задан массив:
# 1 4 7 2
# 5 9 2 3
# 8 4 2 4
# Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.


from random import randint, uniform


# import sys
# sys.exit()


def arithmetic_average_column(matrix):
    print("Среднее арифметическое каждого столбца: ", end="")
    for j in range(len(matrix[0])):
        sum_column = 0
        for i in range(len(matrix)):
            sum_column = sum_column + matrix[i][j]

        print(f" {round((sum_column / 2), 2)} ", end="")
    # print("{0:0.2f}".format(matrix[i][j]), end="  ")


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
    arithmetic_average_column(my_matrix)