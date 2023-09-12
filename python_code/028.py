# Задача 28: Напишите программу, которая принимает на вход число N и выдаёт произведение  
# чисел от 1 до N. 
# 4 -> 24  
# 5 -> 120 

def product_of_numbers(limit):
    product = 1
    for i in range(1, limit+1):
        product = product * i
    return product


x = abs(int(input("Введите число N: ")))
print("Произведение всех чисел от 1 до ", x, " = ", product_of_numbers(x))