# Задача 29: Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.
# 1, 2, 5, 7, 19 -> [1, 2, 5, 7, 19]
# 6, 1, 33 -> [6, 1, 33]
# Задачу не совсем понял!
# Вариант 1 создает массив случайных чисел из указанного количества элементов и выводит на консоль

import random

def fill_1d_array(len, start, finish): # длина списка, начало диапазона, конец диапазона
    array =  []   
    for i in range(0,len): 
        array.append(random.randint(start, finish))       
    return array

len_list = int(input("ВведИте количество элементов массива: "))
start = int(input("Введите начало диапазона число : "))
finish = int(input("Введите конец диапазона число: "))
print(fill_1d_array(len_list, start, finish))