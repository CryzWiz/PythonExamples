import math

height = float(input('Høyden av sylinderen: '))
radian = float(input('Radius av sylinderen: '))

volume = math.pi * radian * radian * height
sur_area = ((2 * math.pi * radian) * height) + ((math.pi * radian ** 2) * 2)

print("Volum: ", volume)
print("Overflateareal: ", sur_area)
