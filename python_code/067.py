# Задача 67: Напишите программу, которая будет принимать на вход число и возвращать сумму его цифр.
# 453 -> 12
# 45 -> 9

def get_sum_digit(number):
    if (number == 0):
        return number
    return number % 10 + get_sum_digit(number / 10)


number = int(input("Введите число N:"))
print(f"{number} -> {int(get_sum_digit(number))}")
