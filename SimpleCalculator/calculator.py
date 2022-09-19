# simpel kalkulator

# Ta imot 2 variabler og returner de sammenlagt
def LeggSammen(variabel1, variabel2):
    return (variabel1 + variabel2)
# Ta imot 2 variabler og retuner de trukket fra hverandre
def TrekkFra(variabel1, variabel2):
    return (variabel1 - variabel2)
# Ta imot 2 variabler og returner de multiplisert med hverandre
def Multipliser(variabel1, variabel2):
    return (variabel1 * variabel2)
# Ta imot 2 variabler og returner de dividert med hverandre
def Divider(variabel1, variabel2):
    return (variabel1 / variabel2)

def Kalkuler(Valg, variabel1, variabel2):
   # Utfør et regnestykke basert på hva brukeren ønsker skal gjøres
    if Valg == 1:
        # print ut resultatet av funksjonen LeggSammen() og send inn variabel1 og variabel2
        print(f'Svaret er: {LeggSammen(variabel1,variabel2)}')
    elif Valg == 2:
        # print ut resultatet av funksjonen TrekkFra() og send inn variabel1 og variabel2
        print(f'Svaret er: {TrekkFra(variabel1,variabel2)}')
    elif Valg == 3:
        # print ut resultatet  av funksjonen Multipliser() og send inn variabel1 og variabel2
        print(f'Svaret er: {Multipliser(variabel1,variabel2)}')
    elif Valg == 4:
        # print ut resultatet av funksjonen Divider() og send inn variabel1 og variabel2
        print(f'Svaret er: {Divider(variabel1,variabel2)}')


def Stopp():
    # Setter running til False slik at while-løkke stopper opp
    global running
    running = False

# Setter en variabel for om vi kjører programmet eller ikke til sann(True)
running = True

# Starter en while-løkke som skal kjøre helt til varibelen running ikke er sann lengre (True)
while running:
    """ Så lenge running er SANN(True) skal han utføre det som er kodet under. Når alle kodelinjene under er utført skal han komme
    tilbake til dette punktet, sjekke om running er SANN(True) og kjøre alle kodelinjene på nytt så sant running er SANN(True) """

    # Print en linje med hva som er mulig til informasjon
    print("1: Legg sammen, 2: Trekk fra, 3: Multipliser, 4: Divider, 5: Avslutt")

    # Spør brukeren om hva som er ønskelig og sett svaret i en variabel "Valg"
    # Her benytter vi int(input("tekst tekst")) siden vi ikke ønsker desimaltall på valget fra brukeren. Heltall holder
    Valg = int(input("Hva ønsker du å gjøre? "))

    if Valg == 5:
        Stopp()
    else:
        # Hent inn tallene som bruker ønsker å regne sammen
        variabel1 = float(input("Skriv inn tall nummer 1: "))
        variabel2 = float(input("Skriv inn tall nummer 2: "))
        Kalkuler(Valg, variabel1, variabel2)


# Printer ut en hilsning og bekreftelse på at programmet er avsluttet.
print("Takk for at du testet meg. Program avsluttet.")
