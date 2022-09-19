import threading
import queue
import random

# Enkelt mattespill hvor vi generere 2 tilfeldige tall mellom 0 og 50. Vi spørr så bruker
# hva disse er sammenlagt. Bruker har 5 sekund på å svare. Vi teller 1 poeng for hvert
# korrekt svar så lenge det ikke timer ut eller bruker svarer feil.

Svar = 0
poeng = 0
# Generer tall og presenter mattestykket for bruker.
def gameThread(thread_queue):
   a = random.randint(0, 51)
   b = random.randint(0, 51)
   Svar = a + b
   # Presenter regnestykket og be om et svar
   regnestykke = int(input(f'{a} + {b} = '))
   # Sjekk om brukerens svar er korrekt, og returner suksess eller feil
   if(regnestykke == Svar):
      thread_queue.put("Suksess")
   else:
      thread_queue.put("Feil")


SpilleVi = True

if __name__ == '__main__':
    thread_queue = queue.Queue()
    # Så lenge tiden ikke er ute eller bruker svarer feil SpilleVi
    while SpilleVi:
      # Start en tråd vi har timeout på
      thread = threading.Thread(target=gameThread, args=(thread_queue,))
      thread.daemon = True
      thread.start()
      # Hent inputstringen som bruker har satt i tråden
      try:
         resultat = thread_queue.get(timeout=5)
      # Om trådkøen er tom har det gått mer enn 5 sekunder og vi avslutter
      except queue.Empty:
        print("\nToo late - Game Over!")
        print(f'\nDu fikk {poeng} poeng')
        SpilleVi = False
      # Vi har fått et svar i tråden og sjekker om det er Suksess eller Feil
      else:
         # Korrekt svar. Legg til et poeng og start while-løkken på nytt
         if resultat == "Suksess":
            poeng = poeng + 1
         # Feil svar - Vi setter SpilleVi til False og avslutter spillet
         else:
            SpilleVi = False
            print("\nFeil svar - Game Over!")
            print(f'\nDu fikk {poeng} poeng')