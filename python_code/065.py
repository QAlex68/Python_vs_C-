# Задача 65: Задайте значения M и N. Напишите программу, которая выведет все натуральные
# числа в промежутке от M до N.
# M = 1; N = 5 -> "1, 2, 3, 4, 5"
# M = 4; N = 8 -> "4, 6, 7, 8"

def print_natural_numbers_between(m, n):
    if m <= n:
        print(m, end=" ")
        print_natural_numbers_between(m + 1, n)

m = int(input("Введите натуральное число m: "))
n = int(input("Введите натуральное число n: "))
print_natural_numbers_between(m, n)