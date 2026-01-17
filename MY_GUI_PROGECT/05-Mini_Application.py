from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys

def exit_handler():
    print('Exiting the app')
    root_window.destroy()
    sys.exit()

#------------------------------------------------------------------------------

# Area of Square
def area_of_square():
    def area_handler():
        try:
            side = float(entry_side_strv.get())
            area = side * side
            Label_result_strv.set(f"Area of a square {area} cmSqure")
        except ValueError:
            messagebox.showerror('Error Messagebox', 'Enter valid details')

    def clear_handler():
        entry_side_strv.set('')
        Label_result_strv.set('')
        
    Square_frame = ttk.Frame(root_window)
    Square_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
    Square_frame.grid(row=1, column=1, sticky=(E, W, N, S))
    Square_frame.rowconfigure(1, weight=1)
    Square_frame.columnconfigure(1, weight=1)
    Square_frame.grid_configure(pady=5)

    Label_side = Label(Square_frame)
    Label_side.configure(text='Enter Side Of Square in cm')
    Label_side.grid(row=1, column=1, sticky=(E, W))

    entry_side_strv = StringVar()
    Entry_side = ttk.Entry(Square_frame)
    Entry_side.configure(textvariable=entry_side_strv)
    Entry_side.grid(row=1, column=2, sticky=(E, W))

    area_button = ttk.Button(Square_frame)
    area_button.configure(text='Area Of Square', command=area_handler)
    area_button.grid(row=2, column=1, sticky=(E, W))

    clear_button = ttk.Button(Square_frame)
    clear_button.configure(text='Clear', command=clear_handler)
    clear_button.grid(row=2, column=2, sticky=(E, W))

    Label_result_strv = StringVar()
    Label_result = Label(result_frame)
    Label_result.configure(textvariable=Label_result_strv)
    Label_result.grid(row=1, column=1, sticky=(E, W))

    for widget in Square_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)
        
#---------------------------------------------------------------------------------
        
# Area Of Rectangle
def area_of_rectangle():
    def area_handler():
        try:
            width = float(entry_width_strv.get())
            length = float(entry_length_strv.get())
            area = width * length
            Label_result_strv.set(f"Area of a rectangle {area} cmSqure")
        except ValueError:
            messagebox.showerror('Error Messagebox', 'Enter valid details')

    def clear_handler():
        entry_width_strv.set('')
        entry_length_strv.set('')
        Label_result_strv.set('')

    Rectangle_frame = ttk.Frame(root_window)
    Rectangle_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
    Rectangle_frame.grid(row=1, column=1, sticky=(E, W, N, S))
    Rectangle_frame.rowconfigure(1, weight=1)
    Rectangle_frame.columnconfigure(1, weight=1)
    Rectangle_frame.grid_configure(pady=5)
    
    Label_width = Label(Rectangle_frame)
    Label_width.configure(text='Enter Width Of Rectangle in cm')
    Label_width.grid(row=1, column=1, sticky=(E, W))

    Label_length = Label(Rectangle_frame)
    Label_length.configure(text='Enter Length Of Rectangle in cm')
    Label_length.grid(row=2, column=1, sticky=(E, W))

    entry_width_strv = StringVar()
    Entry_width = ttk.Entry(Rectangle_frame)
    Entry_width.configure(textvariable=entry_width_strv)
    Entry_width.grid(row=1, column=2, sticky=(E, W))

    entry_length_strv = StringVar()
    Entry_length = ttk.Entry(Rectangle_frame)
    Entry_length.configure(textvariable=entry_length_strv)
    Entry_length.grid(row=2, column=2, sticky=(E, W))

    rectangle_area_button = ttk.Button(Rectangle_frame)
    rectangle_area_button.configure(text='Area of Rectangle', command=area_handler)
    rectangle_area_button.grid(row=3, column=1, sticky=(E, W))

    rectangle_clear_button = ttk.Button(Rectangle_frame)
    rectangle_clear_button.configure(text='Clear', command=clear_handler)
    rectangle_clear_button.grid(row=3, column=2, sticky=(E, W))

    Label_result_strv = StringVar()
    Label_result = Label(result_frame)
    Label_result.configure(textvariable=Label_result_strv)
    Label_result.grid(row=1, column=1, sticky=(E, W))

    for widget in Rectangle_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)

#-------------------------------------------------------------------

# Addition
def addition():
    def addition_handler():
        try:       
            a = float(entry_1_strv.get())
            b = float(entry_2_strv.get())
            result = a + b
            Label_result_strv.set(f"Addition : {result}")
        except ValueError:
            messagebox.showerror('Error Messagebox', 'Enter valid details')

    def clear_handler():
        entry_1_strv.set('')
        entry_2_strv.set('')
        Label_result_strv.set('')

    Addition_frame = ttk.Frame(root_window)
    Addition_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
    Addition_frame.grid(row=1, column=1, sticky=(E, W, N, S))
    Addition_frame.rowconfigure(1, weight=1)
    Addition_frame.columnconfigure(1, weight=1)
    Addition_frame.grid_configure(pady=5)

    Label_1 = Label(Addition_frame)
    Label_1.configure(text='Enter First Number')
    Label_1.grid(row=1, column=1, sticky=(E, W))

    Label_2 = Label(Addition_frame)
    Label_2.configure(text='Enter Second Number')
    Label_2.grid(row=2, column=1, sticky=(E, W))

    entry_1_strv = StringVar()
    Entry_1 = ttk.Entry(Addition_frame)
    Entry_1.configure(textvariable=entry_1_strv)
    Entry_1.grid(row=1, column=2, sticky=(E, W))

    entry_2_strv = StringVar()
    Entry_2 = ttk.Entry(Addition_frame)
    Entry_2.configure(textvariable=entry_2_strv)
    Entry_2.grid(row=2, column=2, sticky=(E, W))

    addition_button = ttk.Button(Addition_frame)
    addition_button.configure(text='Addition', command=addition_handler)
    addition_button.grid(row=3, column=1, sticky=(E, W))

    addition_clear_button = ttk.Button(Addition_frame)
    addition_clear_button.configure(text='Clear', command=clear_handler)
    addition_clear_button.grid(row=3, column=2, sticky=(E, W))

    Label_result_strv = StringVar()
    Label_result = Label(result_frame)
    Label_result.configure(textvariable=Label_result_strv)
    Label_result.grid(row=1, column=1, sticky=(E, W))

    for widget in Addition_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)
        
#--------------------------------------------------------------------------------------

# Subtraction
def subtraction():
    def subtraction_handler():
        try:
            a = float(entry_1_strv.get())
            b = float(entry_2_strv.get())
            result = a - b
            Label_result_strv.set(f"Subtraction : {result}")
        except ValueError:
            messagebox.showerror('Error Messagebox', 'Enter valid details')

    def clear_handler():
        entry_1_strv.set('')
        entry_2_strv.set('')
        Label_result_strv.set('')

    Subtraction_frame = ttk.Frame(root_window)
    Subtraction_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
    Subtraction_frame.grid(row=1, column=1, sticky=(E, W, N, S))
    Subtraction_frame.rowconfigure(1, weight=1)
    Subtraction_frame.columnconfigure(1, weight=1)
    Subtraction_frame.grid_configure(pady=5)

    Label_1 = Label(Subtraction_frame)
    Label_1.configure(text='Enter First Number')
    Label_1.grid(row=1, column=1, sticky=(E, W))

    Label_2 = Label(Subtraction_frame)
    Label_2.configure(text='Enter Second Number')
    Label_2.grid(row=2, column=1, sticky=(E, W))

    entry_1_strv = StringVar()
    Entry_1 = ttk.Entry(Subtraction_frame)
    Entry_1.configure(textvariable=entry_1_strv)
    Entry_1.grid(row=1, column=2, sticky=(E, W))

    entry_2_strv = StringVar()
    Entry_2 = ttk.Entry(Subtraction_frame)
    Entry_2.configure(textvariable=entry_2_strv)
    Entry_2.grid(row=2, column=2, sticky=(E, W))

    addition_button = ttk.Button(Subtraction_frame)
    addition_button.configure(text='Subtraction', command=subtraction_handler)
    addition_button.grid(row=3, column=1, sticky=(E, W))

    addition_clear_button = ttk.Button(Subtraction_frame)
    addition_clear_button.configure(text='Clear', command=clear_handler)
    addition_clear_button.grid(row=3, column=2, sticky=(E, W))

    Label_result_strv = StringVar()
    Label_result = Label(result_frame)
    Label_result.configure(textvariable=Label_result_strv)
    Label_result.grid(row=1, column=1, sticky=(E, W))

    for widget in Subtraction_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)

#------------------------------------------------------------------------------------

# Multiplication
def Multiplication():
    def Multiplication_handler():
        try:
            a = float(entry_1_strv.get())
            b = float(entry_2_strv.get())
            result = a * b
            Label_result_strv.set(f"Multiplication : {result}")
        except ValueError:
            messagebox.showerror('Error Messagebox', 'Enter valid details')

    def clear_handler():
        entry_1_strv.set('')
        entry_2_strv.set('')
        Label_result_strv.set('')

    Multiplication_frame = ttk.Frame(root_window)
    Multiplication_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
    Multiplication_frame.grid(row=1, column=1, sticky=(E, W, N, S))
    Multiplication_frame.rowconfigure(1, weight=1)
    Multiplication_frame.columnconfigure(1, weight=1)
    Multiplication_frame.grid_configure(pady=5)

    Label_1 = Label(Multiplication_frame)
    Label_1.configure(text='Enter First Number')
    Label_1.grid(row=1, column=1, sticky=(E, W))

    Label_2 = Label(Multiplication_frame)
    Label_2.configure(text='Enter Second Number')
    Label_2.grid(row=2, column=1, sticky=(E, W))

    entry_1_strv = StringVar()
    Entry_1 = ttk.Entry(Multiplication_frame)
    Entry_1.configure(textvariable=entry_1_strv)
    Entry_1.grid(row=1, column=2, sticky=(E, W))

    entry_2_strv = StringVar()
    Entry_2 = ttk.Entry(Multiplication_frame)
    Entry_2.configure(textvariable=entry_2_strv)
    Entry_2.grid(row=2, column=2, sticky=(E, W))

    addition_button = ttk.Button(Multiplication_frame)
    addition_button.configure(text='Multiplication', command=Multiplication_handler)
    addition_button.grid(row=3, column=1, sticky=(E, W))

    addition_clear_button = ttk.Button(Multiplication_frame)
    addition_clear_button.configure(text='Clear', command=clear_handler)
    addition_clear_button.grid(row=3, column=2, sticky=(E, W))

    Label_result_strv = StringVar()
    Label_result = Label(result_frame)
    Label_result.configure(textvariable=Label_result_strv)
    Label_result.grid(row=1, column=1, sticky=(E, W))

    for widget in Multiplication_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)

#------------------------------------------------------------------------------------------------

# Division
def Division():
    def Division_handler():
        try:
            a = float(entry_1_strv.get())
            b = float(entry_2_strv.get())
            result = a / b
            Label_result_strv.set(f"Division : {result}")
        except ValueError:
            messagebox.showerror('Error Messagebox', 'Enter valid details')

    def clear_handler():
        entry_1_strv.set('')
        entry_2_strv.set('')
        Label_result_strv.set('')

    Division_frame = ttk.Frame(root_window)
    Division_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
    Division_frame.grid(row=1, column=1, sticky=(E, W, N, S))
    Division_frame.rowconfigure(1, weight=1)
    Division_frame.columnconfigure(1, weight=1)
    Division_frame.grid_configure(pady=5)

    Label_1 = Label(Division_frame)
    Label_1.configure(text='Enter First Number')
    Label_1.grid(row=1, column=1, sticky=(E, W))

    Label_2 = Label(Division_frame)
    Label_2.configure(text='Enter Second Number')
    Label_2.grid(row=2, column=1, sticky=(E, W))

    entry_1_strv = StringVar()
    Entry_1 = ttk.Entry(Division_frame)
    Entry_1.configure(textvariable=entry_1_strv)
    Entry_1.grid(row=1, column=2, sticky=(E, W))

    entry_2_strv = StringVar()
    Entry_2 = ttk.Entry(Division_frame)
    Entry_2.configure(textvariable=entry_2_strv)
    Entry_2.grid(row=2, column=2, sticky=(E, W))

    addition_button = ttk.Button(Division_frame)
    addition_button.configure(text='Division', command=Division_handler)
    addition_button.grid(row=3, column=1, sticky=(E, W))

    addition_clear_button = ttk.Button(Division_frame)
    addition_clear_button.configure(text='Clear', command=clear_handler)
    addition_clear_button.grid(row=3, column=2, sticky=(E, W))

    Label_result_strv = StringVar()
    Label_result = Label(result_frame)
    Label_result.configure(textvariable=Label_result_strv)
    Label_result.grid(row=1, column=1, sticky=(E, W))

    for widget in Division_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)
#-----------------------------------------------------------------------------

# Area of Triangle

def area_of_triangle():
    def area_handler():
        try:
            base = float(entry_base_strv.get())
            height = float(entry_height_strv.get())
            area = (1/2)*(base * height)
            Label_result_strv.set(f"Area of a triangle {area} cmSqure")
        except ValueError:
            messagebox.showerror('Error Messagebox', 'Enter valid details')

    def clear_handler():
        entry_base_strv.set('')
        entry_height_strv.set('')
        Label_result_strv.set('')

    Triangle_frame = ttk.Frame(root_window)
    Triangle_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
    Triangle_frame.grid(row=1, column=1, sticky=(E, W, N, S))
    Triangle_frame.rowconfigure(1, weight=1)
    Triangle_frame.columnconfigure(1, weight=1)
    Triangle_frame.grid_configure(pady=5)
    
    Label_base = Label(Triangle_frame)
    Label_base.configure(text='Enter Base Of triangle in cm')
    Label_base.grid(row=1, column=1, sticky=(E, W))

    Label_height = Label(Triangle_frame)
    Label_height.configure(text='Enter Height Of triangle in cm')
    Label_height.grid(row=2, column=1, sticky=(E, W))

    entry_base_strv = StringVar()
    Entry_base = ttk.Entry(Triangle_frame)
    Entry_base.configure(textvariable=entry_base_strv)
    Entry_base.grid(row=1, column=2, sticky=(E, W))

    entry_height_strv = StringVar()
    Entry_height = ttk.Entry(Triangle_frame)
    Entry_height.configure(textvariable=entry_height_strv)
    Entry_height.grid(row=2, column=2, sticky=(E, W))

    area_button = ttk.Button(Triangle_frame)
    area_button.configure(text='Area of Triangle', command=area_handler)
    area_button.grid(row=3, column=1, sticky=(E, W))

    clear_button = ttk.Button(Triangle_frame)
    clear_button.configure(text='Clear', command=clear_handler)
    clear_button.grid(row=3, column=2, sticky=(E, W))

    Label_result_strv = StringVar()
    Label_result = Label(result_frame)
    Label_result.configure(textvariable=Label_result_strv)
    Label_result.grid(row=1, column=1, sticky=(E, W))

    for widget in Triangle_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)

#---------------------------------------------------------------------------

#Simple Interest
def simple_interest():
    def interest():
        try:
            a = float(entry_amount_strv.get())
            r = float(entry_rate_strv.get())
            t = float(entry_time_strv.get())
            I = (a * r * t)/(100)
            Label_result_strv.set(f"Simple Interest Is {I}")
        except ValueError:
            messagebox.showerror('Error Messagebox', 'Enter valid details')

    def clear():
        entry_amount_strv.set('')
        entry_time_strv.set('')
        entry_rate_strv.set('')
        Label_result_strv.set('')
        
    Interest_frame = ttk.Frame(root_window)
    Interest_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
    Interest_frame.grid(row=1, column=1, sticky=(E, W, N, S))
    Interest_frame.rowconfigure(1, weight=1)
    Interest_frame.columnconfigure(1, weight=1)
    Interest_frame.grid_configure(pady=5)

    label_amount = Label(Interest_frame)
    label_amount.configure(text='Enter The Amount')
    label_amount.grid(row=1, column=1, sticky=(E, W))

    label_rate = Label(Interest_frame)
    label_rate.configure(text='Enter The Rate')
    label_rate.grid(row=2, column=1, sticky=(E, W))

    label_time = Label(Interest_frame)
    label_time.configure(text='Enter The Amount')
    label_time.grid(row=3, column=1, sticky=(E, W))

    entry_amount_strv = StringVar()
    entry_amount = ttk.Entry(Interest_frame)
    entry_amount.configure(textvariable=entry_amount_strv)
    entry_amount.grid(row=1, column=2, sticky=(E, W))

    entry_rate_strv = StringVar()
    entry_rate = ttk.Entry(Interest_frame)
    entry_rate.configure(textvariable=entry_rate_strv)
    entry_rate.grid(row=2, column=2, sticky=(E, W))

    entry_time_strv = StringVar()
    entry_time = ttk.Entry(Interest_frame)
    entry_time.configure(textvariable=entry_time_strv)
    entry_time.grid(row=3, column=2, sticky=(E, W))

    interest_button = ttk.Button(Interest_frame)
    interest_button.configure(text='Simple Interest', command=interest)
    interest_button.grid(row=4, column=1, sticky=(E, W))

    clear_button = ttk.Button(Interest_frame)
    clear_button.configure(text='Clear', command=clear)
    clear_button.grid(row=4, column=2, sticky=(E, W))

    Label_result_strv = StringVar()
    Label_result = Label(result_frame)
    Label_result.configure(textvariable=Label_result_strv)
    Label_result.grid(row=1, column=1, sticky=(E, W))

    for widget in Interest_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)

#--------------------------------------------------------------------
# Home

def home_handler():
    display_frame = ttk.Frame(root_window)
    display_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
    display_frame.grid(row=1, column=1, sticky=(E, W, N, S))
    display_frame.rowconfigure(1, weight=1)
    display_frame.columnconfigure(1, weight=1)
    display_frame.grid_configure(pady=5)
    
    label_display = Label(display_frame)
    label_display.configure(text='📱 MINI APPLICATION 📱\n------------------', bg='tan', font='bold')
    label_display.grid(row=1, column=1, sticky=(E, W))

    Label_result = Label(result_frame)
    Label_result.configure(text=(''))
    Label_result.grid(row=1, column=1, sticky=(E, W))

#-----------------------------------------------------------------------------

# Gravitation
def gravitation():
    G = 6.67 * 10**-11

    def compute_handler():
        try:
            m1 = float(entry_object_1_strv.get())
            m2 = float(entry_object_2_strv.get())
            r = float(entry_distance_strv.get())
            F = (G * m1 * m2) / (r ** 2)
            Label_result_strv.set(f"Gravitation Force Is {F} N")
        except ValueError:
            messagebox.showerror('Error Messagebox', 'Enter valid details')

    def clear_handler():
        entry_object_1_strv.set(' ')
        entry_object_2_strv.set(' ')
        entry_distance_strv.set(' ')
        Label_result_strv.set(' ')

    gravitation_frame = ttk.Frame(root_window)
    gravitation_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
    gravitation_frame.grid(row=1, column=1, sticky=(E, W, N, S))
    gravitation_frame.rowconfigure(1, weight=1)
    gravitation_frame.columnconfigure(1, weight=1)
    gravitation_frame.grid_configure(pady=5)

    label_object_1 = Label(gravitation_frame)
    label_object_1.configure(text='Enter mass of object 1 in kgs')
    label_object_1.grid(row=1, column=1, sticky=(E, W))

    label_object_2 = Label(gravitation_frame)
    label_object_2.configure(text='Enter mass of object 2 in kgs')
    label_object_2.grid(row=2, column=1, sticky=(E, W))

    label_distance = Label(gravitation_frame)
    label_distance.configure(text='Enter distance between two objects in kgs')
    label_distance.grid(row=3, column=1, sticky=(E, W))

    button_compute = ttk.Button(gravitation_frame)
    button_compute.configure(text='Compute', command=compute_handler)
    button_compute.grid(row=4, column=1, sticky=(E, W))

    button_clear = ttk.Button(gravitation_frame)
    button_clear.configure(text='Clear', command=clear_handler)
    button_clear.grid(row=4, column=2, sticky=(E, W))

    entry_object_1_strv = StringVar()
    entry_object_1 = ttk.Entry(gravitation_frame)
    entry_object_1.configure(textvariable=entry_object_1_strv)
    entry_object_1.grid(row=1, column=2, sticky=(E, W))

    entry_object_2_strv = StringVar()
    entry_object_2 = ttk.Entry(gravitation_frame)
    entry_object_2.configure(textvariable=entry_object_2_strv)
    entry_object_2.grid(row=2, column=2, sticky=(E, W))

    entry_distance_strv = StringVar()
    entry_distance = ttk.Entry(gravitation_frame)
    entry_distance.configure(textvariable=entry_distance_strv)
    entry_distance.grid(row=3, column=2, sticky=(E, W))

    Label_result_strv = StringVar()
    Label_result = Label(result_frame)
    Label_result.configure(textvariable=Label_result_strv)
    Label_result.grid(row=1, column=1, sticky=(E, W))

    for widget in gravitation_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)
#-------------------------------------------------------------------------

# Meter To Feet
def meter_to_feet():
    def calculate():
        try:
            value = float(feet.get())
            meter_value = int(0.3048 * value * 10000.0 + 0.5)/10000.0
            Label_result_strv.set(f"Meter Value Is {meter_value}")
        except ValueError:
            messagebox.showerror('Error Messagebox', 'Enter valid details')

    def clear_handler():
        feet.set('')
        Label_result_strv.set(' ')

    meter_frame = ttk.Frame(root_window)
    meter_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
    meter_frame.grid(row=1, column=1, sticky=(E, W, N, S))
    meter_frame.rowconfigure(1, weight=1)
    meter_frame.columnconfigure(1, weight=1)
    meter_frame.grid_configure(pady=5)


    feet = StringVar() 
    feet_entry = ttk.Entry(meter_frame)
    feet_entry.configure(textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky=(W,E))

    button_handle = ttk.Button(meter_frame)
    button_handle.configure(text = "Convert", command = calculate) 
    button_handle.grid(column=1, row=3, sticky=(E, W))

    button_clear = ttk.Button(meter_frame)
    button_clear.configure(text='Clear', command=clear_handler)
    button_clear.grid(row=3, column=2, sticky=(E, W))

    feet_label = Label(meter_frame)
    feet_label.configure(text = "Enter Feet For Meter Conversion")
    feet_label.grid(column=1, row=1, sticky=W)

    Label_result_strv = StringVar()
    Label_result = Label(result_frame)
    Label_result.configure(textvariable=Label_result_strv)
    Label_result.grid(row=1, column=1, sticky=(E, W))

    for widget in meter_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)
    
#Main Window
root_window = Tk()
root_window.title('📱 Mini Application 📱')
root_window.configure(bg='pink')
root_window.iconbitmap("My_Icon.ico")

root_window.minsize(300, 300)
root_window.maxsize(500, 500)

display_frame = ttk.Frame(root_window)
display_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
display_frame.grid(row=1, column=1, sticky=(E, W, N, S))
display_frame.rowconfigure(1, weight=1)
display_frame.columnconfigure(1, weight=1)
display_frame.grid_configure(pady=5)

label_display = Label(display_frame)
label_display.configure(text='📱 MINI APPLICATION 📱\n------------------', bg='tan', font='bold')
label_display.grid(row=1, column=1, sticky=(E, W))

main_frame = ttk.Frame(root_window)
main_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
main_frame.grid(row=2, column=1, sticky=(E, W, N, S))
main_frame.rowconfigure(1, weight=1)
main_frame.columnconfigure(1, weight=1)

result_frame = ttk.Frame(root_window)
result_frame.configure(padding='3 3 12 12', borderwidth=10, relief='raised')
result_frame.grid(row=3, column=1, sticky=(E, W, N, S), pady=5)
result_frame.rowconfigure(1, weight=1)
result_frame.columnconfigure(1, weight=1)

label = Label(result_frame)
label.configure(text='')
label.grid(row=1, column=1, sticky=(E, W))

square_button = ttk.Button(main_frame)
square_button.configure(text='Area of Square', command=area_of_square)
square_button.grid(row=1, column=1, sticky=(E, W))

rectangle_button = ttk.Button(main_frame)
rectangle_button.configure(text='Area of Rectangle', command=area_of_rectangle)
rectangle_button.grid(row=1, column=2, sticky=(E, W))

triangle_button = ttk.Button(main_frame)
triangle_button.configure(text='Area of Triangle', command=area_of_triangle)
triangle_button.grid(row=1, column=3, sticky=(E, W))

Addition_button = ttk.Button(main_frame)
Addition_button.configure(text='Addition', command=addition)
Addition_button.grid(row=2, column=1, sticky=(E, W))

Subtraction_button = ttk.Button(main_frame)
Subtraction_button.configure(text='Subtraction', command=subtraction)
Subtraction_button.grid(row=2, column=2, sticky=(E, W))

Division_button = ttk.Button(main_frame)
Division_button.configure(text='Division', command=Division)
Division_button.grid(row=2, column=3, sticky=(E, W))

Multiplication_button = ttk.Button(main_frame)
Multiplication_button.configure(text='Multiplication', command=Multiplication)
Multiplication_button.grid(row=3, column=1, sticky=(E, W))

SimpleInterest_button = ttk.Button(main_frame)
SimpleInterest_button.configure(text='Simple Interest', command=simple_interest)
SimpleInterest_button.grid(row=3, column=2, sticky=(E, W))

Gravitation_button = ttk.Button(main_frame)
Gravitation_button.configure(text='Gravitation', command=gravitation)
Gravitation_button.grid(row=4, column=1, sticky=(E, W))

Home_button = ttk.Button(main_frame)
Home_button.configure(text='Home', command=home_handler)
Home_button.grid(row=4, column=2, sticky=(E, W))

Meter_to_Feet_button = ttk.Button(main_frame)
Meter_to_Feet_button.configure(text='Meter to Feet', command=meter_to_feet)
Meter_to_Feet_button.grid(row=3, column=3, sticky=(E, W))

exit_button = ttk.Button(main_frame)
exit_button.configure(text='Exit', command=exit_handler)
exit_button.grid(row=4, column=3, sticky=(E, W))

for widget in main_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)


root_window.mainloop()
