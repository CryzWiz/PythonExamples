"""
    Importer biblioteket
"""

import turtle

"""
    Lag en scene og vår egen turtle som kan utføre tegningen.
"""

scene = turtle.Screen()
minSkillpadde = turtle.Turtle()

"""
    Benytter så minSkillpadde for å tegne.
"""

for i in range(4):
    minSkillpadde.forward(75)
    minSkillpadde.right(90)

"""
    Gi scenen beskjed at ved musklikk skal den lukkes og avsluttes
"""
scene.exitonclick()

"""
    Påkall og vi scenen vår.
"""
scene.mainloop()