#Задача 32. Напишите программу замены элементов массива,
#положительные числа замените на отрицательные и наоборот.

import random

def number_sign_change(array):
    for i in range(0, len(array)):
        if array[i] > 0:
            array[i] = - array[i]                
        else:
            array[i] = abs(array[i])       
    return array

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
print("Замена знаков элементов массива на обратный:")
print(number_sign_change(my_list))