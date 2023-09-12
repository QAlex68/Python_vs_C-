# Задача 10: Напишите программу, которая выводит случайное трехзначное число и
# удаляет вторую цифру этого числа.
# 456 -> 46
# 782 -> 72
# 918 -> 98

import random

number = random.randint(100, 999)
firstDigit = number // 100
secondDigit = number % 10
print("Сгенерировано целое число ", number," удаляем среднюю цифру -> ",firstDigit,secondDigit)