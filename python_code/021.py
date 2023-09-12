## Задача 21
## Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 3D пространстве.
## A (3,6,8); B (2,1,-7), -> 15.84   
## A (7,-5, 0); B (1,-1,9) -> 11.53
#  round (2.137, 2)  = 2.14

import math

def distans_3d(ax, ay, az, bx, by, bz):
    distans = math.sqrt(math.pow(bx - ax, 2) + math.pow(by - ay, 2) + math.pow(bz - az, 2))
    print("Расстояние между двумя точками ",ax,ay,az," и ",bx, by,bz," в 3D пространстве: ", round(distans,2))

ax = int(input("Введите координату Х точки А: "))
ay = int(input("Введите координату Y точки А: "))
az = int(input("Введите координату Z точки А: "))
bx = int(input("Введите координату Х точки B: "))
by = int(input("Введите координату Y точки B: "))
bz = int(input("Введите координату Z точки B: "))

distans_3d(ax, ay, az, bx, by, bz)