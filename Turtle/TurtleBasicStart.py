"""
    Importer biblioteket
"""

import turtle

"""
    Lag en scene og vår egen turtle som kan utføre tegningen.
    Scenen er vinduet som åpnes. Med å definere den inn kan du gi
    den egne verdier for tekst, farge og størrelse osv.
"""

scene = turtle.Screen()
minSkilpadde = turtle.Turtle()

"""
    Benytter så minSkilpadde for å tegne.
"""

for i in range(4):
    minSkilpadde.forward(75)
    minSkilpadde.right(90)

"""
    Gi scenen beskjed at ved musklikk skal den lukkes og avsluttes
"""
scene.exitonclick()

"""
    Påkall og vis scenen vår.
"""
scene.mainloop()