from turtle import Turtle, Screen, colormode
import random

screen = Screen()
screen.bgcolor("black")

kush = Turtle()
kush.pensize(2)
kush.speed("fastest")
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        kush.color(random_color())
        kush.circle(100)
        kush.setheading(kush.heading() + size_of_gap)

draw_spirograph(5)
screen.exitonclick()
