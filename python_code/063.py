# Задача 63: Задайте значение N. Напишите программу, которая выведет все натуральные
# числа в промежутке от 1 до N.
# N = 5 -> "1, 2, 3, 4, 5"
# N = 6 -> "1, 2, 3, 4, 5, 6"

def print_natural_numbers(n):
    if n > 0:
        print_natural_numbers(n - 1)
        print(n, end=" ")

n = int(input("Введите натуральное число N: "))
print_natural_numbers(n)

