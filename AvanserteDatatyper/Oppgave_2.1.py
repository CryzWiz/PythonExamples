"""a) I øving 2 hjalp du en entomolog å skrive et program for å registrere antall målinger han hadde gjort av larver.
Nå ønsker han at du utvider programmet for å også registrere målingene i en liste. Ta inn målingene én og én,
og legg dem til i en liste helt til du har 15 stk. Print listen ut til konsoll."""

print("La oss utføre noen målinger!")

# Antall målinger vi ønsker å foreta
ant_maalinger = input("Hvor mange målinger:")
# Listen vår
registrerte_maalinger = list()

# Hvis brukers input er et tall
if str.isdigit(ant_maalinger):
    # For hver måling vi ønsker å ta
    for m in range(int(ant_maalinger)):
        # Spør etter mål og legg det til listen vår
        registrerte_maalinger.append(int(input("Hvor lang er orm {0}: ".format(m+1))))
# Brukeren skrev ikke inn et tall
else:
    print("Feil! Du må skrive inn et tall.")

print("----------------------------------------")

# Innhenting gjort - og vi printer ut innsamlede data
for i in range(len(registrerte_maalinger)):
    print("Orm {0} er {1} cm lang".format(i+1, registrerte_maalinger[i]))

"""b) Skriv en funksjon som analyserer målingene som er gjort: regn ut og print gjennomsnittet av målingene, 
samt standardavvik. Til dette kan du bruke innebygde funksjoner fra biblioteker som *math* eller *numpy*. """
# Benytter numpy
import numpy
print("----------------------------------------")
print("Resultat for målingen")
print("Gjennomsnitt: {0} cm".format(round(numpy.average(registrerte_maalinger), 2)))
print("Standardavvik: {0} cm".format(numpy.std(registrerte_maalinger)))
