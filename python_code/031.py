# Задача 31: Задайте массив из 12 элементов, заполненный
#случайными числами из промежутка [-9, 9].
#Найдите сумму отрицательных и положительных элементов массива.
# Например, в массиве [3,9,-8,1,0,-7,2,-1,8,-3,-1,6]
#сумма положительных чисел равна 29, сумма отрицательных равна -20.

import random

def sum_plus_or_minus_digit(array, is_positive):
    sum = 0
    for i in range(0, len(array)):
        if (is_positive):
            if array[i] > 0:
                sum += array[i]        
        else:
            if array[i] < 0:
                sum += array[i]        
    return sum

def fill_1d_array(len, start, finish): # длина списка, начало диапазона, конец диапазона
    array =  []   
    for i in range(0,len): 
        array.append(random.randint(start, finish))
    print("Сгенерирован массив: ", array)       
    return array

len_list = int(input("ВведИте количество элементов массива: "))
start = int(input("Введите начало диапазона число : "))
finish = int(input("Введите конец диапазона число: "))
my_list = fill_1d_array(len_list, start, finish)
print("Cумма положительных чисел равна: ", sum_plus_or_minus_digit(my_list, True))
print("Cумма отрицательных чисел равна: ", sum_plus_or_minus_digit(my_list, False))