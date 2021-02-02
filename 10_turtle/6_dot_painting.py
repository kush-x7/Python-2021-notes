# import colorgram
#
# # Extracted colors from the pic
# colors = colorgram.extract("pnt.jpg", 100)
#
# # Now saving those colors in an empty list
# rgb_colors = []
# for color in colors:  # Extracting the RGB color value we need
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)  # created a RGB tuple
#     rgb_colors.append(new_color)  # Appending them one by one in our empty list
#
# print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random

screen = Screen()
colormode(255)
color_list = [(239, 242, 247), (237, 245, 240), (212, 149, 95),
              (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60),
              (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91),
              (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12),
              (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187),
              (151, 206, 220), (97, 127, 168), (34, 81, 49), (180, 188, 210), (84, 65, 30), ]

kush = Turtle()
kush.speed("fastest")

kush.penup()
kush.hideturtle()
kush.setheading(225)
kush.forward(300)
kush.setheading(0)

number_of_dots = 101
for dot_count in range(1, number_of_dots):
    kush.dot(20, random.choice(color_list))
    kush.forward(50)

    if dot_count % 10 == 0:
        kush.setheading(90)
        kush.forward(50)
        kush.setheading(180)
        kush.forward(500)
        kush.setheading(0)



screen.exitonclick()
