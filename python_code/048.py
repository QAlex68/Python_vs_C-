# Задача 48: Задайте двумерный массив размера m на n, каждый элемент в массиве
# находится по формуле: Aₘₙ = i+j. Выведите полученный массив на экран.
# m = 3, n = 4.
# 0 1 2 3
# 1 2 3 4
# 2 3 4 5


from random import randint

def print_2d_matrix ( matrix ): 
   for i in range ( len(matrix) ): 
      for j in range ( len(matrix[i]) ): 
          print ( "{:4d}".format(matrix[i][j]), end = "" )
      print ()

def create_fill_2d_matrix(m, n):
    matrix = [[i + j for j in range(n)] for i in range(m)]
    return matrix

# def create_fill_2d_matrix(m, n, start, finish):
#     matrix = [[randint(start, finish) for j in range(m)] for i in range(n)]
#     return matrix

m = int(input("Введите количество строк массива: "))
n = int(input("Введите количество столбцов массива: "))
my_matrix = create_fill_2d_matrix(m, n)
print_2d_matrix ( my_matrix )