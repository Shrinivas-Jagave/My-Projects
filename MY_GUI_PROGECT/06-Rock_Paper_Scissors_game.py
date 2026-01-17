from tkinter import * 
from tkinter import ttk 
import sys 
import random


def choice_fun(user):
    choices = ['✂', '✋🏻', '👊🏻']
    r = random.choice(choices)
    label_2_strv.set(r)

    if r == user:
        result = "Its Tie Between you and computer"
    elif(user == "👊🏻" and r == "✂"):
        result = "Wow !! You Win The Game"

    elif(user == "✂" and r == "✋🏻"):
        result = "Wow !! You Win The Game"

    elif(user == "✋🏻" and r == "👊🏻"):
        result = "Wow !! You Win The Game"

    else:
        result = "Computer Win Try Again"
    

    label_5_strv.set(result)

def paper():
    choice_fun("✋🏻")
    label_1_strv.set("✋🏻")

def stone():
    choice_fun("👊🏻")
    label_1_strv.set("👊🏻")
       
def scissor():  
    choice_fun("✂")
    label_1_strv.set("✂")

def exit():
    sys.exit()

def restart():
    label_1_strv.set("")
    label_2_strv.set("")
    label_5_strv.set("")


root_window = Tk()
root_window.title("Rock, Paper, Scissor Game")
root_window.iconbitmap("My_Icon.ico")
root_window.configure(bg='pink')

upper_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief=RIDGE)
upper_frame.grid(column=1, row=1, sticky=(N,W,E,S))


you_frame = ttk.Frame(upper_frame, padding="3 3 12 12",  borderwidth=10, relief='raised')
you_frame.grid(column=1, row=2, sticky=(N,W,E,S))

com_frame = ttk.Frame(upper_frame, padding="3 3 12 12",  borderwidth=10, relief='raised')
com_frame.grid(column=3, row=2, sticky=(N,W,E,S))

result_frame = ttk.Frame(root_window, padding="3 3 12 12",  borderwidth=10, relief='raised')
result_frame.grid(column=1, row=2, sticky=(N,W,E,S))

label_1_strv = StringVar()
label_1 = Label(you_frame)
label_1.grid(column=1, row=2, sticky=(N,W,E,S))
label_1.configure(textvariable=label_1_strv)

label_2_strv = StringVar()
label_2 = Label(com_frame)
label_2.grid(column=2, row=2, sticky=(N,W,E,S))
label_2.configure(textvariable=label_2_strv )

label_3 = Label(upper_frame)
label_3.grid(column=1, row=1, sticky=(N,W,E,S))
label_3.configure(text='You')

label_4 = Label(upper_frame)
label_4.grid(column=3, row=1, sticky=(N,W,E,S))
label_4.configure(text='Com')

label_6 = Label(upper_frame)
label_6.grid(column=2, row=2, sticky=(N,W,E,S))
label_6.configure(text='vs')

label_5_strv = StringVar()
label_5 = Label(result_frame)
label_5.grid(column=1, row=3, sticky=(N,W,E,S))
label_5.configure(textvariable=label_5_strv, font=("bold"), fg="red",text="Result")


lower_frame = ttk.Frame(root_window, padding="3 3 12 12",  borderwidth=10, relief='sunken')
lower_frame.grid(column=1, row=3, sticky=(N,W,E,S))


stone_button = ttk.Button(lower_frame)
stone_button.configure(text="👊🏻", command=stone)
stone_button.grid(column=1, row=1, sticky=(E,W,N,S))

paper_button = ttk.Button(lower_frame)
paper_button.configure(text="✋🏻", command=paper)
paper_button.grid(column=2, row=1, sticky=(E,W,N,S))

scissor_button = ttk.Button(lower_frame)
scissor_button.configure(text="✂",  command=scissor)
scissor_button.grid(column=3, row=1, sticky=(E,W,N,S))

exit_button = ttk.Button(lower_frame)
exit_button.configure(text="Exit",  command=exit)
exit_button.grid(column=2, row=2, sticky=(E,W,N,S))

restart_button = ttk.Button(lower_frame)
restart_button.configure(text="Restart",  command=restart)
restart_button.grid(column=1, row=2, sticky=(E,W,N,S))


for frames in root_window.winfo_children(): 
    frames.grid_configure(padx=3, pady=1)
    for widget in frames.winfo_children(): 
        widget.grid_configure(padx=5, pady=5)
        
root_window.mainloop()
