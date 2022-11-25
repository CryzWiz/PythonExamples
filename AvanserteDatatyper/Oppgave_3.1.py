"""
Analyse av værdata

Under har du en dictionary med fiktive data fra været den siste måneden i Trondheim. Dict'en består av følgende: dato (key), og values som er en liste der første element er gj.snittlig mm regn pr døgn (regn_dag), andre er gj.snittlig grader celcius for hvert døgn (temp_dag), og tredje er gj.snittlig vindstyrke m/s pr døgn (vind_dag). Skriv et program som tar inn denne informasjonen, og ved hjelp av funksjoner deretter finner:

* Den uka med mest regn i gjennomsnitt
* Døgnet med lavest temperatur
* Den høyeste vindstyrken som ble målt

"""

trondheim_vaer = {1: [8, 25, 8],
 2: [31, 10, 5],
 3: [19, 23, 3],
 4: [4, 20, 2],
 5: [9, 24, 4],
 6: [10, 20, 8],
 7: [40, 22, 8],
 8: [35, 22, 8],
 9: [10, 15, 2],
 10: [8, 16, 10],
 11: [17, 25, 7],
 12: [6, 14, 7],
 13: [35, 25, 5],
 14: [31, 24, 1],
 15: [29, 16, 8],
 16: [30, 21, 6],
 17: [13, 20, 6],
 18: [34, 25, 0],
 19: [37, 11, 2],
 20: [0, 22, 4],
 21: [32, 22, 5],
 22: [20, 13, 0],
 23: [23, 17, 15],
 24: [8, 12, 1],
 25: [27, 20, 0],
 26: [34, 20, 4],
 27: [4, 24, 3],
 28: [22, 15, 1],
 29: [38, 23, 8],
 30: [29, 21, 3],
 31: [26, 13, 10]}

temp_regn = 0
vinner_regn = list((0, 1))
vinner_temp = list((0, 50))
vinner_vind = list((0, 1))
for i in range(len(trondheim_vaer)):
    week = (i + 1) / 7
    # Vi starter med regn, gjenn.snitt pr uke.
    if (i + 1) % 7 == 0:
        if temp_regn > vinner_regn[0]:
            vinner_regn = list((temp_regn / 7, week))

        temp_regn = 0
    else:
        temp_regn += trondheim_vaer[i+1][0]
    # Finner høyeste temperatur
    if trondheim_vaer[i+1][1] < vinner_temp[1]:
        vinner_temp = list((i + 1, trondheim_vaer[i+1][1]))
    # Finner høyeste vindstyrke
    if trondheim_vaer[i+1][2] > vinner_vind[1]:
        vinner_vind = list((i + 1, trondheim_vaer[i+1][2]))

print("Uken med mest regn er uke {0} med {1} gj.snittlig mm regn pr døgn (regn_dag)".format(str(vinner_regn[1]), str(vinner_regn[0])))
print("Dagen med lavest temperatur er dag {0} med {1} gj.snittlig grader celcius".format(str(vinner_temp[0]), str(vinner_temp[1])))
print("Dagen med høyeste vindstyrke er dag {0} med {1} m/s".format(str(vinner_vind[0]), str(vinner_vind[1])))