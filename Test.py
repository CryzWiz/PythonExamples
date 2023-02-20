import turtle

turtle.speed(3)

# create a loop to create diagonal stripes
for i in range(3):
    turtle.forward(100)
    turtle.right(120)
    turtle.pencolor("blue")
    turtle.forward(100)
    turtle.right(120)
    turtle.pencolor("orange")
    turtle.forward(100)
    turtle.right(120)

turtle.exitonclick()



