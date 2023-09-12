# Задача 69: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def get_power(number, power):
    if power > 1:
        return number * get_power(number, power - 1)
    return number


number = int(input("Введите число A:"))
power = int(input("Введите число N:"))
print(get_power(number, power))
