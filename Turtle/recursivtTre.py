import turtle

"""
    Recursive funksjoner påkaller seg selv for å kunne løse et problem som går over flere nivåer. 
    Eksempel her ved å tegne et tre. 
    Hver gang koden inne i If statementen kommer til påkalling av funksjonen på nytt går den tilbake til start
    og jobber fra det nye nivået. Når den er kommet til nivå 0, altså toppen, stopper den
    og går tilbake til opprinneling kall.
    Så du skal her se at den tar første gren helt opp, så ramler ned et nivå, jobber seg opp til begge bladene er tegnet,
    så ramle ned på et nytt nivå og gjentar prosessen.
    
"""



""" Opprett vinduet og skilpadden """
skilpadde = turtle.Turtle()
vindu = turtle.Screen()
vindu.title("Recursiv funksjon - Lag et tre")
vindu.bgcolor("black")

""" Sett hastighet for skilpadden - 0 er maks hastighet """
skilpadde.speed(0)

""" Vri skilpadden til å peke oppover """
skilpadde.rt(-90)

""" Vinkelen mellom grenene """
vinkel = 30

""" Funksjon for å plotte inn verdier for Y aksen """
def y(lengde, level):
    if level > 0:
        vindu.colormode(255)

        """ Endrer RGB range for fargen utfra hvilken level vi er på """
        skilpadde.pencolor(0, 255 // level, 0)

        """ Tegner basen """
        print("Nivå: " + str(level) + ".Tegner basen")
        skilpadde.forward(lengde)

        """ vrir ihht til satt vinkel """
        print("Nivå: " + str(level) + ".vrir ihht til satt vinkel")
        skilpadde.right(vinkel)

        """ Recursivt kall for den høyre grenen, samt går ned 20% i lengde """
        print("Nivå: " + str(level) + ".Recursivt kall for den høyre grenen")
        y(0.8 * lengde, level - 1)

        """ Setter fargen igjen """
        print("Nivå: " + str(level) + ".Setter fargen igjen")
        skilpadde.pencolor(0, 255 // level, 0)

        """ Vrir oss igjen for den andre grenen, da med * 2 på vinkel siden vi må først
            tilbake fra de 30 graderne vi har vrid oss til høyre, så skal vi 30 grader mot venstre """
        print("Nivå: " + str(level) + ".Vrir oss igjen for den andre grenen")
        skilpadde.left(2 * vinkel)

        """ Recursivt kall for å tegne den venstre grenen, samt går ned 20% i lengde """
        print("Nivå: " + str(level) + ".Recursivt kall for å tegne den venstre grenen")
        y(0.8 * lengde, level - 1)

        """ Setter farge igjen """
        print("Nivå: " + str(level) + ".Setter farge igjen")
        skilpadde.pencolor(0, 255 // level, 0)

        """ Vrir oss til høyre og går tilbake til krysset """
        print("Nivå: " + str(level) + ".Vrir oss til høyre og går tilbake til krysset")
        skilpadde.right(vinkel)
        skilpadde.forward(-lengde)


""" Setter lengde til 80px og 9 nivåer """
y(80, 9)

""" Hold vinduet åpent når funksjonen er ferdig """
vindu.mainloop()
