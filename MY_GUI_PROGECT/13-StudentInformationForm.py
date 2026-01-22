from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sys

def clear():
    reset = messagebox.askyesno("Student Information", 'Do You Want To Reset ?')
    if reset>0:
        text_view.delete("1.0", "end-1c")
        entry_1_strv.set("")
        entry_2_strv.set("")
        entry_3_strv.set("")
        entry_4_strv.set("")
        entry_5_strv.set("")
        entry_6_strv.set("")
        entry_7_strv.set("")
        entry_8_strv.set("")
        entry_9_strv.set("")
        entry_10_strv.set("")
        entry_11_strv.set("")
        entry_12_strv.set("")
        entry_13_strv.set("")
        entry_14_strv.set("")
        entry_15_strv.set("")
        entry_16_strv.set("")
        entry_17_strv.set("")
        entry_18_strv.set("")
        entry_19_strv.set("")
        entry_20_strv.set("")
        entry_21_strv.set("")
        entry_22_strv.set("")
        entry_23_strv.set("")
        entry_24_strv.set("")
        entry_25_strv.set("")
        entry_26_strv.set("")
        entry_27_strv.set("")



def Exit():
    Exit = messagebox.askyesno("Student Information", 'Do You Want To Exit ?')
    if Exit>0:
        root_window.destroy()
        sys.exit()



def SaveData():
    requiredEntries = (
                        entry_27_strv.get(),
                        entry_25_strv.get(),
                        entry_23_strv.get(),
                        entry_21_strv.get(),
                        entry_20_strv.get(),
                        entry_11_strv.get(),
                        entry_10_strv.get(),
                        entry_9_strv.get(),
                        entry_8_strv.get(),
                        entry_6_strv.get(),
                        entry_5_strv.get(),
                        entry_4_strv.get(),
                        entry_3_strv.get(),
                        entry_2_strv.get(),
                        entry_1_strv.get()
    )
    if any(entries.strip() == "" for entries in requiredEntries):
        messagebox.showerror("Error", "Please fill in * fields.")
    else:
        StudentData = text_view.get("1.0", "end-1c")
        file_path = filedialog.asksaveasfilename(
                                                    defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                                                    title="Save As"
                                                    )
        
    if file_path: 
        text_view.delete("1.0", "end-1c")
        view()
        with open(file_path, 'w') as f:
            f.write(StudentData)
            f.close()
            messagebox.showinfo("Student Information", "Data Saved Susscefully")

    else:
        messagebox.showerror("Student Information", "Data Not Saved")




def view():
    requiredEntries = (
                         entry_27_strv.get(),
                         entry_25_strv.get(),
                         entry_23_strv.get(),
                         entry_21_strv.get(),
                         entry_20_strv.get(),
                         entry_11_strv.get(),
                         entry_10_strv.get(),
                         entry_9_strv.get(),
                         entry_8_strv.get(),
                         entry_6_strv.get(),
                         entry_5_strv.get(),
                         entry_4_strv.get(),
                         entry_3_strv.get(),
                         entry_2_strv.get(),
                         entry_1_strv.get()
    )
    if any(entries.strip() == "" for entries in requiredEntries):
        messagebox.showerror("Error", "Please fill in * fields.")
    else:
        text_view.insert(END, "Student First Name : " + entry_1_strv.get()+"\n")
        text_view.insert(END, "Student Middle Name : " + entry_2_strv.get()+"\n")
        text_view.insert(END, "Student Last Name : " + entry_3_strv.get()+"\n")
        text_view.insert(END, "Email : " + entry_4_strv.get()+"\n")
        text_view.insert(END, "Contact Number : " + entry_5_strv.get()+"\n")
        text_view.insert(END, "Current Address : " + entry_6_strv.get()+"\n")
        text_view.insert(END, "Permenant Address : " + entry_7_strv.get()+"\n")
        text_view.insert(END, "RollNo : " + entry_8_strv.get()+"\n")
        text_view.insert(END, "Batch : " + entry_9_strv.get()+"\n")
        text_view.insert(END, "D.O.B : " + entry_10_strv.get()+"\n")
        text_view.insert(END, "Gender : " + entry_11_strv.get()+"\n")
        text_view.insert(END, "Refered By : " + entry_12_strv.get()+"\n")
        text_view.insert(END, "Qualification : " + entry_13_strv.get()+"\n")
        text_view.insert(END, "Nationality : " + entry_14_strv.get()+"\n")
        text_view.insert(END, "Religion : " + entry_15_strv.get()+"\n")
        text_view.insert(END, "Category : " + entry_16_strv.get()+"\n")
        text_view.insert(END, "Blood Group : " + entry_17_strv.get()+"\n")
        text_view.insert(END, "Adhar Card Number : " + entry_18_strv.get()+"\n")
        text_view.insert(END, "Pan Card Number : " + entry_19_strv.get()+"\n")
        text_view.insert(END, "Emergency Contact : " + entry_20_strv.get()+"\n")
        text_view.insert(END, "Father FullName : " + entry_21_strv.get()+"\n")
        text_view.insert(END, "Father Occupation : " + entry_22_strv.get()+"\n")
        text_view.insert(END, "Father Contact Number : " + entry_23_strv.get()+"\n")
        text_view.insert(END, "Annual Income : " + entry_24_strv.get()+"\n")
        text_view.insert(END, "Mother Full Name : " + entry_25_strv.get()+"\n")
        text_view.insert(END, "Mother Occupation : " + entry_26_strv.get()+"\n")
        text_view.insert(END, "Mother Contact Number : " + entry_27_strv.get()+"\n")



def Add():
    pass



def Delete():
    pass



def update():
    pass



root_window = Tk()
root_window.title("Student Information")
root_window.iconbitmap("My_Icon.ico")
root_window.configure(bg='pink')
root_window.geometry("1540x800")



headinglabel = Label(root_window)
headinglabel.configure(
                        bd=7, 
                        relief=RIDGE,
                        text="* Core Code Programming Academy *", 
                        fg="#E59E41", 
                        font=("Garamond",20, "bold")
                    )
headinglabel.pack(side=TOP, fill=X)




Label_Frame = LabelFrame(root_window)
Label_Frame.configure(
                        bd=3, 
                        relief='raised', 
                        text="Student Information \t\t\t\t\t\t\t\t\t\t\t\t\t"
                        "(* fields are compulsary to fill)")
Label_Frame.place(x=0, y=50, width=930, height=540)




view_Frame = LabelFrame(root_window)
view_Frame.configure( 
                        bd=3, 
                        relief='raised',
                        text="Pre-View"
                    )
view_Frame.place(x=933, y=50, width=425, height=370)




table_Frame = LabelFrame(root_window)
table_Frame.configure( 
                        bd=3, 
                        relief='raised', 
                        text="Table"
                    )
table_Frame.place(x=933, y=420, width=425, height=320)



Buttons_Frame = Frame(root_window)
Buttons_Frame.configure(
                            bd=3, 
                            relief='raised', 
                            cursor='hand2'
                        )
Buttons_Frame.place(x=0, y=597, width=930, height=140)



style = ttk.Style()
style.configure("Custom.TButton",
                font=("Garamond", 15))



Button_add = ttk.Button(Buttons_Frame)
Button_add.configure(
                        text="Add Data", 
                        style="Custom.TButton"
                        
                    )
Button_add.grid(row=1, column=1, sticky=(E, W, N, S), padx=20, pady=5)



Button_view = ttk.Button(Buttons_Frame)
Button_view.configure(
                        text="Pre-View", 
                        style="Custom.TButton",
                        command=view
                    )
Button_view.grid(row=1, column=2, sticky=(E, W, N, S), padx=20, pady=5)



Button_Update = ttk.Button(Buttons_Frame)
Button_Update.configure(
                            text="Update", 
                            style="Custom.TButton"
                        )
Button_Update.grid(row=1, column=3, sticky=(E, W, N, S), padx=20, pady=5)



Button_Delete = ttk.Button(Buttons_Frame)
Button_Delete.configure(
                            text="Delete", 
                            style="Custom.TButton"
                        )
Button_Delete.grid(row=1, column=4, sticky=(E, W, N, S), padx=20, pady=5)




Button_Reset = ttk.Button(Buttons_Frame)
Button_Reset.configure(
                        text="Reset", 
                        style="Custom.TButton", 
                        command=clear
                    )
Button_Reset.grid(row=1, column=5, sticky=(E, W, N, S), padx=20, pady=5)




Button_Exit = ttk.Button(Buttons_Frame)
Button_Exit.configure(
                        text="Exit",
                        style="Custom.TButton", 
                        command=Exit
                    )
Button_Exit.grid(row=2, column=2, sticky=(E, W, N, S), padx=20, pady=5)




Button_Save = ttk.Button(Buttons_Frame)
Button_Save.configure(
                        text="Save", 
                        style="Custom.TButton",
                        command=SaveData
                    )
Button_Save.grid(row=2, column=1, sticky=(E, W, N, S), padx=20, pady=5)




text_view = Text(view_Frame)
text_view.configure(font=("Garamond",12, "bold"))
text_view.place(x=0, y=0, width=420, height=370)



Scrollbar_y = ttk.Scrollbar(text_view)
Scrollbar_y.pack(side=RIGHT, fill=Y)
Scrollbar_y.config(command=text_view.yview)
text_view.config(yscrollcommand=Scrollbar_y.set)



label_1 = Label(Label_Frame)
label_1.configure(
                    text="Student First Name :", 
                    font=("Garamond",12, "bold")
                )
label_1.grid(row=1, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_2 = Label(Label_Frame)
label_2.configure(
                    text="Student Middle Name : ", 
                    font=("Garamond",12, "bold")
                )
label_2.grid(row=2, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_3 = Label(Label_Frame)
label_3.configure(
                    text="Student Last Name : ", 
                    font=("Garamond",12, "bold")
                )
label_3.grid(row=3, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_4 = Label(Label_Frame)
label_4.configure(
                    text="Email : ", 
                    font=("Garamond",12, "bold")
                )
label_4.grid(row=4, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_5 = Label(Label_Frame)
label_5.configure(
                    text="Contact Number : ", 
                    font=("Garamond",12, "bold")
                )
label_5.grid(row=5, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_6 = Label(Label_Frame)
label_6.configure(
                    text="Current Address : ", 
                    font=("Garamond",12, "bold")
                )
label_6.grid(row=6, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_7 = Label(Label_Frame)
label_7.configure(
                    text="Permenant Address : ", 
                    font=("Garamond",12, "bold")
                 )
label_7.grid(row=7, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_8 = Label(Label_Frame)
label_8.configure(
                    text="Roll No. : ", 
                    font=("Garamond",12, "bold")
                )
label_8.grid(row=8, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_9 = Label(Label_Frame)
label_9.configure(
                    text="Batch : ", 
                    font=("Garamond",12, "bold")
                )
label_9.grid(row=9, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_10 = Label(Label_Frame)
label_10.configure(
                    text="D.O.B : ", 
                    font=("Garamond",12, "bold")
                )
label_10.grid(row=10, column=1, sticky=(E, W, N, S), padx=5, pady=5)




label_11 = Label(Label_Frame)
label_11.configure(
                    text="Gender : ", 
                    font=("Garamond",12, "bold")
                )
label_11.grid(row=11, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_12 = Label(Label_Frame)
label_12.configure(
                    text="Refered By : ", 
                    font=("Garamond",12, "bold")
                )
label_12.grid(row=12, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_13 = Label(Label_Frame)
label_13.configure(
                    text="Qualification : ", 
                    font=("Garamond",12, "bold")
                )
label_13.grid(row=13, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_14 = Label(Label_Frame)
label_14.configure(
                    text="Nationality : ", 
                    font=("Garamond",12, "bold")                   
                )
label_14.grid(row=14, column=1, sticky=(E, W, N, S), padx=5, pady=5)



label_15 = Label(Label_Frame)
label_15.configure(
                        text="Religion : ", 
                        font=("Garamond",12, "bold")
                  )
label_15.grid(row=1, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_16 = Label(Label_Frame)
label_16.configure(
                    text="Category : ", 
                    font=("Garamond",12, "bold")
                )
label_16.grid(row=2, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_17 = Label(Label_Frame)
label_17.configure(
                        text="Blood Group : ", 
                        font=("Garamond",12, "bold")
                    )
label_17.grid(row=3, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_18 = Label(Label_Frame)
label_18.configure(
                    text="Adhar Card Number : ", 
                    font=("Garamond",12, "bold")
                )
label_18.grid(row=4, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_19 = Label(Label_Frame)
label_19.configure(
                    text="Pan Card Number : ", 
                    font=("Garamond",12, "bold")
                )
label_19.grid(row=5, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_20 = Label(Label_Frame)
label_20.configure(
                    text="Emergency Contact Details : ", 
                    font=("Garamond",12, "bold")
                )
label_20.grid(row=6, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_21 = Label(Label_Frame)
label_21.configure(
                    text="Father Full Name : ", 
                    font=("Garamond",12, "bold")
                )
label_21.grid(row=7, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_22 = Label(Label_Frame)
label_22.configure(
                    text="Father Occupation : ", 
                    font=("Garamond",12, "bold")
                )
label_22.grid(row=8, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_23 = Label(Label_Frame)
label_23.configure(     
                    text="Father Contact Number : ", 
                    font=("Garamond",12, "bold")
                )
label_23.grid(row=9, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_24 = Label(Label_Frame)
label_24.configure(
                    text="Annual Income : ", 
                    font=("Garamond",12, "bold")
                )
label_24.grid(row=10, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_25 = Label(Label_Frame)
label_25.configure(
                    text="Mother Full Name : ", 
                    font=("Garamond",12, "bold")
                )
label_25.grid(row=11, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_26 = Label(Label_Frame)
label_26.configure(
                    text="Mother Occupation : ", 
                    font=("Garamond",12, "bold")
                )
label_26.grid(row=12, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_27 = Label(Label_Frame)
label_27.configure(
                    text="Mother Contact Number : ", 
                    font=("Garamond",12, "bold")
                )
label_27.grid(row=13, column=3, sticky=(E, W, N, S), padx=5, pady=5)



label_1_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_1_star.grid(row=1, column=1, padx=(165, 0))



label_2_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_2_star.grid(row=2, column=1, padx=(177, 0))



label_3_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_3_star.grid(row=3, column=1, padx=(160, 0))



label_4_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_4_star.grid(row=4, column=1, padx=(60, 0))



label_5_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_5_star.grid(row=5, column=1, padx=(140, 0))



label_6_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_6_star.grid(row=6, column=1, padx=(140, 0))



label_8_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_8_star.grid(row=8, column=1, padx=(77, 0))



label_9_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_9_star.grid(row=9, column=1, padx=(60, 0))



label_10_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_10_star.grid(row=10, column=1, padx=(60, 0))



label_11_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_11_star.grid(row=11, column=1, padx=(70, 0))



label_20_star = Label(
                        Label_Frame, text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_20_star.grid(row=6, column=3, padx=(223, 0))



label_21_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"),
                        fg="red"
                    )
label_21_star.grid(row=7, column=3, padx=(145, 0))



label_23_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_23_star.grid(row=9, column=3, padx=(195, 0))



label_25_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_25_star.grid(row=11, column=3, padx=(150, 0))



label_27_star = Label(
                        Label_Frame, 
                        text="*", 
                        font=("Garamond",12, "bold"), 
                        fg="red"
                    )
label_27_star.grid(row=13, column=3, padx=(195, 0))



entry_1_strv = StringVar()
entry_1 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_1.configure(textvariable=entry_1_strv)
entry_1.grid(row=1, column=2)



entry_2_strv = StringVar()
entry_2 = ttk.Entry(
                       Label_Frame, 
                       font=("Garamond",10, "bold"), 
                       width=25
                    )
entry_2.configure(textvariable=entry_2_strv)
entry_2.grid(row=2, column=2)



entry_3_strv = StringVar()
entry_3 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_3.configure(textvariable=entry_3_strv)
entry_3.grid(row=3, column=2)



entry_4_strv = StringVar()
entry_4 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_4.configure(textvariable=entry_4_strv)
entry_4.grid(row=4, column=2)



entry_5_strv = StringVar()
entry_5 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_5.configure(textvariable=entry_5_strv)
entry_5.grid(row=5, column=2)




entry_6_strv = StringVar()
entry_6 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25                       
                    )
entry_6.configure(textvariable=entry_6_strv)
entry_6.grid(row=6, column=2)



entry_7_strv = StringVar()
entry_7 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_7.configure(textvariable=entry_7_strv)
entry_7.grid(row=7, column=2)



entry_8_strv = StringVar()
entry_8 = ttk.Entry(
                       Label_Frame,
                       textvariable=entry_8_strv, 
                       font=("Garamond",10, "bold"), 
                       width=25
                    )
entry_8.configure(textvariable=entry_8_strv)
entry_8.grid(row=8, column=2)



entry_9_strv = StringVar()
entry_9 = ttk.Combobox(
                            Label_Frame, 
                            textvariable=entry_9_strv,
                            font=("Garamond",10, "bold"), 
                            width=25
                        )
entry_9["values"] = ("C", "Python", "C++", "DSA In Python", "DSA In C And C++")
entry_9.grid(row=9, column=2)




entry_10_strv = StringVar()
entry_10 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_10.configure(textvariable=entry_10_strv)
entry_10.grid(row=10, column=2)



entry_11_strv = StringVar()
entry_11 = ttk.Combobox(
                            Label_Frame,
                            textvariable=entry_11_strv, 
                            font=("Garamond",10, "bold"),
                            width=25
                        )
entry_11["values"] = ("Male", "Female", "Other")
entry_11.grid(row=11, column=2)



entry_12_strv = StringVar()
entry_12 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_12.configure(textvariable=entry_12_strv)
entry_12.grid(row=12, column=2)



entry_13_strv = StringVar()
entry_13 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_13.configure(textvariable=entry_13_strv)
entry_13.grid(row=13, column=2)



entry_14_strv = StringVar()
entry_14 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_14.configure(textvariable=entry_14_strv)
entry_14.grid(row=14, column=2)



entry_15_strv = StringVar()
entry_15 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"),
                        width=25
                    )
entry_15.configure(textvariable=entry_15_strv)
entry_15.grid(row=1, column=4)



entry_16_strv = StringVar()
entry_16 = ttk.Combobox(
                            Label_Frame, 
                            textvariable=entry_16_strv, 
                            font=("Garamond",10, "bold"), 
                            width=25
                        )
entry_16["values"] = ("General", "OBC", "SC", "ST", "EWS")
entry_16.grid(row=2, column=4)



entry_17_strv = StringVar()
entry_17 = ttk.Combobox(
                            Label_Frame, 
                            textvariable=entry_17_strv, 
                            font=("Garamond",10, "bold"), 
                            width=25
                        )
entry_17["values"] = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
entry_17.grid(row=3, column=4)



entry_18_strv = StringVar()
entry_18 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_18.configure(textvariable=entry_18_strv)
entry_18.grid(row=4, column=4)




entry_19_strv = StringVar()
entry_19 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_19.configure(textvariable=entry_19_strv)
entry_19.grid(row=5, column=4)



entry_20_strv = StringVar()
entry_20 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_20.configure(textvariable=entry_20_strv)
entry_20.grid(row=6, column=4)



entry_21_strv = StringVar()
entry_21 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_21.configure(textvariable=entry_21_strv)
entry_21.grid(row=7, column=4)



entry_22_strv = StringVar()
entry_22 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_22.configure(textvariable=entry_22_strv)
entry_22.grid(row=8, column=4)



entry_23_strv = StringVar()
entry_23 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_23.configure(textvariable=entry_23_strv)
entry_23.grid(row=9, column=4)



entry_24_strv = StringVar()
entry_24 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_24.configure(textvariable=entry_24_strv)
entry_24.grid(row=10, column=4)



entry_25_strv = StringVar()
entry_25 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_25.configure(textvariable=entry_25_strv)
entry_25.grid(row=11, column=4)



entry_26_strv = StringVar()
entry_26 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25                  
                    )
entry_26.configure(textvariable=entry_26_strv)
entry_26.grid(row=12, column=4)



entry_27_strv = StringVar()
entry_27 = ttk.Entry(
                        Label_Frame, 
                        font=("Garamond",10, "bold"), 
                        width=25
                    )
entry_27.configure(textvariable=entry_27_strv)
entry_27.grid(row=13, column=4)



data_table = ttk.Treeview(table_Frame, columns=(
                                                    "StudentFirstName",
                                                    "StudentMiddleName",
                                                    "StudentLastName",
                                                    "Email",
                                                    "ContactNumber",
                                                    "CurrentAddress",
                                                    "PermenantAddress",
                                                    "RollNo",
                                                    "Batch",
                                                    "D.O.B",
                                                    "Gender",
                                                    "ReferedBy",
                                                    "Qualification",
                                                    "Nationality",
                                                    "Religion",
                                                    "Category",
                                                    "BloodGroup",
                                                    "AdharCardNumber",
                                                    "PanCardNumber",
                                                    "EmergencyContact",
                                                    "FatherFullName",
                                                    "FatherOccupation",
                                                    "FatherContactNumber",
                                                    "AnnualIncome",
                                                    "MotherFullName",
                                                    "MotherOccupation",
                                                    "MotherContactNumber"
                                                ))



data_table.heading("StudentFirstName",text="Student First Name")
data_table.heading("StudentMiddleName",text="Student Middle Name")
data_table.heading("StudentLastName",text="Student Last Name")
data_table.heading("Email",text="Email")
data_table.heading("ContactNumber",text="Contact Number")
data_table.heading("CurrentAddress",text="Current Address")
data_table.heading("PermenantAddress",text="Permenant Address")
data_table.heading("RollNo",text="Roll No")
data_table.heading("Batch",text="Batch")
data_table.heading("D.O.B",text="D.O.B")
data_table.heading("Gender",text="Gender")
data_table.heading("ReferedBy",text="Refered By")
data_table.heading("Qualification",text="Qualification")
data_table.heading("Nationality",text="Nationality")
data_table.heading("Religion",text="Religion")
data_table.heading("Category",text="Category")
data_table.heading("BloodGroup",text="Blood Group")
data_table.heading("AdharCardNumber", text="Adhar Card Number")
data_table.heading("PanCardNumber", text="Pan Card Number")
data_table.heading("EmergencyContact", text="Emergency Contact")
data_table.heading("FatherFullName", text="Father Full Name")
data_table.heading("FatherOccupation", text="Father Occupation")
data_table.heading("FatherContactNumber", text="Father Contact Number")
data_table.heading("AnnualIncome", text="Annual Income")
data_table.heading("MotherFullName", text="Mother Full Name")
data_table.heading("MotherOccupation", text="Mother Occupation")
data_table.heading("MotherContactNumber", text="Mother Contact Number")


data_table["show"] = "headings"
data_table.pack(fill=BOTH, expand=1)


data_table.column("StudentFirstName", width=120)
data_table.column("StudentMiddleName", width=120)
data_table.column("StudentLastName", width=120)
data_table.column("Email", width=70)
data_table.column("ContactNumber", width=70)
data_table.column("CurrentAddress", width=100)
data_table.column("PermenantAddress", width=100)
data_table.column("RollNo", width=60)
data_table.column("Batch", width=60)
data_table.column("D.O.B", width=60)
data_table.column("Gender", width=60)
data_table.column("ReferedBy", width=100)
data_table.column("Qualification", width=100)
data_table.column("Nationality", width=80)
data_table.column("Religion", width=70)
data_table.column("Category", width=70)
data_table.column("BloodGroup", width=70)
data_table.column("AdharCardNumber", width=100)
data_table.column("PanCardNumber", width=100)
data_table.column("EmergencyContact", width=100)
data_table.column("FatherFullName", width=100)
data_table.column("FatherOccupation", width=100)
data_table.column("FatherContactNumber", width=120)
data_table.column("AnnualIncome", width=100)
data_table.column("MotherFullName", width=100)
data_table.column("MotherOccupation", width=100)
data_table.column("MotherContactNumber", width=120)

Scrollbar_x = ttk.Scrollbar(data_table, orient=HORIZONTAL)
Scrollbar_x.pack(side=BOTTOM, fill=X)
Scrollbar_x.config(command=data_table.xview)
data_table.config(xscrollcommand=Scrollbar_x.set)

Scrollbar_y = ttk.Scrollbar(data_table, orient=VERTICAL)
Scrollbar_y.pack(side=RIGHT, fill=Y)
Scrollbar_y.config(command=data_table.yview)
data_table.config(yscrollcommand=Scrollbar_y.set)

root_window.mainloop()
