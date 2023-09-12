# Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве,
# и возвращает значение этого элемента или же указание, что такого элемента нет.
# Например, задан массив:
# 1 4 7 2
# 5 9 2 3
# 8 4 2 4
# 17 -> такого числа в массиве нет
# с условием долго спорили, сделана еще проверка на наличие числа

from random import randint


def seek_number(massive, number):
    count = 0
    for i in range(len(massive)):
        for j in range(len(massive[i])):
            if number == massive[i][j]:
                count += 1
    if count == 0:
        print(f"Число {number} в массиве ОТСУТСТВУЕТ!")
    else:
        print(f"Число {number} в массиве ПРИСУТСТВУЕТ в количестве - {count} !")


def seek_element(massive, row, column):
    if row >= len(massive) and column >= len(massive[0]):
        print(f"Элемент с номером строки {row} и номером столбца {column} ОТСУТСТВУЕТ!")
    else:
        print(f"Элемент с номером строки {row} и номером столбца {column} = {massive[row][column]} !")


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
print(len(my_matrix))
print(len(my_matrix[0]))
row = int(input("Введите номер строки элемента: "))
column = int(input("Введите номер столбца элемента: "))
seek_element(my_matrix, row, column)
digit = int(input("Введите число для проверки наличия в массиве: "))
seek_number(my_matrix, digit)

