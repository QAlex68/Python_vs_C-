# Задача 49: Задайте двумерный массив. Найдите элементы, у которых оба 
#  индекса чётные, и замените эти элементы на их квадраты. 

# Например, изначально массив 
#  выглядел вот так: 
# 1 4 7 2 
# 5 9 2 3 
# 8 4 2 4 

# Новый массив будет выглядеть  
# вот так: 
# 1 4 7 2 
# 5 81 2 9 
# 8 4 2 4 

from random import randint


def replace_2d_matrix(matrix):
    for i in range(0, len(matrix), 2):
        for j in range(0, len(matrix[i]), 2):
            matrix[i][j] = matrix[i][j] * matrix[i][j]
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
print_2d_matrix(my_matrix)
new_matrix = replace_2d_matrix(my_matrix)
print()
print_2d_matrix(new_matrix)