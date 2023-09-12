# Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму
# натуральных элементов в промежутке от M до N.
# M = 1; N = 15 -> 120
# M = 4; N = 8. -> 30

def sum_of_natural_numbers(m, n):
    if m > n:
        return 0
    else:
        return m + sum_of_natural_numbers(m + 1, n)


m = int(input("Введите натуральное число N: "))
n = int(input("Введите натуральное число N: "))
print(sum_of_natural_numbers(m, n))
