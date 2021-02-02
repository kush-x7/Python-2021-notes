from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.bgcolor("black")

kush = Turtle()
kush.shape("turtle")
kush.setheading(90)
kush.penup()
kush.forward(250)
kush.pendown()
kush.right(90)
kush.pensize(3)

kush.speed("fast")
colours = ["#003049", "#d62828", "#f77f00", "#f77f00", "#fcbf49"]


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        kush.forward(90)
        kush.right(angle)


for shape_sides in range(3,20):
    kush.color(choice(colours))
    draw_shapes(shape_sides)

screen.exitonclick()
