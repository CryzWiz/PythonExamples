from math import radians, sin, cos, acos

"""
    Beregner lengden mellom 2 punkter gitt i lengde og breddegrad. 

    Eksemplet beregner fra krysset til inn mot trollvik og til krysset inn mot gressmyra. Altså brua.

    Start: 69.2387515258355, 17.979929292871635
    Stopp: 69.24498956877933, 17.952011220933255

    Benytter Haversine formel.

"""

print("Legg inn koordinatene for 2 punkter du vil se avstand for:")

startlat = radians(float(input("Breddegrad start: ")))
startlon = radians(float(input("Lengdegrad start: ")))
endlat = radians(float(input("Breddegrad slutt: ")))
endlon = radians(float(input("Lengdegrad slutt: ")))

dist = 6371.01 * acos(sin(startlat)*sin(endlat) + cos(startlat)*cos(endlat)*cos(startlon - endlon))
print("Avstanden er %.2f km." % dist)
