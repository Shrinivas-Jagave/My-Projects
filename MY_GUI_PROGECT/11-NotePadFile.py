from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import sys

root_window = Tk()
root_window.title("NotePad")
root_window.iconbitmap("My_Icon.ico")
root_window.geometry("1540x800")
root_window.resizable(True, True)

def save():
    notepad_content = text.get("1.0", "end-1c")
    
    file_path = filedialog.asksaveasfilename(
                                                defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                                                title="Save As"
                                            )
    
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(notepad_content)
            f.close()
            label.config(
                            text=os.path.basename(file_path), 
                            font=("Garamond",13, "bold")
                        )
        messagebox.showinfo("Student Information", "Data Saved Successfully")
   

def Exit():
    Exit = messagebox.askyesno("Exit", 'Do You Want To Exit ?')
    if Exit>0:
        root_window.destroy()
        sys.exit()

def clear():
    reset = messagebox.askyesno("Notepad", 'Do You Want To Clear ?')
    if reset>0:
        text.delete("1.0", "end-1c")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete("1.0", END)
            text.insert(END, content)
            label.config(
                            text=os.path.basename(file_path), 
                            font=("Garamond",13, "bold")
                        )


def help():
    messagebox.showinfo("Help", "Help")

def about():
    messagebox.showinfo("About", 
                        "This is a Notepad\n" \
                        "Made By : Jyoti Jagave\n" \
                        "\tRohit Jagave\n" \
                        "\tShrinivas Jagave\n" \
                        "Shrikant Tate" \
                        "Using Tkinter Python")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def cut():
    text.event_generate("<<Cut>>")

def bold_font():
    selected_font = combox_1_strv.get()
    selected_size = combox_2_strv.get()
    if Toggle.get():
        text.configure(font=(selected_font, selected_size, "normal"))
        Toggle.set(False)
    else:
        text.configure(font=(selected_font, selected_size, "bold"))
        Toggle.set(True)

def italic_font():
    selected_font = combox_1_strv.get()
    selected_size = combox_2_strv.get()
    if Toggle.get():
        text.configure(font=(selected_font, selected_size, "normal"))
        Toggle.set(False)
    else:
        text.configure(font=(selected_font, selected_size, "italic"))
        Toggle.set(True)

def update_font():
    selected_font = combox_1_strv.get()
    selected_size = combox_2_strv.get()
    text.configure(font=(selected_font, int(selected_size)))

def new():
  label.config(
                    text="Untitled",
                    font=("Garamond",12, "bold")
                )
  text.delete("1.0", END)

def red_colour():
    text.config(fg="red")

def green_colour():
    text.config(fg="green")

def blue_colour():
    text.config(fg="blue")

def yellow_colour():
    text.config(fg="yellow")

def orange_colour():
    text.config(fg="orange")

def black_colour():
    text.config(fg="black")

def pink_colour():
    text.config(fg="pink")

def purple_colour():
    text.config(fg="purple")

def skyblue_colour():
    text.config(fg="sky blue")

def cyan_colour():
    text.config(fg="cyan")

def orchid_colour():
    text.config(fg="orchid")

def olive_colour():
    text.config(fg="olive")

def magenta_colour():
    text.config(fg="magenta")


Menu_Frame = LabelFrame(root_window)
Menu_Frame.configure(
                        bd=2, 
                        relief='sunken', 
                        text="File Name", 
                        font=("Garamond",12, "bold")
                    )
Menu_Frame.place(x=0, y=0, width=350, height=50)

font_Frame = LabelFrame(root_window)
font_Frame.configure( 
                        bd=2, 
                        relief='sunken', 
                        text="Fonts", 
                        font=("Garamond",12, "bold")
                    )
font_Frame.place(x=350, y=0, width=900, height=50)

Colour_Frame = LabelFrame(root_window)
Colour_Frame.configure(
                        bd=2, 
                        relief='sunken', 
                        text="Colours", 
                        font=("Garamond",12, "bold")
                    )
Colour_Frame.place(x=900, y=0, width=930, height=50)

Text_Frame = Frame(root_window)
Text_Frame.configure(
                        bd=3, 
                        relief='raised', 
                        bg="red"
                    )
Text_Frame.place(x=0, y=50, width=1370, height=760)

text = Text(Text_Frame)
text.configure(
                undo=True,
            )
text.place(x=0, y=0, width=1360, height=760)
Toggle = BooleanVar(value=False)

label = Label(Menu_Frame)
label.configure(
                    text="Untitled", 
                    font=("Garamond",12, "bold")
                )
label.grid(row=1, column=1, padx=5, pady=2, sticky='nsew')

combox_1_strv = StringVar()
combox_1 = ttk.Combobox(font_Frame)
combox_1.configure(textvariable=combox_1_strv, width=35)
combox_1["values"] = (
                        "MS Gothic", 
                        "MS PGothic", 
                        "MS UI Gothic", 
                        "Malgun Gothic", 
                        "Malgun Gothic Semilight",
                        "Microsoft JhengHei",
                        "Microsoft JhengHei Light", 
                        "Microsoft JhengHei UI",
                        "Microsoft JhengHei UI Light",
                        "Microsoft YaHei", 
                        "Microsoft YaHei Light", 
                        "Microsoft YaHei UI", 
                        "Microsoft YaHei UI Light",
                        "MingLiU-ExtB", 
                        "MingLiU_HKSCS-ExtB", 
                        "MingLiU_MSCS-ExtB", 
                        "NSimSun", 
                        "PMingLiU-ExtB",
                        "SimSun",
                        "SimSun-ExtB", 
                        "SimSun-ExtG", 
                        "Yu Gothic", 
                        "Yu Gothic Light", 
                        "Yu Gothic Medium", 
                        "Yu Gothic UI",
                        "Yu Gothic UI Light", 
                        "Yu Gothic UI Semibold", 
                        "Yu Gothic UI Semilight", 
                        "Arabic Transparent",
                        "Arial", "Arial Baltic", 
                        "Arial Black", "Arial CE",
                        "Arial CYR", 
                        "Arial Greek", 
                        "Arial TUR",
                        "Bahnschrift", 
                        "Bahnschrift Condensed", 
                        "Bahnschrift Light", 
                        "Bahnschrift Light Condensed",
                        "Bahnschrift Light SemiCondensed", 
                        "Bahnschrift SemiBold", 
                        "Bahnschrift SemiBold Condensed",
                        "Bahnschrift SemiBold SemiConden", 
                        "Bahnschrift SemiCondensed", 
                        "Bahnschrift SemiLight",
                        "Bahnschrift SemiLight Condensed", 
                        "Bahnschrift SemiLight SemiConde", 
                        "Calibri", 
                        "Calibri Light",
                        "Cambria", 
                        "Cambria Math", 
                        "Candara", 
                        "Candara Light", 
                        "Cascadia Code", 
                        "Cascadia Code ExtraLight",
                        "Cascadia Code Light", 
                        "Cascadia Code SemiBold", 
                        "Cascadia Code SemiLight", 
                        "Cascadia Mono",
                        "Cascadia Mono ExtraLight",
                        "Cascadia Mono Light", 
                        "Cascadia Mono SemiBold", 
                        "Cascadia Mono SemiLight",
                        "Comic Sans MS", 
                        "Consolas", 
                        "Constantia", 
                        "Corbel", 
                        "Corbel Light", 
                        "Courier", 
                        "Courier New",
                        "Courier New Baltic",
                        "Courier New CE", 
                        "Courier New CYR", 
                        "Courier New Greek", 
                        "Courier New TUR",
                        "Ebrima", 
                        "Fixedsys", 
                        "Franklin Gothic Medium", 
                        "Gabriola", 
                        "Gadugi", 
                        "Georgia", 
                        "Impact", 
                        "Ink Free",
                        "Javanese Text", 
                        "Leelawadee UI", 
                        "Leelawadee UI Semilight", 
                        "Lucida Console", 
                        "Lucida Sans Unicode",
                        "MS Sans Serif", 
                        "MS Serif", 
                        "MV Boli", 
                        "Marlett", 
                        "Microsoft Himalaya", 
                        "Microsoft New Tai Lue",
                        "Microsoft PhagsPa", 
                        "Microsoft Sans Serif", 
                        "Microsoft Tai Le", 
                        "Microsoft Yi Baiti", 
                        "Modern",
                        "Mongolian Baiti", 
                        "Myanmar Text", 
                        "Nirmala Text", 
                        "Nirmala Text Semilight", 
                        "Nirmala UI",
                        "Nirmala UI Semilight", 
                        "Palatino Linotype", 
                        "Roman", 
                        "Sans Serif Collection", 
                        "Script",
                        "Segoe Fluent Icons", 
                        "Segoe MDL2 Assets", 
                        "Segoe Print", 
                        "Segoe Script", 
                        "Segoe UI",
                        "Segoe UI Black", 
                        "Segoe UI Emoji", 
                        "Segoe UI Historic", 
                        "Segoe UI Light", 
                        "Segoe UI Semibold",
                        "Segoe UI Semilight", 
                        "Segoe UI Symbol", 
                        "Segoe UI Variable Display", 
                        "Segoe UI Variable Display Light",
                        "Segoe UI Variable Display Semib", 
                        "Segoe UI Variable Display Semil", 
                        "Segoe UI Variable Small",
                        "Segoe UI Variable Small Light", 
                        "Segoe UI Variable Small Semibol", 
                        "Segoe UI Variable Small Semilig",
                        "Segoe UI Variable Text", 
                        "Segoe UI Variable Text Light", 
                        "Segoe UI Variable Text Semibold",
                        "Segoe UI Variable Text Semiligh", 
                        "Sitka Banner", 
                        "Sitka Banner Semibold",
                        "Sitka Display",
                        "Sitka Display Semibold", 
                        "Sitka Heading", 
                        "Sitka Heading Semibold", 
                        "Sitka Small",
                        "Sitka Small Semibold", 
                        "Sitka Subheading", 
                        "Sitka Subheading Semibold", 
                        "Sitka Text",
                        "Sitka Text Semibold", 
                        "Small Fonts", 
                        "Sylfaen", 
                        "Symbol", 
                        "System", 
                        "Tahoma", 
                        "Terminal",
                        "Times New Roman", 
                        "Times New Roman Baltic", 
                        "Times New Roman CE", 
                        "Times New Roman CYR",
                        "Times New Roman Greek", 
                        "Times New Roman TUR", 
                        "Trebuchet MS", 
                        "Verdana", 
                        "Webdings", 
                        "Wingdings"
)
combox_1.set("Arial")
combox_1.grid(row=1, column=3, padx=5, pady=2, sticky='nsew')

combox_2_strv = StringVar()
combox_2 = ttk.Combobox(font_Frame) 
combox_2.configure(textvariable=combox_2_strv, width=5)
combox_2["values"] = (
                        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                        11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
                        41, 42, 43, 44, 45, 46, 47, 48, 49, 50
)
combox_2.set(11)
combox_2.grid(row=1, column=4, padx=5, pady=2, sticky='nsew')

combox_1.bind("<<ComboboxSelected>>", lambda e: update_font())
combox_2.bind("<<ComboboxSelected>>", lambda e: update_font())

#-------------------Menubar 1 for file-------------------
menubar = Menu(root_window)
menubar_1_files = Menu(menubar, tearoff=0)
menubar_1_files.add_command(label="New", command=new)
menubar_1_files.add_command(label="Open", command=open_file)
menubar_1_files.add_command(label="Save", command=save)
menubar_1_files.add_separator()
menubar_1_files.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=menubar_1_files)

#--------------------Menubar 2 for edit-----------
menubar_2_files = Menu(menubar, tearoff=0)
menubar_2_files.add_command(label="Copy", command=copy)
menubar_2_files.add_command(label="Cut", command=cut)
menubar_2_files.add_command(label="Paste", command=paste)
menubar_2_files.add_separator()
menubar_2_files.add_command(label="Clear", command=clear)
menubar.add_cascade(label="Edit", menu=menubar_2_files)

#--------------------Menubar 2 for edit-----------
menubar_3_files = Menu(menubar, tearoff=0)
menubar_3_files.add_command(label="About", command=about)
menubar_3_files.add_command(label="Help", command=help)
menubar.add_cascade(label="Help", menu=menubar_3_files)

root_window.config(menu=menubar)

bold_button = ttk.Button(font_Frame)
bold_button.configure(
                        text="Bold", 
                        command=bold_font
                    )
bold_button.grid(row=1, column=1, padx=5, pady=2, sticky='nsew')

italic_button = ttk.Button(font_Frame)
italic_button.configure(
                            text="Italic", 
                            command=italic_font
                        )
italic_button.grid(row=1, column=2, padx=5, pady=2, sticky='nsew')

colour_Button_1 = Button(Colour_Frame)
colour_Button_1.configure(
                            height=1, 
                            width=2, 
                            bg="red", 
                            command=red_colour
                        )
colour_Button_1.grid(row=1, column=1, padx=5, pady=2, sticky='nsew')

colour_Button_2 = Button(Colour_Frame)
colour_Button_2.configure(
                            height=1, 
                            width=2, 
                            bg="blue", 
                            command=blue_colour
                        )
colour_Button_2.grid(row=1, column=2, padx=5, pady=2, sticky='nsew')

colour_Button_3 = Button(Colour_Frame)
colour_Button_3.configure(
                            height=1, 
                            width=2, 
                            bg="green", 
                            command=green_colour
                        )
colour_Button_3.grid(row=1, column=3, padx=5, pady=2, sticky='nsew')

colour_Button_4 = Button(Colour_Frame)
colour_Button_4.configure(
                            height=1, 
                            width=2, 
                            bg="yellow", 
                            command=yellow_colour
                        )
colour_Button_4.grid(row=1, column=4, padx=5, pady=2, sticky='nsew')

colour_Button_5 = Button(Colour_Frame)
colour_Button_5.configure(
                            height=1, 
                            width=2, 
                            bg="black", 
                            command=black_colour
                        )
colour_Button_5.grid(row=1, column=5, padx=5, pady=2, sticky='nsew')

colour_Button_6 = Button(Colour_Frame)
colour_Button_6.configure(
                            height=1, 
                            width=2, 
                            bg="orange", 
                            command=orange_colour
                        )
colour_Button_6.grid(row=1, column=6, padx=5, pady=2, sticky='nsew')

colour_Button_7 = Button(Colour_Frame)
colour_Button_7.configure(
                            height=1, 
                            width=2, 
                            bg="pink", 
                            command=pink_colour
                        )
colour_Button_7.grid(row=1, column=7, padx=5, pady=2, sticky='nsew')

colour_Button_8 = Button(Colour_Frame)
colour_Button_8.configure(
                            height=1, 
                            width=2, 
                            bg="purple", 
                            command=purple_colour
                        )
colour_Button_8.grid(row=1, column=8, padx=5, pady=2, sticky='nsew')

colour_Button_9 = Button(Colour_Frame)
colour_Button_9.configure(
                            height=1, 
                            width=2, 
                            bg="sky blue", 
                            command=skyblue_colour
                        )
colour_Button_9.grid(row=1, column=9, padx=5, pady=2, sticky='nsew')

colour_Button_10 = Button(Colour_Frame)
colour_Button_10.configure(
                            height=1, 
                            width=2, 
                            bg="cyan", 
                            command=cyan_colour
                        )
colour_Button_10.grid(row=1, column=10, padx=5, pady=2, sticky='nsew')

colour_Button_11 = Button(Colour_Frame)
colour_Button_11.configure(
                            height=1, 
                            width=2, 
                            bg="magenta", 
                            command=magenta_colour
                        )
colour_Button_11.grid(row=1, column=11, padx=5, pady=2, sticky='nsew')

colour_Button_12 = Button(Colour_Frame)
colour_Button_12.configure(
                            height=1, 
                            width=2, 
                            bg="orchid", 
                            command=orchid_colour
                        )
colour_Button_12.grid(row=1, column=12, padx=5, pady=2, sticky='nsew')

colour_Button_13 = Button(Colour_Frame)
colour_Button_13.configure(
                            height=1, 
                            width=2, 
                            bg="olive", 
                            command=olive_colour
                        )
colour_Button_13.grid(row=1, column=13, padx=5, pady=2, sticky='nsew')

redo_Button = Button(font_Frame)
redo_Button.configure(
                        text="↷",
                        height=1,
                        width=2,
                        command=text.edit_redo,
                        bg='grey',
                        font=('Arial',11, "bold")
                    )
redo_Button.grid(row=1, column=6, padx=2, pady=1, sticky='nsew')

undo_Button = Button(font_Frame)
undo_Button.configure(
                        text="↶",
                        height=1, 
                        width=2,
                        command=text.edit_undo,
                        bg="grey",
                        font=("Arial", 11,"bold")    
                    )
undo_Button.grid(row=1, column=5, padx=2, pady=1, sticky='nsew')

Scrollbar_y = ttk.Scrollbar(text)
Scrollbar_y.pack(side=RIGHT, fill=Y)
Scrollbar_y.config(command=text.yview)
text.config(yscrollcommand=Scrollbar_y.set)

text.bind("<Control-z>", lambda event: text.edit_undo())
text.bind("<Control-y>", lambda event: text.edit_redo())
text.bind("<Control-b>", lambda event: bold_font())
text.bind("<Control-i>", lambda event: italic_font())
text.bind("<Control-s>", lambda event: save())
text.bind("<Control-o>", lambda event: open_file())

for col in range(5):  
    root_window.grid_columnconfigure(col, weight=1)

for row in range(7):  
    root_window.grid_rowconfigure(row, weight=1)

root_window.mainloop()
