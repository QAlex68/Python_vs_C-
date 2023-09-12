# Задача 33. Напишите программу присутствует ли заданное число в массиве.

import random

def is_seek_number_list(array, number):
    is_seek = False
    for i in range(0, len(array)):
        if array[i] == number:
            is_seek = True             
    return is_seek

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
number = int(input("Введите число для проверки: "))
if is_seek_number_list(my_list, number):
    print("Число ", number, " присутствует среди элементов массива!")
else:
    print("Число ", number, " отсутсвует среди элементов массива!")