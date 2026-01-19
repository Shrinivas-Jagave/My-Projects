import tkinter as tk
import math
import sys

def button_click(value):
    current_text = entry.get()
    new_value = current_text + str(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_value)

def calculate_result():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def on_enter(e):
    e.widget['background'] = "#7f7d9c"

def on_leave(e):
    e.widget['background'] = "#787276"

def clear_entry():
    entry.delete(0, tk.END)


def backspace():
    current = entry.get()
    updated = current[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, updated)


def calculate_reciprocal():
    try:
        value = float(entry.get())
        result = 1 / value
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calculate_square():
    try:
        value = float(entry.get())
        result = value ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calculate_square_root():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def exit_calculation():
    sys.exit()

root_window = tk.Tk()
root_window.title("Scientific Calculator")
root_window.iconbitmap("My_Icon.ico")
root_window.configure(bg="#333333")
root_window.geometry("400x550")
root_window.resizable(True, True)


entry = tk.Entry(
    root_window,
    font=("Courier New Baltic", 20),
    justify="right",
    bd=5,
    relief="ridge"
)
entry.grid(row=0, column=0, columnspan=5, padx=0, pady=15, ipadx=8, ipady=10, sticky="nsew")


B1 = tk.Button(
                root_window, 
                text='%', 
                command=lambda: button_click('%'), 
                font=("Arial", 16, "bold"), 
                width=7,
                height=3,
                bg="#787276",
                fg="#83F5D8"
            )
B1.grid(row=1, column=0, padx=4, pady=4, sticky="nsew")

B2 = tk.Button(
                root_window, 
                text='(', 
                command=lambda: button_click('('), 
                font=("Arial", 16, "bold"),
                width=7, 
                height=3,
                bg="#787276",
                fg="#83F5D8"
            )
B2.grid(row=1, column=1, padx=4, pady=4, sticky="nsew")

B3 = tk.Button(
                root_window, 
                text=')', 
                command=lambda: button_click(')'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="#83F5D8"
            )
B3.grid(row=1, column=2, padx=4, pady=4, sticky="nsew")

B4 = tk.Button(
                root_window, 
                text='C', 
                command=clear_entry, 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="red"
            )
B4.grid(row=1, column=3, padx=4, pady=4, sticky="nsew")

B5 = tk.Button(
                root_window, 
                text='<--', 
                command=backspace, 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="Blue"
            )
B5.grid(row=1, column=4, padx=4, pady=4, sticky="nsew")

B6 = tk.Button(
                root_window, 
                text='1/x', 
                command=calculate_reciprocal, 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="#83F5D8"
            )
B6.grid(row=2, column=0, padx=4, pady=4, sticky="nsew")

B7 = tk.Button(
                root_window, 
                text='√', 
                command=calculate_square_root, 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="#83F5D8"
            )
B7.grid(row=2, column=1, padx=4, pady=4, sticky="nsew")

B8 = tk.Button(
                root_window, 
                text='x²', 
                command=calculate_square, 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="#83F5D8"
            )
B8.grid(row=2, column=2, padx=4, pady=4, sticky="nsew")

B9 = tk.Button(
                root_window, 
                text='/', 
                command=lambda: button_click('/'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="#83F5D8"
            )
B9.grid(row=2, column=3, padx=4, pady=4, sticky="nsew")

B10 = tk.Button(
                root_window, 
                text='7', 
                command=lambda: button_click('7'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="White"
            )
B10.grid(row=3, column=0, padx=4, pady=4, sticky="nsew")

B11 = tk.Button(
                root_window, 
                text='8', 
                command=lambda: button_click('8'), 
                font=("Arial", 16, "bold"),
                width=7, 
                height=3,
                bg="#787276",
                fg="White"
            )
B11.grid(row=3, column=1, padx=4, pady=4, sticky="nsew")

B12 = tk.Button(    
                root_window, 
                text='9', 
                command=lambda: button_click('9'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="White"
            )
B12.grid(row=3, column=2, padx=4, pady=4, sticky="nsew")

B13 = tk.Button(
                root_window, 
                text='*', 
                command=lambda: button_click('*'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="#83F5D8"
            )
B13.grid(row=3, column=3, padx=4, pady=4, sticky="nsew")

B14 = tk.Button(
                root_window, 
                text='4', 
                command=lambda: button_click('4'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="White"
            )
B14.grid(row=4, column=0, padx=4, pady=4, sticky="nsew")

B15 = tk.Button(
                root_window, 
                text='5', 
                command=lambda: button_click('5'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="White"
            )
B15.grid(row=4, column=1, padx=4, pady=4, sticky="nsew")

B16 = tk.Button(
                root_window, 
                text='6', 
                command=lambda: button_click('6'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="White"
            )
B16.grid(row=4, column=2, padx=4, pady=4, sticky="nsew")

B17 = tk.Button(
                root_window, 
                text='-', 
                command=lambda: button_click('-'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="#83F5D8"
            )
B17.grid(row=4, column=3, padx=4, pady=4, sticky="nsew")

B18 = tk.Button(
                root_window, 
                text='1', 
                command=lambda: button_click('1'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="White"
            )
B18.grid(row=5, column=0, padx=4, pady=4, sticky="nsew")

B19 = tk.Button(
                root_window, 
                text='2', 
                command=lambda: button_click('2'), 
                font=("Arial", 16, "bold"),
                width=7, 
                height=3,
                bg="#787276",
                fg="White"
            )
B19.grid(row=5, column=1, padx=4, pady=4, sticky="nsew")

B20 = tk.Button(
                root_window, 
                text='3', 
                command=lambda: button_click('3'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="White"
            )
B20.grid(row=5, column=2, padx=4, pady=4, sticky="nsew")

B21 = tk.Button(
                root_window, 
                text='+', 
                command=lambda: button_click('+'), 
                font=("Arial", 16, "bold"), 
                width=7,
                height=3,
                bg="#787276",
                fg="#83F5D8"
            )
B21.grid(row=5, column=3, padx=4, pady=4, sticky="nsew")

B22 = tk.Button(
                root_window, 
                text='Home', 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="#FA4B05"
            )
B22.grid(row=6, column=0, padx=4, pady=4, sticky="nsew")

B23 = tk.Button(
                root_window, 
                text='0', 
                command=lambda: button_click('0'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="White"
            )
B23.grid(row=6, column=1, padx=4, pady=4, sticky="nsew")

B24 = tk.Button(
                root_window, 
                text='.', 
                command=lambda: button_click('.'), 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#787276",
                fg="White"
            )
B24.grid(row=6, column=2, padx=4, pady=4, sticky="nsew")

B25 = tk.Button(
                root_window, 
                text='=', 
                command=calculate_result, 
                font=("Arial", 16, "bold"), 
                width=7, 
                height=3,
                bg="#3A69C2",
                fg="White"
            )
B25.grid(row=6, column=3, padx=4, pady=4, sticky="nsew")

B1.bind("<Enter>", on_enter)
B1.bind("<Leave>", on_leave)

B2.bind("<Enter>", on_enter)
B2.bind("<Leave>", on_leave)

B3.bind("<Enter>", on_enter)
B3.bind("<Leave>", on_leave)

B4.bind("<Enter>", on_enter)
B4.bind("<Leave>", on_leave)

B5.bind("<Enter>", on_enter)
B5.bind("<Leave>", on_leave)

B6.bind("<Enter>", on_enter)
B6.bind("<Leave>", on_leave)

B7.bind("<Enter>", on_enter)
B7.bind("<Leave>", on_leave)

B8.bind("<Enter>", on_enter)
B8.bind("<Leave>", on_leave)

B9.bind("<Enter>", on_enter)
B9.bind("<Leave>", on_leave)

B10.bind("<Enter>", on_enter)
B10.bind("<Leave>", on_leave)

B11.bind("<Enter>", on_enter)
B11.bind("<Leave>", on_leave)

B12.bind("<Enter>", on_enter)
B12.bind("<Leave>", on_leave)

B13.bind("<Enter>", on_enter)
B13.bind("<Leave>", on_leave)

B14.bind("<Enter>", on_enter)
B14.bind("<Leave>", on_leave)

B15.bind("<Enter>", on_enter)
B15.bind("<Leave>", on_leave)

B16.bind("<Enter>", on_enter)
B16.bind("<Leave>", on_leave)

B17.bind("<Enter>", on_enter)
B17.bind("<Leave>", on_leave)

B18.bind("<Enter>", on_enter)
B18.bind("<Leave>", on_leave)

B19.bind("<Enter>", on_enter)
B19.bind("<Leave>", on_leave)

B20.bind("<Enter>", on_enter)
B20.bind("<Leave>", on_leave)

B21.bind("<Enter>", on_enter)
B21.bind("<Leave>", on_leave)

B22.bind("<Enter>", on_enter)
B22.bind("<Leave>", on_leave)

B23.bind("<Enter>", on_enter)
B23.bind("<Leave>", on_leave)

B24.bind("<Enter>", on_enter)
B24.bind("<Leave>", on_leave)

B25.bind("<Enter>", on_enter)
B25.bind("<Leave>", on_leave)

# =========================
# Start App
# =========================

for col in range(5):  
    root_window.grid_columnconfigure(col, weight=1)

for row in range(7):  
    root_window.grid_rowconfigure(row, weight=1)

root_window.mainloop()
