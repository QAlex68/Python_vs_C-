# Задача 39: Напишите программу, которая перевернёт одномерный массив
# (последний элемент будет на первом месте, а первый - на последнем и т.д.)
# [1 2 3 4 5] -> [5 4 3 2 1]
# [6 7 3 6] -> [6 3 7 6]

import random

def reverse_list_in_place(lst):
    length = len(lst)
    for i in range(length // 2):
        lst[i], lst[length - i - 1] = lst[length - i - 1], lst[i]
    print("Перевернутый массив -> ", lst)

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
reverse_list_in_place(my_list)