﻿"""
Skriv et program som tar inn Trontalen for 2021, gjengitt under, som én lang string-variabel, og utfør følgende analyse:

* Tell antall ord i teksten og print antallet ut til konsoll
* Tell antall setninger i teksten og print antallet ut til konsoll
* Beregn gjennomsnittlig antall ord i hver setning og print til konsoll
* Tell hvor mange ganger hver bokstav i alfabetet forekommer i teksten, og skriv en sortert liste som går fra høyest til lavest til konsoll.

"""


tekst = "Ærede President, Folkets representanter. Jeg hilser Stortinget velkommen til ansvarsfullt arbeid og ønsker at " \
        "det må bli til gagn for fedrelandet. Etter halvannet år har koronaviruset løsnet sitt grep om vår hverdag. " \
        "Norge har klart seg bedre gjennom pandemien enn de fleste andre land. Tiltakene har vært byrdefulle for mange. " \
        "Men færre har mistet livet og flere har vært i jobb sammenlignet med andre land. " \
        "Raske og effektive tiltak har begrenset spredningen av viruset. God etterlevelse og oppslutning om tiltakene " \
        "har vært nødvendig. Samarbeidet med EU om anskaffelse av vaksiner har gitt oss en vei ut av pandemien. " \
        "Regjeringen har etablert beredskapslagre for smittevernutstyr og medisiner. Arbeid er satt i gang for å øke " \
        "intensivkapasiteten. Regjeringen vil opprettholde en høy beredskap for nye virusvarianter. Regjeringen vil " \
        "i den kommende perioden særlig prioritere to store utfordringer for Norge: Begrense utslippene av klimagasser " \
        "og inkludere flere i arbeidslivet. Farlige klimaendringer er vår tids største utfordring. Norge skal redusere " \
        "egne utslipp av klimagasser i tråd med våre internasjonale forpliktelser. I tillegg skal vi støtte fattige " \
        "land i deres arbeid. Norske utslipp går ned. I forrige periode la regjeringen frem planen for ytterligere " \
        "utslippskutt frem mot 2030. Nå skal denne planen iverksettes. Det viktigste tiltaket er at prisen for å " \
        "slippe ut klimagasser må gå opp. Det er nødvendig for å skape et marked for nye, klimavennlige løsninger " \
        "og ny teknologi. Regjeringen vil derfor fremme forslag om økt pris på utslipp av gasser som bidrar til " \
        "klimaendringene. Øvrige skatter og avgifter skal senkes, slik at samlet skattenivå ikke øker. Regjeringen " \
        "vil også fremme forslag om et nytt og mer nøytralt skattesystem for petroleumssektoren. Regjeringen vil " \
        "følge opp veikartet for hydrogen og fortsette byggingen av anlegg for fangst og lagring av CO2. Og så " \
        "snart som mulig skal selskaper kunne søke konsesjon for utbygging av havvind i åpnede områder. " \
        "God sameksistens med eksisterende næringer skal ivaretas. Regjeringen vil legge til rette for " \
        "videre elektrifisering av og fortsatt sikker tilgang på strøm for norsk industri og transport. Regjeringen " \
        "vil styrke Grønn plattform som støtter opp om økt verdiskaping innenfor bærekraftige rammer. Et nytt " \
        "fond som skal investere i fornybar energi i utviklingsland, skal bygges opp over fem år. Den andre " \
        "store utfordringen er å inkludere flere i arbeidslivet. Den økonomiske aktiviteten i Norge tar seg raskt opp. " \
        "Det er nå flere sysselsatte i befolkningen enn før pandemien kom. Stadig færre går ledige. Det blir " \
        "stadig flere ledige stillinger. Perspektivmeldingen viser at vi trenger flere lønnsomme jobber og flere i " \
        "arbeid for å finansiere velferden når bidraget fra oljeaktiviteten reduseres. Allerede nå ser vi mangel " \
        "på kvalifisert arbeidskraft flere steder. Det er både en utfordring og en mulighet. En utfordring fordi " \
        "mangel på arbeidskraft gir mindre verdiskaping og velferd i samfunnet. En mulighet fordi det er mange flere " \
        "som kan og vil arbeide i vårt samfunn. Den muligheten vil regjeringen gripe. Regjeringen vil gjennomføre " \
        "fullføringsreformen slik at flere blir kvalifisert for arbeidslivet og videre studier. Utdanningsløftet " \
        "skal fortsette. Regjeringen vil følge opp strategien for desentralisert og fleksibel utdanning ved fagskoler, " \
        "høyskoler og universiteter for å styrke tilgangen på kompetanse både i byene og distriktene. Muligheten for " \
        "stedsuavhengige arbeidsplasser gjør det mulig å jobbe fra der man måtte ønske. Arbeidet for inkludering i " \
        "arbeidslivet må styrkes ytterligere. Den nye NAV-strategien skal gi økt innovasjon og bedre tjenester på " \
        "arbeids- og velferdsfeltet. Regjeringen vil gjøre det enklere å ta utdanning samtidig som man mottar " \
        "offentlige ytelser til livsopphold. Kompetansereformen skal bidra til at ingen som er i jobb, går ut på dato " \
        "i vårt arbeidsliv. Flere i arbeid er den viktigste forutsetningen for et samfunn med mindre fattigdom og små " \
        "forskjeller. Pandemien har vist at godt internasjonalt samarbeid er god beredskap. Norge har vært avhengig av " \
        "EU for effektiv tilgang til vaksiner. EØS-avtalen bidro til å lette importen av smittevernutstyr. Norge har " \
        "også hjulpet andre land som har vært mer alvorlig rammet enn oss. Pandemien har rammet mange fattige " \
        "land hardt. Regjeringen vil fortsette arbeidet for likeverdig tilgang til covid-19-vaksiner, diagnostikk " \
        "og tester globalt. Norge skal fortsatt være en pådriver for at FNs bærekraftsmål skal nås. Både i " \
        "Norge og internasjonalt. Regjeringen vil gjennom medlemskapet i FNs sikkerhetsråd arbeide for et " \
        "sterkt og velfungerende internasjonalt samarbeid for å ivareta global sikkerhet og fred. Regjeringen " \
        "vil basere sin politikk på sterk støtte til EØS-avtalen og NATO-medlemskapet. Et godt nordisk samarbeid " \
        "bygger opp om dette. Disse avtalene representerer et verdifellesskap Norge deler med våre nærmeste " \
        "samarbeidspartnere. De er en forutsetning for norske arbeidsplasser og vår nasjonale sikkerhet. " \
        "Og de er en avgjørende del av Norges beredskap mot kriser. Regjeringen vil videreføre arbeidet for å " \
        "skape et bærekraftig velferdssamfunn. Endringer i skattesystemet skal gjøre det mer lønnsomt å jobbe " \
        "og mer lønnsomt å investere i norske arbeidsplasser. Regjeringen vil fortsette den historiske satsingen " \
        "på samferdsel. Regjeringen vil følge opp den nye nasjonale strategien for sosial boligpolitikk. Stadig " \
        "færre er bostedsløse i Norge og den positive utviklingen må fortsette. Bostøtten skal styrkes, " \
        "og regjeringen vil prioritere midler til boliglån i distriktene. Regjeringen vil styrke kompetansen i " \
        "barnevernet for å forbedre tjenesten og forberede kommunene på økt ansvar. Det vil bli tatt initiativ til " \
        "å oppheve aktivitetskravet tilsvarende fedrekvoten, slik at alle fedre med opptjente foreldrepengerettigheter " \
        "kan ta ut fedrekvoten. Regjeringen vil utvide tilbudet om helsekartlegging for barn i barnevernet som " \
        "skal flyttes ut av hjemmet. Målet er å identifisere barn som trenger hjelp på et tidligere tidspunkt. " \
        "Regjeringen vil utvide fritidskortet for å senke den økonomiske terskelen for at barn kan delta i " \
        "fritidsaktiviteter. Tilbudet til barn og unge med psykiske helseutfordringer skal styrkes videre, og " \
        "det skal utdannes flere fagfolk til tjenestene. Regjeringen vil sette ned et partssammensatt utvalg for" \
        " å styrke heltidskultur i helsetjenesten. Regjeringen vil ta initiativ til en pilot med investeringstilskudd" \
        " til trygghetsboliger for eldre i distriktene. Målet er at flere eldre som selv ønsker det, skal kunne bo " \
        "i eget hjem. Regjeringen vil fortsette arbeidet med å reformere og effektivisere offentlig sektor. Med " \
        "lavere vekst i Statens pensjonsfond utland og en aldrende befolkning, vil handlingsrommet på budsjettene " \
        "etter hvert bli klart mindre enn vi har vært vant til. Regjeringen vil fase ut den ekstraordinære bruken " \
        "av oljepenger knyttet til koronapandemien. Mer effektiv bruk av fellesskapets ressurser vil bidra til at " \
        "vi fortsatt kan løse utfordringer vårt samfunn stilles overfor. Digitalisering, forenkling og modernisering " \
        "kan frigjøre store ressurser til velferd. Regjeringen vil videreføre og forsterke dette arbeidet. " \
        "Stortingsvalget ga en ny politisk sammensetning av Stortinget. Den parlamentariske situasjonen vil kunne " \
        "endre grunnlaget for det videre arbeidet med flere av de bebudede sakene. Jeg ber Gud velsigne Stortingets " \
        "arbeid, og erklærer Norges 166. storting for åpnet."

# Print ut lengden(antall) ord vi får når vi splitter ved alle tomrom.
print("Antall ord: {0}".format(len(tekst.split())))
# Samme prosess som tidl, men nå splitter vi på .
print("Antall setninger: {0}".format(len(tekst.split("."))))
# deler antall ord på antall setninger for å få gjennomsnitt
print("Gjen.snitt ord pr setning: {0}".format(len(tekst.lower().split()) / len(tekst.split("."))))
# Finner forekomst av alle bokstaver i alfabetet
alfabetet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z','æ', 'ø', 'å')
# støttefunksjon for sortering
def finnAntall(elem):
    return elem[1]

# lag en usortert liste med å telle opp antall forekomster pr bokstav
usortert = list()
for l in range(len(alfabetet)):
        usortert.append((alfabetet[l], len(tekst.lower().split(alfabetet[l]))))

# sorter listen ved hjelp av støttefunksjonen
sortert = sorted(usortert, key=finnAntall, reverse=True)

# skriv ut resultatet
for b in range(len(sortert)):
        print("{0}: {1}".format(sortert[b][0], sortert[b][1]))