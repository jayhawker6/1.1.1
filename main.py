# EZ turtle commands by Andrew G #
import turtle
painter = turtle.Turtle()
wn = turtle.Screen()
wn.mainloop()
painter.right(90)
def down(x):
    painter.forward(x)
def up(x):
    painter.backward(x)
def right(x):
    painter.left(90)
    down(x)
    painter.right(90)
def left(x):
    painter.right(90)
    down(x)
    painter.left(90)
def speed(x):
    painter.speed(x)
def size(x):
    painter.pensize(x)
# End of EZ turtle commands by Andrew G #