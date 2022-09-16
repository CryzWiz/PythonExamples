"""
    Importer biblioteket
"""

import turtle

"""
    Lag en scene og vår egen turtle som kan utføre tegningen.
"""

scene = turtle.Screen()
minSkilpadde = turtle.Turtle()

"""
    Benytter så minSkillpadde for å tegne.
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