# Задача 23
# Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
# 3 -> 1, 8, 27  
# 5 -> 1, 8, 27, 64, 125

import math

def number_output(n):
    print("Кубы чисел в промежутке от 0 до ", n, ": -> ", end= ' ')
    if n == 0:
         print(n)
    if n > 0:
        for i in range(0,n):
            print(round(math.pow(i, 3)), end =', ')
        print(round(math.pow(i+1, 3)))

    if n < 0:
        for i in range(n,0):        
            print(round(math.pow(i, 3)), end =', ')        
        print("0")
    
n = int(input("Введите число N: "))
number_output(n)