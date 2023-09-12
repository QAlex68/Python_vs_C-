# Задача 2: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.
# a = 5; b = 7->max = 7
# a = 2 b = 10->max = 10
# a = -9 b = -3->max = -3

number1 = int(input("Введите число N: "))
number2 = int(input("Введите число M: "))
if number1 > number2:
    print("Число ", number1, " больше числа ", number2 , "!!")
if number1 < number2:
    print("Число ", number1, " меньше числа ", number2 , "!!")
if number1 == number2:
    print("Число ", number1, " равно числу ", number2 , "!!")
