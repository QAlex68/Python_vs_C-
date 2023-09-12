# Задача 46: Задайте двумерный массив размером m×n, заполненный случайными целыми числами.
# m = 3, n = 4.
# 1 4 8 19
# 5 -2 33 -2
# 77 3 8 1
from random import randint

def print_2d_matrix ( matrix ): 
   for i in range ( len(matrix) ): 
      for j in range ( len(matrix[i]) ): 
          print ( "{:4d}".format(matrix[i][j]), end = "" )
      print ()


def create_fill_2d_matrix(m, n, start, finish):
    matrix = [[randint(start, finish) for j in range(m)] for i in range(n)]
    return matrix

m = int(input("Введите количество строк массива: "))
n = int(input("Введите количество столбцов массива: "))
start = int(input("Введите начало диапазона элементов: "))
finish = int(input("Введите конец диапазона элементов: "))
my_matrix = create_fill_2d_matrix(m, n, start, finish)
print_2d_matrix ( my_matrix )
