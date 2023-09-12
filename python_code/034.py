# Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами.
# Напишите программу, которая покажет количество чётных чисел в массиве.
# [345, 897, 568, 234] -> 2

import random


def even_numbers_count(array):
    count = 0
    for i in range(0, len(array)):
        if array[i] % 2 == 0:
            count += 1
    return count


def fill_1d_array(len, start, finish):  # длина списка, начало диапазона, конец диапазона
    array = []
    for i in range(0, len):
        array.append(random.randint(start, finish))
    print("Сгенерирован массив: ", array)
    return array


len_list = int(input("Введите количество элементов массива: "))
start = int(input("Введите начало диапазона число : "))
finish = int(input("Введите конец диапазона число: "))
my_list = fill_1d_array(len_list, start, finish)
print("Количество четных элементов в массиве: ", even_numbers_count(my_list))
