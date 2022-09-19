import math

"""
    Beregner reel temperatur du utsettes for mtp vind og lufttemperatur.

    Benytter følgende formel: https://www.weather.gov/media/epz/wxcalc/windChill.pdf

    Ikke kontrollsjekket.

"""

#
v = float(input("Vindhastighet m/s: ")) * 3600 / 1000
t = float(input("Lufttemperatur i Celcius: "))

realfeel = 13.12 + 0.6215 * t - 11.37 * math.pow(v, 0.16) + 0.3965 * t * math.pow(v, 0.16)

print("Realfeel temperatur vil da være: ", float(round(realfeel, 2)))