from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.title("I AM IRON-MAN")

kush = Turtle("arrow")
kush.hideturtle()

piece1Goto = (-56, 207)
piece2Goto = (-144, 10)
piece3Goto = (-70, -167)
piece4Goto = (-100, 20)
piece5Goto = (22, -7)

# yellow_part
piece1 = [[55, 207], [19, 72], [-20, 72], [-64, 207], [-130, 157], [-145, 15],
[-115, -139], [-48, -206], [48, -206], [115, -139], [145, 15], [127, 161], [64, 207]]

piece2 = [[-40, -145], [40, -145], [144, 10]]

piece3 = [[-49, -145], [49, -145], [70, -167]]

piece4 = [[-22, -7]]

piece5 = [[100, 20]]

color = ["yellow", "yellow", "yellow", "cyan", "cyan"]
def draw(piece, piecegoto):
    kush.penup()
    kush.goto(piecegoto)
    kush.pendown()
    kush.speed("slowest")
    kush.pensize(20)
    kush.begin_fill()
    for i in range(len(piece)):
        x = piece[i][0]
        y = piece[i][1]
        kush.goto(x, y)


screen.bgcolor("#AA0505")
kush.color("#FBCA03")
draw(piece1, piece1Goto)
draw(piece2, piece2Goto)
draw(piece3, piece3Goto)
kush.color("#67C7EB")
draw(piece4, piece4Goto)
draw(piece5, piece5Goto)

# def get_mouse_click_coor(x, y):
#     print(x,y)
#
# # screen.bgpic("Untitled design-2.gif")
# screen.onscreenclick(get_mouse_click_coor)

screen.mainloop()
