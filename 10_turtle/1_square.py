from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")

kush = Turtle()
kush.shape("turtle")
kush.color("cyan")

for _ in range(4):
    kush.forward(200)
    kush.right(90)

screen.exitonclick()
