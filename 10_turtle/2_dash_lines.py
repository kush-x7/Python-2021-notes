from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")

kush = Turtle()
kush.shape("turtle")
kush.color("cyan")

for _ in range(15):
    kush.forward(10)
    kush.penup()
    kush.forward(10)
    kush.pendown()

screen.exitonclick()
