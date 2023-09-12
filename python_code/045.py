# Задача 45: Напишите программу, которая будет создавать 
# копию заданного массива с помощью поэлементного копирования.

import random

def list_copy(lst):
    lst_copy = []
    for i in range(0, len(lst)):
        lst_copy.append(lst[i])
    return lst_copy
   
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
print("Копия новый массив: ", list_copy(my_list))