# Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
# 452 -> 11
# 82 -> 10
# 9012 -> 12

def sum_digit(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum

n = int(input("Введите число N: "))
print("Сумма цифр в числе ", n, " = ",sum_digit(n))