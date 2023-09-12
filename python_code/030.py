# Задача 30: Напишите программу, которая выводит массив из 8 элементов,
# заполненный нулями и единицами в случайном порядке.
# [1,0,1,1,0,1,0,0]

import random

def fill_1d_array(len, start, finish): # длина списка, начало диапазона, конец диапазона
    array =  []   
    for i in range(0,len): 
        array.append(random.randint(start, finish))       
    return array
 
print(fill_1d_array(8, 0, 1))
