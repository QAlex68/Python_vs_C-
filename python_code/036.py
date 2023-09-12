# Задача 36: Задайте одномерный массив, заполненный случайными числами.
# Найдите сумму элементов, стоящих на нечётных позициях.
# [3, 7, 23, 12] -> 19
# [-4, -6, 89, 6] -> 0
# Задача решена для чисел с нечетными индексами как в условии!!

import random

def sum_odd_index_numbers(array):
    sum = 0
    for i in range(1, len(array), 2):
        sum = sum + array[i]            
    return sum

def fill_1d_array(len, start, finish): # длина списка, начало диапазона, конец диапазона
    array =  []   
    for i in range(0,len): 
        array.append(random.randint(start, finish))
    print("Сгенерирован массив: ", array)       
    return array

len_list = int(input("Введите количество элементов массива: "))
start = int(input("Введите начало диапазона число : "))
finish = int(input("Введите конец диапазона число: "))
my_list = fill_1d_array(len_list, start, finish)
print("Сумма элементов с нечетными индексами = ", sum_odd_index_numbers(my_list))