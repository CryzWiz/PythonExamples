"""
I denne oppgaven skal du ved hjelp av en nøstet liste liste printe ut den lille gangetabellen (1-10) til konsoll.

"""

# hovedlisten vår
hovedliste = list()
# generer en ny liste med 1-10 tall i seg og legg denne til hovedlisten. Liste i liste.
for i in range(10):
    for s in range(10):
        innerliste = list((i + 1, s + 1))
        hovedliste.append(innerliste)

# for lengden av listen, hent ut tallet i den nøstede listen og gang det med 10. Print resultatet.
for i in range(len(hovedliste)):
        print("{0} * {1} er {2}".format(hovedliste[i][0], hovedliste[i][1], hovedliste[i][0] * hovedliste[i][1]))
