import turtle
from tkinter import *

root_window = Tk()
root_window.title("Final Demo Project")
root_window.iconbitmap("My_Icon.ico")
root_window.geometry("1540x800")

main_Frame = Frame(root_window, bd=3, relief='raised')
main_Frame.place(x=0, y=0, height=800, width=1540)

canvas = Canvas(main_Frame, height=580)
canvas.place(x=0, y=0, height=800, width=1540)

turtle_screen = turtle.TurtleScreen(canvas)
turtle_screen.bgcolor("white")

t = turtle.RawTurtle(turtle_screen)
t.hideturtle()
t.speed(1.5)
def draw_circle():
    t.penup()
    t.goto(500, -20)
    t.pendown()
    t.pensize(5)
    t.color("#ffcc00", "#2c2f48")  
    t.begin_fill()
    t.circle(150)
    t.end_fill()


def draw_logo_lines():
    t.fillcolor("#ffcc00")
    t.pensize(1)
    t.penup()
    t.goto(410, 15)
    t.begin_fill()
    t.pendown()
    t.forward(18)
    t.left(65)
    t.forward(140)
    t.right(120)
    t.forward(155)
    t.left(60)
    t.forward(25)
    t.left(180)
    t.penup()
    t.forward(19)
    t.pendown()
    t.right(60)
    t.forward(270)
    t.left(57)
    t.forward(28)
    t.left(180)
    t.forward(22)
    t.right(57)
    t.forward(109)
    t.right(60)
    t.forward(147)
    t.end_fill()
    
    t.penup()
    t.goto(428, 237)
    t.pendown()
    t.left(120)
    t.forward(6)
    t.right(60)
    t.forward(142)
    t.left(117)
    t.forward(133)
    t.right(60)
    t.forward(25)
    t.left(180)
    t.forward(19)
    t.left(60)
    t.forward(138)
    t.left(62)
    t.forward(123)

def horozontal_line():
    t.penup
    t.goto(170, -170)
    t.pendown()
    t.pensize(3)
    t.pencolor("gray")
    t.left(56)
    t.forward(680)
    t.penup()

def write_text():
    t.penup()
    t.goto(500, -80)
    t.color("#444444")
    t.write("CPA", align="center", font=("Lucida Calligraphy", 25, "bold"))

    t.goto(500, -120)
    t.color("black")
    t.write("CORECODE PROGRAMMING ACADEMY", align="center", font=("Lucida Fax", 20, "bold"))

    t.goto(500, -150)
    t.color("gray")
    t.write("An Academy By Yogeshwar Shukla Sir", align="center", font=("Lucida Fax", 15, "bold"))

def another_write_text():
    t.goto(500, -210)
    t.color("#444444")
    t.write("Project By : ", align="center", font=("Lucida Lucida Fax", 15, "bold"))

    t.goto(500, -240)
    t.color("#444444")
    t.write("134_Jyoti Jagave", align="center", font=("Lucida Calligraphy", 13, "bold"))

    t.goto(500, -265)
    t.color("#444444")
    t.write("062_Rohit Jagave", align="center", font=("Lucida Calligraphy", 13, "bold"))

    t.goto(500, -295)
    t.color("#444444")
    t.write("055_Shrinivas Jagave", align="center", font=("Lucida Calligraphy", 13, "bold"))

    t.goto(500, -325)
    t.color("#444444")
    t.write("064_Shrikant Tate", align="center", font=("Lucida Calligraphy", 13, "bold"))

draw_circle()
draw_logo_lines()
write_text()
horozontal_line()
another_write_text()

root_window.mainloop()
