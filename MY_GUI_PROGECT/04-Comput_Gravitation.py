from tkinter import *
from tkinter import ttk
import sys
from tkinter import messagebox

G = 6.67 * 10**-11

def compute_handler():
    try:
        m1 = float(entry_object_1_strv.get())
        m2 = float(entry_object_2_strv.get())
        r = float(entry_distance_strv.get())
        F = (G * m1 * m2) / (r ** 2)
        label_value_strv.set()
    except ValueError:
        messagebox.showerror('Error Messagebox', 'Enter valid details')


def clear_handler():
    entry_object_1_strv.set(' ')
    entry_object_2_strv.set(' ')
    entry_distance_strv.set(' ')
    label_value_strv.set(' ')

def exit_handler():
    print('Exiting the application....')
    root_window.destroy()
    sys.exit()

root_window = Tk()
root_window.title('Compute Gravitational Force')
root_window.configure(bg="pink")
root_window.iconbitmap("My_Icon.ico")

upper_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
upper_frame.grid(column=1, row=1, sticky=(N,W,E,S))

Button_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
Button_frame.grid(column=1, row=2, sticky=(N,W,E,S))

Output_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
Output_frame.grid(column=1, row=3, sticky=(N,W,E,S))


label_object_1 = Label(upper_frame)
label_object_1.configure(text='Enter mass of object 1 in kgs')
label_object_1.grid(row=1, column=1, sticky=(E, W))

label_object_2 = Label(upper_frame)
label_object_2.configure(text='Enter mass of object 2 in kgs')
label_object_2.grid(row=2, column=1, sticky=(E, W))

label_distance = Label(upper_frame)
label_distance.configure(text='Enter distance between two objects in kgs')
label_distance.grid(row=3, column=1, sticky=(E, W))

button_compute = ttk.Button(Button_frame)
button_compute.configure(text='Compute', command=compute_handler)
button_compute.grid(row=1, column=1, sticky=(E, W))

button_clear = ttk.Button(Button_frame)
button_clear.configure(text='Clear', command=clear_handler)
button_clear.grid(row=1, column=2, sticky=(E, W))

button_exit = ttk.Button(Button_frame)
button_exit.configure(text='Exit', command=exit_handler)
button_exit.grid(row=1, column=3, sticky=(E, W))

entry_object_1_strv = StringVar()
entry_object_1 = ttk.Entry(upper_frame)
entry_object_1.configure(textvariable=entry_object_1_strv)
entry_object_1.grid(row=1, column=2, sticky=(E, W))

entry_object_2_strv = StringVar()
entry_object_2 = ttk.Entry(upper_frame)
entry_object_2.configure(textvariable=entry_object_2_strv)
entry_object_2.grid(row=2, column=2, sticky=(E, W))

entry_distance_strv = StringVar()
entry_distance = ttk.Entry(upper_frame)
entry_distance.configure(textvariable=entry_distance_strv)
entry_distance.grid(row=3, column=2, sticky=(E, W))

label_result_1 = Label(Output_frame)
label_result_1.configure(text='Gravitational Force is : [')
label_result_1.grid(row=1, column=1, sticky=(E, W))

label_result_2 = Label(Output_frame)
label_result_2.configure(text='N]')
label_result_2.grid(row=1, column=3, sticky=(E, W))

label_value_strv = StringVar()
label_value = Label(Output_frame)
label_value.configure(textvariable=label_value_strv)
label_value.grid(row=1, column=2, sticky=(E, W))

for widget in root_window.winfo_children():
    widget.grid_configure(padx=3, pady=3)

root_window.mainloop()
