from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')

tim = Turtle()
tim.color('cyan')
tim.speed('slowest')


def shape():
    for _ in range(1):
        tim.right(90)
        tim.forward(200)

        tim.left(90)
        tim.forward(40)

        tim.left(90)
        tim.forward(50)

        tim.right(45 +90)
        tim.forward(70)

        tim.left(90 +45)
        tim.forward(50)

        tim.left(40)
        tim.forward(70)

        tim.right( 85)
        tim.forward(70)

        tim.left(45)
        tim.forward(50)

        tim.left(90 + 45)
        tim.forward(80)

        tim.right(45 + 90)
        tim.forward(50)

        tim.left(90)
        tim.forward(40)


num = 72
while num != 0:
    shape()
    new_pointing = tim.heading() + 5
    tim.setheading(new_pointing)
    num -= 1


screen.exitonclick()
