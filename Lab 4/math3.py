import math

sides = float(input())
lenght = float(input())

apothem = lenght / 2 * math.tan(math.pi/sides)

s = apothem * sides*lenght / 2
print(math.ceil(s))