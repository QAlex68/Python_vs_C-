# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09 
# A (7,-5); B (1,-1) -> 7,21
import math

def distans_2d(ax, ay,bx, by):
    distans = math.sqrt(math.pow(ax-bx, 2)+ math.pow(ay-by , 2))
    print("Расстояние между двух точек: ", round(distans,2))

ax = int(input("Введите число X: "))
ay = int(input("Введите число Y: "))
bx = int(input("Введите число X: "))
by = int(input("Введите число Y: "))

distans_2d(ax, ay, bx, by)