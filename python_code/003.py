# Задача №3. Напишите программу, которая будет выдавать название дня недели по заданному номеру.
# 3 -> Среда 
# 5 -> Пятница

day = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
numberDay = int(input("Введите номер дня недели: "))

if numberDay < 1 or numberDay > 7:
    print("В неделе 7 дней!!")
    exit()

if numberDay == 1:
    print("Сегодня ", day[numberDay -1], " !!")
if numberDay == 2:
    print("Сегодня ", day[numberDay -1], " !!")
if numberDay == 3:
    print("Сегодня ", day[numberDay -1], " !!")
if numberDay == 4:
    print("Сегодня ", day[numberDay -1], " !!")
if numberDay == 5:
    print("Сегодня развратница ", day[numberDay -1], " !!")
if numberDay == 6:
    print("Сегодня ", day[numberDay -1], " !!")
if numberDay == 7:
    print("Ура сегодня ", day[numberDay -1], " !!")



