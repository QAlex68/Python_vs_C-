# Задача 53: Задайте двумерный массив. Напишите программу,
# которая поменяет местами первую и последнюю строку массива.


from random import randint, uniform


# import sys
# sys.exit()


def swap_first_last_rows(matrix):
    print("Массив с заменой первой и последней строки: ")
    i = 0
    for j in range(0, len(matrix)):
        temp = matrix[i][j]
        matrix[i][j] = matrix[len(matrix) - 1][j]
        matrix[len(matrix) - 1][j] = temp
    print_2d_matrix(matrix)


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
    swap_first_last_rows(my_matrix)