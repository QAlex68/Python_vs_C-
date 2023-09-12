# Задача 59: Задайте двумерный массив из целых чисел. Напишите программу, которая удалит строку и столбец, на пересечении которых расположен наименьший элемент массива.
# Например, задан массив:
# 1 4 7 2
# 5 9 2 3
# 8 4 2 4
# 5 2 6 7
# Наименьший элемент - 1, на выходе получим 
# следующий массив:
# 9 4 2
# 2 2 6
# 3 4 7

from random import randint, uniform


# import sys
# sys.exit()


def find_and_delete(matrix):
    del_row = 0
    del_col = 0
    min_element = matrix[0][0]
    # Поиск минимального элемента
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if min_element > matrix[i][j]:
                min_element = matrix[i][j]
                del_row = i
                del_col = j
    # Собираем новую матрицу (двухмерный список) из срезов до и от ненужных нам строк и столбцов
    new_matrix = [
        row[:del_col] + row[del_col + 1:]
        for row in matrix[:del_row] + matrix[del_row + 1:]
    ]
    print(f"Новая матрица без строки {del_row} и столбца {del_col}:")
    print_2d_matrix(new_matrix)


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
    find_and_delete(my_matrix)
