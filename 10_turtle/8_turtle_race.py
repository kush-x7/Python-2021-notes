from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)

user_bet = screen.textinput(title="Make Your bet", prompt="Which turtle will win the race?")

colors = ["red", "green", "yellow", "orange", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    # Giving position to turtle
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    # appending all turtles one by one
    all_turtle.append((new_turtle))

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You,ve won! The {winning_color} turtle is the winner!")
            else:
                print(f"You,ve lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
