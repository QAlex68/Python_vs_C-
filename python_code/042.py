#  Задача 42: Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  45 -> 101101
#  3  -> 11
#  2  -> 10
# функция bin() строка
n = int(input("Введите число N: "))
nn = n
print("Числo ", n, " в двоичном формате - ", bin(n))
# ручной перевод строка
binary = ""
while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n = n // 2
print(binary)
# функция format() строка
decimal_num = nn
binary_num = format(decimal_num, 'b')
print(binary_num)  # '11001'