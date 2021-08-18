import turtle
tur=turtle.Turtle()
turtle.bgcolor("black")
tur.pensize(2)
tur.speed(0)
for i in range(5):
    for colors in ["violet","indigo","blue","green","yellow","orange","red"]:
        tur.color(colors)
        tur.circle(150)
        tur.left(10)
turtle.hideturtle()
turtle.done()