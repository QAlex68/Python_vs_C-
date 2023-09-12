# Задача 35: Задайте массив из 123 случайных числел и найдите количество элементов массива
# которые лежат в диапазоне от 10 до 99.


import random

def range_element_count(array, begin, end):
    count = 0
    for i in range(0, len(array)):
        if array[i] >= begin and array[i] <= end:
            count += 1             
    return count

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
begin = int(input("Введите диапазона проверки: "))
end = int(input("Введите конец диапазона проверки: "))
print("Количество элементов в диапазоне <", begin, ", ", end, "> = ", range_element_count(my_list, begin, end))