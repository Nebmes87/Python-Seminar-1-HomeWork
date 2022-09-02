# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xA = int(input('Введите координату x точки А: '))
yA = int(input('Введите координату y точки А: '))
xB = int(input('Введите координату x точки B: '))
yB = int(input('Введите координату y точки B: '))

distance = ((xA - xB)*(xA - xB) + (yA - yB)*(yA - yB)) ** 0.5
distance = round(distance, 3)
print(f'Расстояние между точками А и B = {distance}')