from tkinter import *
from tkinter import ttk
import tkinter as tk
import sys

positions = [(50, 50), (150, 50), (150, 150), (50, 150)]

colors = ["blue", "red", "green", "yellow"]

def clockwise():
    global colors
    colors = [colors[-1]] + colors[:-1] 
    update_squares()


def anticlockwise():
    global colors
    colors = colors[1:] + [colors[0]] 
    update_squares()

def update_squares():
    for i in range(4):
        canvas.itemconfig(squares[i], fill=colors[i])  

def exit():
    sys.exit()
    destroy.root_window()


root_window = Tk()
root_window.title("Shivdhan_demo")
root_window.iconbitmap("My_Icon.ico")

lower_frame = ttk.Frame(root_window)
lower_frame.grid(row=2, column=1)

upper_frame = ttk.Frame(root_window)
upper_frame.grid(row=1, column=1)



canvas = tk.Canvas(upper_frame, width=300, height=300, bg="white")
canvas.pack(pady=20)


square_size = 100
squares = [canvas.create_rectangle(x, y, x + square_size, y + square_size,
                                   fill=colors[i], outline="black", width=3) 
           for i, (x, y) in enumerate(positions)]


anti_clock_button = ttk.Button(lower_frame)
anti_clock_button.configure(text="Anti-Clockwise", command=anticlockwise)
anti_clock_button.grid(row=1, column=1, sticky=(E,W,S,N))

clock_button = ttk.Button(lower_frame)
clock_button.configure(text="Clockwise", command=clockwise)
clock_button.grid(row=1, column=2, sticky=(E,W,S,N))

exit_button = ttk.Button(lower_frame)
exit_button.configure(text="Exit", command=exit)
exit_button.grid(row=1, column=3, sticky=(E,W,S,N))

for widget in root_window.winfo_children():
    widget.grid_configure(padx=5, pady=5)


root_window.mainloop()
