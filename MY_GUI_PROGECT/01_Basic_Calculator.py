from tkinter import *
from tkinter import ttk
import sys

def do_addition():
    first_number = float(entry_strv_1.get())
    second_number = float(entry_strv_2.get())
    result = first_number + second_number
    result_label_strv.set(str(result))

def do_substraction():
    first_number = float(entry_strv_1.get())
    second_number = float(entry_strv_2.get())
    result = first_number - second_number
    result_label_strv.set(str(result))

def do_multiplication():
    first_number = float(entry_strv_1.get())
    second_number = float(entry_strv_2.get())
    result = first_number * second_number
    result_label_strv.set(str(result))

def do_division():
    first_number = float(entry_strv_1.get())
    second_number = float(entry_strv_2.get())
    result = first_number / second_number
    result_label_strv.set(str(result))

def do_floordivision():
    first_number = float(entry_strv_1.get())
    second_number = float(entry_strv_2.get())
    result = first_number // second_number
    result_label_strv.set(str(result))

def do_clear():
    entry_strv_1.set('')
    entry_strv_2.set('')
    result_label_strv.set('')
    
def do_exit():
    print('Exiting the app')
    root_window.destroy()
    sys.exit(0)
    
root_window = Tk()
root_window.iconbitmap("My_Icon.ico")
root_window.title('Calculator')
root_window.configure(bg='pink')

upper_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
upper_frame.grid(column=1, row=1, sticky=(N,W,E,S))

Button_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
Button_frame.grid(column=1, row=2, sticky=(N,W,E,S))

Output_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
Output_frame.grid(column=1, row=3, sticky=(N,W,E,S))

label_1 = Label(upper_frame)
label_1.configure(text='Enter First Number')
label_1.grid(row=1, column=1, sticky=(E, W))

label_2 = Label(upper_frame)
label_2.configure(text='Enter Second Number')
label_2.grid(row=2, column=1, sticky=(E, W))

label_3 = Label(Output_frame)
label_3.configure(text='Result : ')
label_3.grid(row=1, column=1, sticky=(E, W))

entry_strv_1 = StringVar()
entry_1 = ttk.Entry(upper_frame)
entry_1.configure(textvariable=entry_strv_1)
entry_1.grid(row=1, column=2, sticky=(E, W))

entry_strv_2 = StringVar()
entry_2 = ttk.Entry(upper_frame)
entry_2.configure(textvariable=entry_strv_2)
entry_2.grid(row=2, column=2, sticky=(E, W))

button_addition = ttk.Button(Button_frame)
button_addition.configure(text='Addition', command=do_addition)
button_addition.grid(row=1, column=1, sticky=(E, W))

button_subtraction = ttk.Button(Button_frame)
button_subtraction.configure(text='Subtraction', command=do_substraction)
button_subtraction.grid(row=1, column=2, sticky=(E, W))

button_multiplication = ttk.Button(Button_frame)
button_multiplication.configure(text='Multiplication', command=do_multiplication)
button_multiplication.grid(row=2, column=1, sticky=(E, W))

button_division = ttk.Button(Button_frame)
button_division.configure(text='Division', command=do_division)
button_division.grid(row=2, column=2, sticky=(E, W))

button_floordivision = ttk.Button(Button_frame)
button_floordivision.configure(text='Floor Division', command=do_floordivision)
button_floordivision.grid(row=3, column=1, sticky=(E, W))

button_clear = ttk.Button(Button_frame)
button_clear.configure(text='Clear', command=do_clear)
button_clear.grid(row=3, column=2, sticky=(E, W))

button_exit = ttk.Button(Button_frame)
button_exit.configure(text='Exit', command=do_exit)
button_exit.grid(row=4, column=1, sticky=(E, W))

result_label_strv = StringVar()
result_label = Label(Output_frame)
result_label.configure(textvariable = result_label_strv)
result_label.grid(row=1, column= 2, sticky=(E, W))

for widget in root_window.winfo_children():
    widget.grid_configure(padx=3, pady=3)


root_window.mainloop()
