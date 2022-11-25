def inngangTillatt(alder):
    grense = 18

    if alder < grense:
        inngang = 'Nei'
    elif alder >= grense:
        inngang = 'Ja'
    else:
        print('Ugyldig alder')
    # Feilen er at vi ba programmet om å skrive ut svaret. Men siden vi skal benytte
    # resultatet av funksjonen må resultatet returneres, ikke printes.
    #print(inngang)
    return inngang


person1 = inngangTillatt(23)

print('Vurderingen av om du kommer inn er:', person1)