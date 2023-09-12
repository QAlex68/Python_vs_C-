# Задача 57: Составить частотный словарь элементов двумерного массива.
# Частотный словарь содержит информацию о том, сколько раз встречается элемент входных данных.
# { 1, 9, 9, 0, 2, 8, 0, 9 }
# 0 встречается 2 раза 
# 1 встречается 1 раз 
# 2 встречается 1 раз 
# 8 встречается 1 раз 
# 9 встречается 3 раза
# 1, 2, 3 
# 4, 6, 1 
# 2, 1, 6
# 1 встречается 3 раза 
# 2 встречается 2 раз 
# 3 встречается 1 раз 
# 4 встречается 1 раз 
# 6 встречается 2 раза

from random import randint, uniform


# import sys
# sys.exit()


def seek_and_count_digit(matrix, start, finish):
    number = start
    count = 0
    while (number <= finish):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if number == matrix[i][j]:
                    count += 1
        if number != 0:
            print(f"Число {number} встречается в массиве {count} раз!")
        number += 1
        count = 0


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
    seek_and_count_digit(my_matrix, start, finish)
