# Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным
# и минимальным элементов массива.
# [3.22, 4.2, 1.15, 77.15, 65.2] => 77.15 - 1.15 = 76
# Ограничение двух цифр после запятой  Console.Write(num.ToString("F2") + " ");

import random

def max_min_difference(array):
    min = array[0]
    max = array[0]
    for i in range (0, len(array)):
        if array[i] < min:
            min = array[i]
        if array[i] > max:
            max = array[i]
    print("Разность между ", max, " и ", min, " = ", round(max - min,2))        

def fill_1d_array_float(len, start, finish): # длина списка, начало диапазона, конец диапазона
    array =  []   
    for i in range(0,len): 
        array.append(round(random.uniform(start, finish),2))
    print("Сгенерирован массив вещественных чисел: ", array)       
    return array

len_list = int(input("Введите количество элементов массива: "))
start = int(input("Введите начало диапазона число : "))
finish = int(input("Введите конец диапазона число: "))
my_list = fill_1d_array_float(len_list, start, finish)
max_min_difference(my_list)
#print("Произведение пар крайних элементов: ", element_product(my_list))