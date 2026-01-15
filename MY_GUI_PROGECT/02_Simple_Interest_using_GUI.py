from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys

def Interest_handler():
    try:
        Amount = float(Amount_entry_strv.get())
        Rate = float(Rate_entry_strv.get())
        Time = float(Time_entry_strv.get())
        S_I = (Amount * Rate * Time) / 100
        Value_label_strv.set(str(S_I))
    except ValueError:
        messagebox.showerror('Error Messagebox', 'Enter valid details')


def Clear_handler():
    Amount_entry_strv.set(' ')
    Rate_entry_strv.set(' ')
    Time_entry_strv.set(' ')
    Value_label_strv.set(' ')

def Exit_handler():
    print("Exiting The App")
    root_window.destroy()
    sys.exit()

root_window = Tk()

root_window.title('Simple Interest Calculator')
root_window.iconbitmap("My_Icon.ico")
root_window.configure(bg='pink')

upper_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
upper_frame.grid(column=1, row=1, sticky=(N,W,E,S))

Button_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
Button_frame.grid(column=1, row=2, sticky=(N,W,E,S))

Output_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
Output_frame.grid(column=1, row=3, sticky=(N,W,E,S))


Amount_label = Label(upper_frame)
Amount_label.configure(text='Enter Amount : ')
Amount_label.grid(row=1, column=1, sticky=(E, W))

Rate_label = Label(upper_frame)
Rate_label.configure(text='Enter Rate Of Interest : ')
Rate_label.grid(row=2, column=1, sticky=(E, W))

Time_label = Label(upper_frame)
Time_label.configure(text='Enter Duration : ')
Time_label.grid(row=3, column=1, sticky=(E, W))

Amount_entry_strv = StringVar()
Amount_entry = ttk.Entry(upper_frame)
Amount_entry.configure(textvariable = Amount_entry_strv)
Amount_entry.grid(row=1, column=2)

Rate_entry_strv = StringVar()
Rate_entry = ttk.Entry(upper_frame)
Rate_entry.configure(textvariable = Rate_entry_strv)
Rate_entry.grid(row=2, column=2)

Time_entry_strv = StringVar()
Time_entry = ttk.Entry(upper_frame)
Time_entry.configure(textvariable = Time_entry_strv)
Time_entry.grid(row=3, column=2)

Interest_button = ttk.Button(Button_frame)
Interest_button.configure(text='Interest', command=Interest_handler)
Interest_button.grid(row=1, column=1, sticky=(E, W))

Clear_button = ttk.Button(Button_frame)
Clear_button.configure(text='Clear', command=Clear_handler)
Clear_button.grid(row=1, column=2, sticky=(E, W))

Exit_button = ttk.Button(Button_frame)
Exit_button.configure(text='Exit', command=Exit_handler)
Exit_button.grid(row=1, column=3, sticky=(E, W))

result_label = Label(Output_frame)
result_label.configure(text='Simple Interest : ')
result_label.grid(row=1, column=1, sticky=(E, W))

Value_label_strv = StringVar()
Value_label = Label(Output_frame)
Value_label.configure(textvariable = Value_label_strv)
Value_label.grid(row=1, column=2, sticky=(E, W))

for widget in root_window.winfo_children():
    widget.grid_configure(padx=3, pady=3)

root_window.mainloop()
