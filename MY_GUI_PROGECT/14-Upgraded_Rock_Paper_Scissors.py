from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import sys

def choice_fun(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
 
    if computer_choice == "rock":
        computer_label.configure(image=tk_Rockimg)

    elif computer_choice == "paper":
        computer_label.configure(image=tk_Paperimg)

    else:
        computer_label.configure(image=tk_Scissorimg)
  
    if user_choice == computer_choice:
        result = "It's a draw!"

    elif(user_choice == "rock" and computer_choice == "scissors"):
        result = "You Win"

    elif(user_choice == "scissors" and computer_choice == "paper"):
        result = "You Win"

    elif(user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"


    else:
        result = "Computer wins!"

    result_label_strv.set(result)

    

def on_enter(e):
    e.widget['background'] = 'light blue'

def on_leave(e):
    e.widget['background'] = 'grey'

def rock():
    choice_fun("rock") 
    you_label.configure(image=tk_Rockimg)

def paper():
    choice_fun("paper")
    you_label.configure(image=tk_Paperimg)

def Scissors():
    choice_fun("scissors") 
    you_label.configure(image=tk_Scissorimg)

def Exit():
    Exit = messagebox.askyesno("Exit", 'Do You Want To Exit ?')
    if Exit>0:
        root_window.destroy()
        sys.exit()

def Restart():
    restart = messagebox.askyesno("Restart", 'Do You Want To Restart ?')
    if restart>0:
        you_label.configure(image='')
        computer_label.configure(image='') 
        result_label_strv.set("")


root_window = Tk()
root_window.title("Rock, Paper, Scissors")
root_window.iconbitmap("My_Icon.ico")
root_window.geometry("1540x800")
root_window.resizable(True, True)

main_Frame = Frame(root_window) 
main_Frame.configure(
                        bd=3, 
                        relief='raised', 
                        bg="pink"
                    )
main_Frame.place(x=300, y=0, width=800, height=350)

button_Frame = Frame(root_window)
button_Frame.configure(
                bd=3, 
                relief='raised', 
                bg="pink"
            )
button_Frame.place(x=300, y=350, width=800, height=400)

button_Frame1 = Frame(button_Frame)
button_Frame1.configure(
                            bd=3, 
                            relief='raised', 
                            bg="pink", 
                            cursor="hand2"
                        )
button_Frame1.place(x=1, y=1, width=800, height=279)

button_Frame2 = Frame(button_Frame)
button_Frame2.configure(
                            bd=3, 
                            relief='raised', 
                            bg="tan"
                        )
                            
button_Frame2.place(x=1, y=280, width=800, height=105)

you_Frame = LabelFrame(main_Frame) 
you_Frame.configure(
                        bd=3, 
                        relief='raised', 
                        bg="pink",
                        text="You", 
                        font=("Garamond",20, "bold")
                    )
you_Frame.place(x=20, y=30, width=300, height=300)

computer_Frame = LabelFrame(main_Frame)
computer_Frame.configure(
                            text="Computer", 
                            font=("Garamond",20, "bold"),
                            bd=3,
                            relief='raised', 
                            bg="pink"
                        )
computer_Frame.place(x=480, y=30, width=300, height=300)

you_label = Label(
                    you_Frame, 
                    bg="pink"
                )
you_label.pack()

computer_label = Label(
                        computer_Frame, 
                        bg="pink"
                    )
computer_label.pack()

vs_label = Label(main_Frame)
vs_label.configure(
                    text="VS", 
                    font=("Garamond",40, "bold")
                )
vs_label.place(x=340, y=160, width=100, height=60)

Rockimg = Image.open("rock.png")
resize_Rockimg = Rockimg.resize((200, 200))
tk_Rockimg = ImageTk.PhotoImage(resize_Rockimg)

Paperimg = Image.open("paper.png")
resize_Paperimg = Paperimg.resize((200, 200))
tk_Paperimg = ImageTk.PhotoImage(resize_Paperimg)

Scissorimg = Image.open("Scissors.png")
resize_Scissorimg = Scissorimg.resize((200, 200))
tk_Scissorimg = ImageTk.PhotoImage(resize_Scissorimg)

Rockimg1 = Image.open("rock.png")
resize_Rockimg1 = Rockimg1.resize((150, 150))
tk_Rockimg1 = ImageTk.PhotoImage(resize_Rockimg1)

Paperimg1 = Image.open("paper.png")
resize_Paperimg1 = Paperimg1.resize((150, 150))
tk_Paperimg1 = ImageTk.PhotoImage(resize_Paperimg1)

Scissorimg1 = Image.open("Scissors.png")
resize_Scissorimg1 = Scissorimg1.resize((150, 150))
tk_Scissorimg1 = ImageTk.PhotoImage(resize_Scissorimg1)

style = ttk.Style()
style.configure("Custom.TButton",
                font=("Garamond", 15))

Button_rock = Button(button_Frame1)
Button_rock.configure(
                        image=tk_Rockimg1, 
                        command=rock,
                        bg="grey"
                    )
Button_rock.grid(row=1, column=1, padx=50, pady=25, sticky="nsew")

Button_paper = Button(button_Frame1)
Button_paper.configure( 
                        image=tk_Paperimg1, 
                        command=paper, 
                        bg="grey"
                    )
Button_paper.grid(row=1, column=2, padx=50, pady=25, sticky="nsew")

Button_Scissor = Button(button_Frame1)
Button_Scissor.configure(
                            image=tk_Scissorimg1, 
                            command=Scissors, 
                            bg="grey"
                        )
Button_Scissor.grid(row=1, column=3, padx=50, pady=25, sticky="nsew")

Button_clear = ttk.Button(button_Frame1)
Button_clear.configure(
                        command=Restart, 
                        text="Restart", 
                        style="Custom.TButton"
                    )
Button_clear.grid(row=2, column=1, padx=50, pady=25, sticky="nsew")

Button_exit = ttk.Button(button_Frame1)
Button_exit.configure(
                        command=Exit, 
                        text="Exit", 
                        style="Custom.TButton"
                    )
Button_exit.grid(row=2, column=2, padx=50, pady=25, sticky="nsew")

Button_rock.bind("<Enter>", on_enter)
Button_rock.bind("<Leave>", on_leave)

Button_paper.bind("<Enter>", on_enter)
Button_paper.bind("<Leave>", on_leave)

Button_Scissor.bind("<Enter>", on_enter)
Button_Scissor.bind("<Leave>", on_leave)

result_label_strv = StringVar()
result_label = Label(button_Frame2)
result_label.configure(
                        textvariable=result_label_strv, 
                        font=("Garamond",40, "bold"), 
                        bg="tan"
                    )
result_label.pack()


root_window.mainloop()
