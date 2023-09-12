# Задача 60. ...Сформируйте трёхмерный массив из неповторяющихся двузначных чисел.
# Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
# Массив размером 2 x 2 x 2
# 66(0,0,0) 25(0,1,0)
# 34(1,0,0) 41(1,1,0)
# 27(0,0,1) 90(0,1,1)
# 26(1,0,1) 55(1,1,1)

import random


def create_unique_3d_array(x, y, z):
    num_range = list(range(10, 100))  # Создаем список двузначных чисел
    random.shuffle(num_range)  # Перемешиваем список, чтобы числа были в случайном порядке

    num_iter = iter(num_range)
    unique_numbers = set()
    array = [[[0] * y for _ in range(x)] for _ in range(z)]

    for i in range(z):
        for j in range(x):
            for k in range(y):
                num = next(num_iter)
                while num in unique_numbers:
                    num = next(num_iter)
                array[i][j][k] = num
                unique_numbers.add(num)

    return array


def print_3d_array(array):
    for i, matrix in enumerate(array):
        print(f"Матрица {i}:")
        for j, row in enumerate(matrix):
            for k, value in enumerate(row):
                print(f"{value}({i},{j},{k})", end=" ")
            print()
        print()


x = int(input("Введите количество строк массива: "))
y = int(input("Введите количество столбцов массива: "))
z = int(input("Введите глубину массива: "))
if x * y * z > 90:
    print("Количество элементов 3D матрицы > 90!!")
else:
    array_3d = create_unique_3d_array(x, y, z)
    print("Сгенерирован массив 3D массив и заполнен двухзначными неповторяющимися  числами:")
    print_3d_array(array_3d)
