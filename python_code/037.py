# Задача 37: Найдите произведение пар в одномерном массиве парой считается,
# первый и последний элемент, второй и предпоследний и т.д. результат запишите в отдельном массиве.

import random

def element_product(array):
    arrayw = []
    for i in range (0, len(array) // 2):    
        arrayw.append(array[i]*array[len(array)-i-1])  
    return arrayw

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
print("Произведение пар крайних элементов: ", element_product(my_list))
