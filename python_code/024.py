# Задача 24: Напишите программу, которая принимает на вход число (А) и выдаёт сумму чисел от 1 до А.
# 7 -> 28
# 4 -> 10
# 8 -> 36

def get_sum(limit):
    summa = 0
    for i in range(1, limit+1):
        summa += i
    return summa


x = abs(int(input("Введите число A: ")))
print("Сумма всех чисел от 1 до ", x, " = ", get_sum(x))