# Задача 8: Напишите программу, которая на вход принимает число (N),
# а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

n = abs(int(input("Введите число N: ")))
if n <= 1:
    print("Четные числа в промежутке от ", -n," до ", n, " -> 0", end = ' ')
    exit()
if n % 2 != 0:
    n -= 1

for i in range(-n, n, 2):
	print(i, end = ', ')
print(n)

