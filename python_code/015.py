# Задача 15: Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# 6 -> да
# 7 -> да
# 1 -> нет

day = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
numberDay = int(input("Введите номер дня недели: "))

if numberDay < 1 or numberDay > 7:
    print("В неделе 7 дней!!")
    exit()

if numberDay == 1:
    print("Сегодня ", day[numberDay -1], " - день тяжелый!!")
if numberDay == 2:
    print("Сегодня ", day[numberDay -1], " - разбег!!")
if numberDay == 3:
    print("Сегодня ", day[numberDay -1], " - взлет!!")
if numberDay == 4:
    print("Сегодня ", day[numberDay -1], " - пора приземляться!!")
if numberDay == 5:
    print("Сегодня развратница ", day[numberDay -1], " - работай, негр, солнце еще высоко!!")
if numberDay == 6:
    print("Сегодня ", day[numberDay -1], " - Выходной день!!")
if numberDay == 7:
    print("Ура сегодня ", day[numberDay -1], " - Выходной день!!")