# step 1 for getting coordinates

import turtle

screen = turtle.Screen()
screen.setup(900, 650)
screen.bgpic("Untitled design-1.gif")

def get_mouse_click_coor(x, y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
