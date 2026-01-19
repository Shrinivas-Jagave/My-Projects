from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys

root_window = Tk()
root_window.title("String Demo")
root_window.configure(bg='pink')
root_window.iconbitmap("My_Icon.ico")

main_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
main_frame.grid(row=1, column=1, sticky=(E, W, N, S))

Button_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
Button_frame.grid(row=2, column=1, sticky=(E, W, N, S))        

def Info_handler():
    messagebox.showinfo("Info", "🧠 About This Application\n" \
    "Multi-Operations Tool\n" \
    "This application is designed to help users perform a variety of basic operations \n" \
    "on Lists, Tuples, and Strings using a simple and interactive graphical interface.\n\n----------------------------------------\n" \
    "✅ List Operations\n* Append elements\n* Sort (Ascending / Descending)\n* Reverse list\n* Copy / Clear / Clear All\n* View input/output in real time\n\n" \
    "--------------------------------\n" \
    "✅ Tuple Operations\n* Append items\n* Sort / Reverse\n* Find max/min values\n* Repeat elements\n* Copy / Clear / Clear All.\n\n" \
    "---------------------------\n" \
    "✅ String Operations\n* Concatenation / Repetition\n* Reverse / Copy\n* Index access / Length\n"
    "* Case transformations (Upper, Lower, Capitalize)\n* Replace / Remove\n* Strip / Find / Count\n* Start with / End with\n\n" \
    "-----------------------------------\n" \
    "🔄 Home & Exit Buttons\n* Use the Home button to return to the main menu or Exit to close the application.\n\n" \
    "----------------------------------------------------------------------------------------------------------\n" \
    "📝 All outputs are dynamically displayed to help you visualize the results of your operations.")

def List():
    def Home():
        main_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
        main_frame.grid(row=1, column=1, sticky=(E, W, N, S))

        Button_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
        Button_frame.grid(row=2, column=1, sticky=(E, W, N, S))

        disciption_label = ttk.Label(main_frame)
        disciption_label.configure(text="Multi-Operations Application \n For More Info Click Info Button",
                                    font=("Arial", 20), foreground="Black", background="Yellow")
        disciption_label.grid(row=1, column=1)

        label = ttk.Label(main_frame)
        label.configure(text="")
        label.grid(row=2, column=1, sticky=(E, W, N, S))

        Info_button = ttk.Button(main_frame)
        Info_button.configure(text="Info", command=Info_handler)
        Info_button.grid(row=3, column=1)

        list_button = ttk.Button(Button_frame)
        list_button.configure(text="List Operations", command=List)
        list_button.grid(row=2, column=1, sticky=(E, W, N, S))

        Tuple_button = ttk.Button(Button_frame)
        Tuple_button.configure(text="Tuple Operations", command=Tuple)
        Tuple_button.grid(row=1, column=2, sticky=(E, W, N, S))

        String_button = ttk.Button(Button_frame)
        String_button.configure(text="String Operations", command=String)
        String_button.grid(row=1, column=1, sticky=(E, W, N, S))

        Exit_button = ttk.Button(Button_frame)
        Exit_button.configure(text="Exit", command=Exit)
        Exit_button.grid(row=2, column=2, sticky=(E, W, N, S))

        List_frame.destroy()
        List_2_frame.destroy()
        List_button_frame.destroy()
        List_output_frame.destroy()

    def safe_eval():
            try:
                return eval(entry_list_strv.get())
            except:
                messagebox.showerror("Error", "Invalid input format. Use Python list syntax.")
                return []

    def Append():
        def Append_2():
            try:
                List = safe_eval()
                enter_by_user_label_strv.set(f"{List}")
                append = int(append_entry_strv.get())
                List.append(append)
                output_label_strv.set(f"{List}")
                output_label_1_strv.set(type(List))
                append_button.destroy()
                append_entry.destroy()
                append_label.destroy()
            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        append_label = ttk.Label(List_frame)
        append_label.configure(text="Append = ", foreground="Blue")
        append_label.grid(row=3, column=1, sticky=(E, W, N, S))

        append_entry_strv = StringVar()
        append_entry = ttk.Entry(List_frame)
        append_entry.configure(textvariable=append_entry_strv)
        append_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        append_button = ttk.Button(List_frame)
        append_button.configure(text="Append", command=Append_2)
        append_button.grid(row=4, column=1, sticky=(E, W, N, S))

    def repetition():
        def repetition_2():
            try:
                List = safe_eval()
                enter_by_user_label_strv.set(f"{List}")
                repetition = int(repetition_entry_strv.get())
                # List.append(",")
                output_label_strv.set(f"{List*repetition}")
                output_label_1_strv.set(type(List))
                repetition_button.destroy()
                repetition_entry.destroy()
                repetition_label.destroy()
            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        repetition_label = ttk.Label(List_frame)
        repetition_label.configure(text="Repetition Count = ", foreground="Blue")
        repetition_label.grid(row=3, column=1, sticky=(E, W, N, S))

        repetition_entry_strv = StringVar()
        repetition_entry = ttk.Entry(List_frame)
        repetition_entry.configure(textvariable=repetition_entry_strv)
        repetition_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        repetition_button = ttk.Button(List_frame)
        repetition_button.configure(text="Repetition", command=repetition_2)
        repetition_button.grid(row=4, column=1, sticky=(E, W, N, S))

    def sort_ascending():
        try:
            List = safe_eval()
            enter_by_user_label_strv.set(f"{List}")
            List.sort()
            output_label_strv.set(f"{List}")
            output_label_1_strv.set(type(List))
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def sort_descending():
        try:
            List = safe_eval()
            enter_by_user_label_strv.set(f"{List}")
            # List = [x for x in List if x != ","]
            List.sort(reverse=True)
            output_label_strv.set(f"{List}")
            output_label_1_strv.set(type(List))
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def Reverse():
        List = safe_eval()
        enter_by_user_label_strv.set(f"{List}")
        List.reverse()
        output_label_strv.set(f"{List}")
        output_label_1_strv.set(type(List))
        
    def Copy():
        List = safe_eval()
        enter_by_user_label_strv.set(f"{List}")
        List.copy()
        output_label_strv.set(f"{List}")
        output_label_1_strv.set(type(List))


    def clear():
        entry_list_strv.set("")
        output_label_strv.set("")
        enter_by_user_label_strv.set("")
        output_label_1_strv.set("")

    def Clear_list_button():
        try:
            List = safe_eval()
            enter_by_user_label_strv.set(f"{List}")
            List.clear()
            output_label_strv.set(f"{List}")
            output_label_1_strv.set(type(List))
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")
        
    List_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    List_frame.grid(row=1, column=1, sticky=(E, W, N, S))

    List_2_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    List_2_frame.grid(row=2, column=1, sticky=(E, W, N, S))

    List_output_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    List_output_frame.grid(row=3, column=1, sticky=(E, W, N, S))

    List_button_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    List_button_frame.grid(row=4, column=1, sticky=(E, W, N, S))

    entry_label = ttk.Label(List_frame)
    entry_label.configure(text="Enter List = ", foreground="red")
    entry_label.grid(row=1, column=1, sticky=(E, W, N, S))

    entry_1_label = ttk.Label(List_frame)
    entry_1_label.configure(text=" ")
    entry_1_label.grid(row=2, column=1, sticky=(E, W, N, S))

    out_label = ttk.Label(List_output_frame)
    out_label.configure(text="Output : ", font=(10), foreground="red")
    out_label.grid(row=1, column=1, sticky=(E, W, N, S))

    by_you_label = ttk.Label(List_2_frame)
    by_you_label.configure(text="Enter By You List :", font=(10), foreground="red")
    by_you_label.grid(row=1, column=1, sticky=(E, W, N, S))

    entry_list_strv = StringVar()
    entry_list = ttk.Entry(List_frame, width=50)
    entry_list.configure(textvariable=entry_list_strv)
    entry_list.grid(row=1, column=2, sticky=(E, W, N, S), )

    enter_by_user_label_strv = StringVar()
    enter_by_user_label = ttk.Label(List_2_frame)
    enter_by_user_label.configure(textvariable=enter_by_user_label_strv)
    enter_by_user_label.grid(row=2, column=1, sticky=(E, W, N, S))

    enter_by_user_label_1_strv = StringVar()
    enter_by_user_label_1 = ttk.Label(List_2_frame)
    enter_by_user_label_1.configure(textvariable=enter_by_user_label_1_strv)
    enter_by_user_label_1.grid(row=3, column=2, sticky=(E, W, N, S))

    output_label_strv = StringVar()
    output_label = ttk.Label(List_output_frame)
    output_label.configure(textvariable=output_label_strv, font=("arial",  15))
    output_label.grid(row=2, column=1, sticky=(E, W, N, S))

    output_label_1_strv = StringVar()
    output_1_label = ttk.Label(List_output_frame)
    output_1_label.configure(textvariable=output_label_1_strv)
    output_1_label.grid(row=3, column=1, sticky=(E, W, N, S))

    append_button = ttk.Button(List_button_frame)
    append_button.configure(text="Append", command=Append)
    append_button.grid(row=1, column=1, sticky=(E, W, N, S))

    sort_ascending_button = ttk.Button(List_button_frame)
    sort_ascending_button.configure(text="Sort_ascending", command=sort_ascending)
    sort_ascending_button.grid(row=1, column=2, sticky=(E, W, N, S))

    sort_descending_button = ttk.Button(List_button_frame)
    sort_descending_button.configure(text="Sort_descending", command=sort_descending)
    sort_descending_button.grid(row=1, column=3, sticky=(E, W, N, S))

    reverse_button = ttk.Button(List_button_frame)
    reverse_button.configure(text="Reverse", command=Reverse)
    reverse_button.grid(row=2, column=1, sticky=(E, W, N, S))

    clear_list_button = ttk.Button(List_button_frame)
    clear_list_button.configure(text="Empty List", command=Clear_list_button)
    clear_list_button.grid(row=2, column=2, sticky=(E, W, N, S))

    copy_button = ttk.Button(List_button_frame)
    copy_button.configure(text="Copy", command=Copy)
    copy_button.grid(row=2, column=3, sticky=(E, W, N, S))

    repetition_button = ttk.Button(List_button_frame)
    repetition_button.configure(text="Repetition", command=repetition)
    repetition_button.grid(row=3, column=1, sticky=(E, W, N, S))

    clear_button = ttk.Button(List_button_frame)
    clear_button.configure(text="Clear All", command=clear)
    clear_button.grid(row=3, column=2, sticky=(E, W, N, S))

    exit_button = ttk.Button(List_button_frame)
    exit_button.configure(text="Exit", command=exit)
    exit_button.grid(row=3, column=3, sticky=(E, W, N, S))

    Home_button = ttk.Button(List_button_frame)
    Home_button.configure(text="Home", command=Home)
    Home_button.grid(row=4, column=1, sticky=(E, W, N, S))
    messagebox.showinfo("Info", "While Entering List Elements Please Use [ ] Squre Brackets")


    
def Tuple():
    def Home():
        main_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
        main_frame.grid(row=1, column=1, sticky=(E, W, N, S))

        Button_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
        Button_frame.grid(row=2, column=1, sticky=(E, W, N, S))

        disciption_label = ttk.Label(main_frame)
        disciption_label.configure(text="This Is Multi-Operations Application \n For More Info Click Info Button",
                                    font=("Arial", 20), foreground="Black", background="Yellow")
        disciption_label.grid(row=1, column=1)

        label = ttk.Label(main_frame)
        label.configure(text="")
        label.grid(row=2, column=1, sticky=(E, W, N, S))

        Info_button = ttk.Button(main_frame)
        Info_button.configure(text="Info", command=Info_handler)
        Info_button.grid(row=3, column=1)

        list_button = ttk.Button(Button_frame)
        list_button.configure(text="List Operations", command=List)
        list_button.grid(row=2, column=1, sticky=(E, W, N, S))

        Tuple_button = ttk.Button(Button_frame)
        Tuple_button.configure(text="Tuple Operations", command=Tuple)
        Tuple_button.grid(row=1, column=2, sticky=(E, W, N, S))

        String_button = ttk.Button(Button_frame)
        String_button.configure(text="String Operations", command=String)
        String_button.grid(row=1, column=1, sticky=(E, W, N, S))

        Exit_button = ttk.Button(Button_frame)
        Exit_button.configure(text="Exit", command=Exit)
        Exit_button.grid(row=2, column=2, sticky=(E, W, N, S))

        Tuple_button_frame.destroy()
        Tuple_output_frame.destroy()
        Tuple_2_frame.destroy()
        Tuple_frame.destroy()

    def get_tuple():
        user_input = entry_Tuple_strv.get()
        return eval(user_input) 
    
    def update_output(result):
        output_label_strv.set(str(result))
        output_label_1_strv.set(str(type(result)))

    def Append_tuple():
        def Append_2():
            try:
                my_tuple =get_tuple()
                enter_by_user_label_strv.set(my_tuple)
                append = int(append_entry_strv.get())
                latest_tuple = my_tuple + (append,)
                update_output(latest_tuple)
                append_button.destroy()
                append_entry.destroy()
                append_label.destroy()
            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        append_label = ttk.Label(Tuple_frame)
        append_label.configure(text="Append = ", foreground="Blue")
        append_label.grid(row=3, column=1, sticky=(E, W, N, S))

        append_entry_strv = StringVar()
        append_entry = ttk.Entry(Tuple_frame)
        append_entry.configure(textvariable=append_entry_strv)
        append_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        append_button = ttk.Button(Tuple_frame)
        append_button.configure(text="Append", command=Append_2)
        append_button.grid(row=4, column=1, sticky=(E, W, N, S))

    def sort_ascending_tuple():
        try:
            my_tuple = get_tuple()
            my_tuple = tuple(my_tuple)
            enter_by_user_label_strv.set(my_tuple)
            sorted_tuple = tuple(sorted(my_tuple))
            update_output(sorted_tuple)
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def sort_descending_tuple():
        try:
            my_tuple = get_tuple()
            my_tuple = tuple(sorted(my_tuple, reverse=True))
            enter_by_user_label_strv.set(my_tuple)
            update_output(my_tuple)
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def Reverse():
        try:
            my_tuple = get_tuple()
            update_output(my_tuple[::-1])
            enter_by_user_label_strv.set(my_tuple)
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def Clear_tuple_button():
        try:
            my_tuple = get_tuple()
            enter_by_user_label_strv.set(my_tuple)
            output_label_strv.set("()")
            output_label_1_strv.set(type(my_tuple))
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def Copy():
        try:
            my_tuple = get_tuple()
            update_output(my_tuple)
            enter_by_user_label_strv.set(my_tuple)
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def maxi():
        try:
            my_tuple = get_tuple()
            update_output(max(my_tuple))
            enter_by_user_label_strv.set(my_tuple)
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def mini():
        try:
            my_tuple = get_tuple()
            update_output(min(my_tuple))
            enter_by_user_label_strv.set(my_tuple)
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def clear():
        output_label_1_strv.set("")
        output_label_strv.set("")
        enter_by_user_label_strv.set("")
        entry_Tuple_strv.set("")

    def repetition():
        def repetition_2():
            try:
                my_tuple = get_tuple()
                enter_by_user_label_strv.set(my_tuple)
                repetition = int(repetition_entry_strv.get())
                update_output(my_tuple * repetition)
                repetition_button.destroy()
                repetition_entry.destroy()
                repetition_label.destroy()
            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        repetition_label = ttk.Label(Tuple_frame)
        repetition_label.configure(text="Repetition Count = ", foreground="Blue")
        repetition_label.grid(row=3, column=1, sticky=(E, W, N, S))

        repetition_entry_strv = StringVar()
        repetition_entry = ttk.Entry(Tuple_frame)
        repetition_entry.configure(textvariable=repetition_entry_strv)
        repetition_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        repetition_button = ttk.Button(Tuple_frame)
        repetition_button.configure(text="Repetition", command=repetition_2)
        repetition_button.grid(row=4, column=1, sticky=(E, W, N, S))
            


    Tuple_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    Tuple_frame.grid(row=1, column=1, sticky=(E, W, N, S))

    Tuple_2_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    Tuple_2_frame.grid(row=2, column=1, sticky=(E, W, N, S))

    Tuple_output_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    Tuple_output_frame.grid(row=3, column=1, sticky=(E, W, N, S))

    Tuple_button_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    Tuple_button_frame.grid(row=4, column=1, sticky=(E, W, N, S))

    entry_label = ttk.Label(Tuple_frame)
    entry_label.configure(text="Enter Tuple = ", foreground="red")
    entry_label.grid(row=1, column=1, sticky=(E, W, N, S))

    entry_1_label = ttk.Label(Tuple_frame)
    entry_1_label.configure(text=" ")
    entry_1_label.grid(row=2, column=1, sticky=(E, W, N, S))

    out_label = ttk.Label(Tuple_output_frame)
    out_label.configure(text="Output : ", font=(10), foreground="red")
    out_label.grid(row=1, column=1, sticky=(E, W, N, S))

    by_you_label = ttk.Label(Tuple_2_frame)
    by_you_label.configure(text="Enter By You Tuple :", font=(10), foreground="red")
    by_you_label.grid(row=1, column=1, sticky=(E, W, N, S))

    entry_Tuple_strv = StringVar()
    entry_Tuple = ttk.Entry(Tuple_frame, width=50)
    entry_Tuple.configure(textvariable=entry_Tuple_strv)
    entry_Tuple.grid(row=1, column=2, sticky=(E, W, N, S), )

    enter_by_user_label_strv = StringVar()
    enter_by_user_label = ttk.Label(Tuple_2_frame)
    enter_by_user_label.configure(textvariable=enter_by_user_label_strv)
    enter_by_user_label.grid(row=2, column=1, sticky=(E, W, N, S))

    enter_by_user_label_1_strv = StringVar()
    enter_by_user_label_1 = ttk.Label(Tuple_2_frame)
    enter_by_user_label_1.configure(textvariable=enter_by_user_label_1_strv)
    enter_by_user_label_1.grid(row=3, column=2, sticky=(E, W, N, S))

    output_label_strv = StringVar()
    output_label = ttk.Label(Tuple_output_frame)
    output_label.configure(textvariable=output_label_strv, font=(15))
    output_label.grid(row=2, column=1, sticky=(E, W, N, S))

    output_label_1_strv = StringVar()
    output_1_label = ttk.Label(Tuple_output_frame)
    output_1_label.configure(textvariable=output_label_1_strv)
    output_1_label.grid(row=3, column=1, sticky=(E, W, N, S))

    append_button = ttk.Button(Tuple_button_frame)
    append_button.configure(text="Append", command=Append_tuple)
    append_button.grid(row=1, column=1, sticky=(E, W, N, S))

    sort_ascending_button = ttk.Button(Tuple_button_frame)
    sort_ascending_button.configure(text="Sort_ascending", command=sort_ascending_tuple)
    sort_ascending_button.grid(row=1, column=2, sticky=(E, W, N, S))

    sort_descending_button = ttk.Button(Tuple_button_frame)
    sort_descending_button.configure(text="Sort_descending", command=sort_descending_tuple)
    sort_descending_button.grid(row=1, column=3, sticky=(E, W, N, S))

    reverse_button = ttk.Button(Tuple_button_frame)
    reverse_button.configure(text="Reverse", command=Reverse)
    reverse_button.grid(row=2, column=1, sticky=(E, W, N, S))

    clear_tuple_button = ttk.Button(Tuple_button_frame)
    clear_tuple_button.configure(text="Empty Tuple", command=Clear_tuple_button)
    clear_tuple_button.grid(row=2, column=2, sticky=(E, W, N, S))

    copy_button = ttk.Button(Tuple_button_frame)
    copy_button.configure(text="Copy", command=Copy)
    copy_button.grid(row=2, column=3, sticky=(E, W, N, S))

    max_button = ttk.Button(Tuple_button_frame)
    max_button.configure(text="Maximum", command=maxi)
    max_button.grid(row=3, column=1, sticky=(E, W, N, S))

    min_button = ttk.Button(Tuple_button_frame)
    min_button.configure(text="Minimum", command=mini)
    min_button.grid(row=3, column=2, sticky=(E, W, N, S))

    repetition_button = ttk.Button(Tuple_button_frame)
    repetition_button.configure(text="Repetition", command=repetition)
    repetition_button.grid(row=3, column=3, sticky=(E, W, N, S))

    clear_button = ttk.Button(Tuple_button_frame)
    clear_button.configure(text="Clear All", command=clear)
    clear_button.grid(row=4, column=1, sticky=(E, W, N, S))

    exit_button = ttk.Button(Tuple_button_frame)
    exit_button.configure(text="Exit", command=exit)
    exit_button.grid(row=4, column=2, sticky=(E, W, N, S))

    Home_button = ttk.Button(Tuple_button_frame)
    Home_button.configure(text="Home", command=Home)
    Home_button.grid(row=4, column=3, sticky=(E, W, N, S))
    messagebox.showinfo("Info", "While Entering Tuple Elements Please Use ( ) Circular Brackets")

def String():
    def Home():
        main_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
        main_frame.grid(row=1, column=1, sticky=(E, W, N, S))

        Button_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
        Button_frame.grid(row=2, column=1, sticky=(E, W, N, S))

        disciption_label = ttk.Label(main_frame)
        disciption_label.configure(text="This Is Multi-Operations Application \n For More Info Click Info Button",
                                    font=("Arial", 20), foreground="Black", background="Yellow")
        disciption_label.grid(row=1, column=1)

        label = ttk.Label(main_frame)
        label.configure(text="")
        label.grid(row=2, column=1, sticky=(E, W, N, S))

        Info_button = ttk.Button(main_frame)
        Info_button.configure(text="Info", command=Info_handler)
        Info_button.grid(row=3, column=1)

        list_button = ttk.Button(Button_frame)
        list_button.configure(text="List Operations", command=List)
        list_button.grid(row=2, column=1, sticky=(E, W, N, S))

        Tuple_button = ttk.Button(Button_frame)
        Tuple_button.configure(text="Tuple Operations", command=Tuple)
        Tuple_button.grid(row=1, column=2, sticky=(E, W, N, S))

        String_button = ttk.Button(Button_frame)
        String_button.configure(text="String Operations", command=String)
        String_button.grid(row=1, column=1, sticky=(E, W, N, S))

        Exit_button = ttk.Button(Button_frame)
        Exit_button.configure(text="Exit", command=Exit)
        Exit_button.grid(row=2, column=2, sticky=(E, W, N, S))
        
        String_frame.destroy()
        String_2_frame.destroy()
        String_button_frame.destroy()
        String_output_frame.destroy()

    def Concatenation():
        def Concatenation_2():
            try:
                string = entry_String_strv.get()
                enter_by_user_label_strv.set(string)
                n = str(Concatenation_entry_strv.get())
                string_repitation = string + n
                output_label_strv.set(string_repitation)
                output_label_1_strv.set(type(string))
                
                Concatenation_button.destroy()
                Concatenation_entry.destroy()
                Concatenation_label.destroy()
            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        Concatenation_label = ttk.Label(String_frame)
        Concatenation_label.configure(text="Concatenation String = ", foreground="Blue")
        Concatenation_label.grid(row=3, column=1, sticky=(E, W, N, S))

        Concatenation_entry_strv = StringVar()
        Concatenation_entry = ttk.Entry(String_frame)
        Concatenation_entry.configure(textvariable=Concatenation_entry_strv)
        Concatenation_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        Concatenation_button = ttk.Button(String_frame)
        Concatenation_button.configure(text="Concatenation", command=Concatenation_2)
        Concatenation_button.grid(row=4, column=1, sticky=(E, W, N, S))

    def Repetition():
        def Repetition_2():
            try:
                string = entry_String_strv.get()
                enter_by_user_label_strv.set(string)
                n = int(Repetition_entry_strv.get())
                string_repitation = string * n
                output_label_strv.set(string_repitation)
                output_label_1_strv.set(type(string))
                
                Repetition_button.destroy()
                Repetition_entry.destroy()
                Repetition_label.destroy()
            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        Repetition_label = ttk.Label(String_frame)
        Repetition_label.configure(text="Repetition = ", foreground="Blue")
        Repetition_label.grid(row=3, column=1, sticky=(E, W, N, S))

        Repetition_entry_strv = StringVar()
        Repetition_entry = ttk.Entry(String_frame)
        Repetition_entry.configure(textvariable=Repetition_entry_strv)
        Repetition_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        Repetition_button = ttk.Button(String_frame)
        Repetition_button.configure(text="Repetition", command=Repetition_2)
        Repetition_button.grid(row=4, column=1, sticky=(E, W, N, S))
        

    def Reverse():
        try:
            string = entry_String_strv.get()
            enter_by_user_label_strv.set(string)
            string_r = string[::-1]
            output_label_strv.set(string_r)
            output_label_1_strv.set(type(string))
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def Copy():
        try:
            string = entry_String_strv.get()
            enter_by_user_label_strv.set(string)
            output_label_strv.set(string)
            output_label_1_strv.set(type(string))
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def Index():
        def Index_2():
            try:
                string = entry_String_strv.get()
                enter_by_user_label_strv.set(string)
                n = int(Index_entry_strv.get())
                string_repitation = string[n]
                output_label_strv.set(string_repitation)
                output_label_1_strv.set(type(string))
                
                index_button.destroy()
                Index_entry.destroy()
                Index_label.destroy()
            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        Index_label = ttk.Label(String_frame)
        Index_label.configure(text="Index = ", foreground="Blue")
        Index_label.grid(row=3, column=1, sticky=(E, W, N, S))

        Index_entry_strv = StringVar()
        Index_entry = ttk.Entry(String_frame)
        Index_entry.configure(textvariable=Index_entry_strv)
        Index_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        index_button = ttk.Button(String_frame)
        index_button.configure(text="Index", command=Index_2)
        index_button.grid(row=4, column=1, sticky=(E, W, N, S))

    def Length():
        try:
            string = entry_String_strv.get()
            enter_by_user_label_strv.set(string)
            output_label_strv.set(len(string))
            output_label_1_strv.set(type(string))
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")
        
    def Uppercase():
        try:
            string = entry_String_strv.get()
            enter_by_user_label_strv.set(string)
            string_upper = string.upper()
            output_label_strv.set(string_upper)
            output_label_1_strv.set(type(string))
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def Lowercase():
        try:
            string = entry_String_strv.get()
            enter_by_user_label_strv.set(string)
            string_lower = string.lower()
            output_label_strv.set(string_lower)
            output_label_1_strv.set(type(string))
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def Capitalize():
        try:
            string = entry_String_strv.get()
            enter_by_user_label_strv.set(string)
            string_capi = string.capitalize()
            output_label_strv.set(string_capi)
            output_label_1_strv.set(type(string))
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def Replace():
        def Replace_2():
            try:
                string = entry_String_strv.get()
                enter_by_user_label_strv.set(string)
                old = str(Replace_2_entry_strv.get())
                new = str(Replace_2_entry_2_strv.get())
                string_repitation = string.replace(old, new)
                output_label_strv.set(string_repitation)
                output_label_1_strv.set(type(string))
            
                Replace_2_button.destroy()
                Replace_2_entry.destroy()
                Replace_2_label.destroy()
                Replace_2_entry_2.destroy()
                Replace_2_entry_2.destroy()
                Replace_2_label_2.destroy()

            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        Replace_2_label = ttk.Label(String_frame)
        Replace_2_label.configure(text="Old = ", foreground="Blue")
        Replace_2_label.grid(row=3, column=1, sticky=(E, W, N, S))

        Replace_2_label_2 = ttk.Label(String_frame)
        Replace_2_label_2.configure(text="New = ", foreground="Blue")
        Replace_2_label_2.grid(row=4, column=1, sticky=(E, W, N, S))

        Replace_2_entry_strv = StringVar()
        Replace_2_entry = ttk.Entry(String_frame)
        Replace_2_entry.configure(textvariable=Replace_2_entry_strv)
        Replace_2_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        Replace_2_entry_2_strv = StringVar()
        Replace_2_entry_2 = ttk.Entry(String_frame)
        Replace_2_entry_2.configure(textvariable=Replace_2_entry_2_strv)
        Replace_2_entry_2.grid(row=4, column=2, sticky=(E, W, N, S))

        Replace_2_button = ttk.Button(String_frame)
        Replace_2_button.configure(text="Replace", command=Replace_2)
        Replace_2_button.grid(row=5, column=1, sticky=(E, W, N, S))

    def Remove():
        def Remove_2():
            try:
                string = entry_String_strv.get()
                enter_by_user_label_strv.set(string)
                old = str(Remove_2_entry_strv.get())
                string_repitation = string.replace(old, " ")
                output_label_strv.set(string_repitation)
                output_label_1_strv.set(type(string))
                
                Remove_2_button.destroy()
                Remove_2_entry.destroy()
                Remove_2_label.destroy()
            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        Remove_2_label = ttk.Label(String_frame)
        Remove_2_label.configure(text="Remove = ", foreground="Blue")
        Remove_2_label.grid(row=3, column=1, sticky=(E, W, N, S))

        Remove_2_entry_strv = StringVar()
        Remove_2_entry = ttk.Entry(String_frame)
        Remove_2_entry.configure(textvariable=Remove_2_entry_strv)
        Remove_2_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        Remove_2_button = ttk.Button(String_frame)
        Remove_2_button.configure(text="Remove", command=Remove_2)
        Remove_2_button.grid(row=5, column=1, sticky=(E, W, N, S))

    def Strip():
        try:
            string = entry_String_strv.get()
            enter_by_user_label_strv.set(string)
            string_strip = string.strip()
            output_label_strv.set(string_strip)
            output_label_1_strv.set(type(string))
        except ValueError:
            messagebox.showerror("Error Massagebox", "Enter Valid Details")

    def Find():
        def Find_2():
            try:
                string = entry_String_strv.get()
                enter_by_user_label_strv.set(string)
                n = str(Find_entry_strv.get())
                string_repitation = string.find(n)
                output_label_strv.set(string_repitation)
                output_label_1_strv.set(type(string))
                
                find_button.destroy()
                Find_entry.destroy()
                find_label.destroy()
            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        find_label = ttk.Label(String_frame)
        find_label.configure(text="Find = ", foreground="Blue")
        find_label.grid(row=3, column=1, sticky=(E, W, N, S))

        Find_entry_strv = StringVar()
        Find_entry = ttk.Entry(String_frame)
        Find_entry.configure(textvariable=Find_entry_strv)
        Find_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        find_button = ttk.Button(String_frame)
        find_button.configure(text="Find", command=Find_2)
        find_button.grid(row=4, column=1, sticky=(E, W, N, S))


    def Count():
        def Count_2():
            try:
                string = entry_String_strv.get()
                enter_by_user_label_strv.set(string)
                n = str(Count_entry_strv.get())
                string_repitation = string.count(n)
                output_label_strv.set(string_repitation)
                output_label_1_strv.set(type(string))
                
                Count_button.destroy()
                Count_entry.destroy()
                Count_label.destroy()
            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        Count_label = ttk.Label(String_frame)
        Count_label.configure(text="Count = ", foreground="Blue")
        Count_label.grid(row=3, column=1, sticky=(E, W, N, S))

        Count_entry_strv = StringVar()
        Count_entry = ttk.Entry(String_frame)
        Count_entry.configure(textvariable=Count_entry_strv)
        Count_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        Count_button = ttk.Button(String_frame)
        Count_button.configure(text="Count", command=Count_2)
        Count_button.grid(row=4, column=1, sticky=(E, W, N, S))

    def Start_With():
        def Start_With_2():
            try:
                string = entry_String_strv.get()
                enter_by_user_label_strv.set(string)
                n = str(start_With_entry_strv.get())
                start_With = string.startswith(n)
                if (start_With == 1):
                    output_label_strv.set("True")
                else:
                    output_label_strv.set("False")
                output_label_1_strv.set(type(string))
                
                start_With_button.destroy()
                start_With_entry.destroy()
                start_With_label.destroy()
            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        start_With_label = ttk.Label(String_frame)
        start_With_label.configure(text="Start_With = ", foreground="Blue")
        start_With_label.grid(row=3, column=1, sticky=(E, W, N, S))

        start_With_entry_strv = StringVar()
        start_With_entry = ttk.Entry(String_frame)
        start_With_entry.configure(textvariable=start_With_entry_strv)
        start_With_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        start_With_button = ttk.Button(String_frame)
        start_With_button.configure(text="Start_With", command=Start_With_2)
        start_With_button.grid(row=4, column=1, sticky=(E, W, N, S))

    def End_With():
        def end_With_2():
            try:
                string = entry_String_strv.get()
                enter_by_user_label_strv.set(string)
                n = str(end_With_entry_strv.get())
                start_With = string.endswith(n)
                if (start_With == 1):
                    output_label_strv.set("True")
                else:
                    output_label_strv.set("False")
                output_label_1_strv.set(type(string))
        
                end_With_entry.destroy()
                end_With_button.destroy()
                end_With_label.destroy()

            except ValueError:
                messagebox.showerror("Error Massagebox", "Enter Valid Details")

        end_With_label = ttk.Label(String_frame)
        end_With_label.configure(text="End_With = ", foreground="Blue")
        end_With_label.grid(row=3, column=1, sticky=(E, W, N, S))

        end_With_entry_strv = StringVar()
        end_With_entry = ttk.Entry(String_frame)
        end_With_entry.configure(textvariable=end_With_entry_strv)
        end_With_entry.grid(row=3, column=2, sticky=(E, W, N, S))

        end_With_button = ttk.Button(String_frame)
        end_With_button.configure(text="End_With", command=end_With_2)
        end_With_button.grid(row=4, column=1, sticky=(E, W, N, S))

    def clear():
        output_label_1_strv.set("")
        output_label_strv.set("")
        enter_by_user_label_strv.set("")
        entry_String_strv.set("")

    String_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    String_frame.grid(row=1, column=1, sticky=(E, W, N, S))

    String_2_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    String_2_frame.grid(row=2, column=1, sticky=(E, W, N, S))

    String_output_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    String_output_frame.grid(row=3, column=1, sticky=(E, W, N, S))

    String_button_frame = ttk.Frame(root_window, padding="3 3 12 12", borderwidth=10, relief='raised')
    String_button_frame.grid(row=4, column=1, sticky=(E, W, N, S))

    entry_label = ttk.Label(String_frame)
    entry_label.configure(text="Enter A String = ", foreground="red")
    entry_label.grid(row=1, column=1, sticky=(E, W, N, S))

    entry_1_label = ttk.Label(String_frame)
    entry_1_label.configure(text=" ")
    entry_1_label.grid(row=2, column=1, sticky=(E, W, N, S))

    out_label = ttk.Label(String_output_frame)
    out_label.configure(text="Output : ", font=(10), foreground="red")
    out_label.grid(row=1, column=1, sticky=(E, W, N, S))

    by_you_label = ttk.Label(String_2_frame)
    by_you_label.configure(text="Enter By You String :", font=(10), foreground="red")
    by_you_label.grid(row=1, column=1, sticky=(E, W, N, S))

    entry_String_strv = StringVar()
    entry_String = ttk.Entry(String_frame, width=50)
    entry_String.configure(textvariable=entry_String_strv)
    entry_String.grid(row=1, column=2, sticky=(E, W, N, S), )

    enter_by_user_label_strv = StringVar()
    enter_by_user_label = ttk.Label(String_2_frame)
    enter_by_user_label.configure(textvariable=enter_by_user_label_strv)
    enter_by_user_label.grid(row=2, column=1, sticky=(E, W, N, S))

    output_label_strv = StringVar()
    output_label = ttk.Label(String_output_frame)
    output_label.configure(textvariable=output_label_strv, font=(15))
    output_label.grid(row=2, column=1, sticky=(E, W, N, S))

    output_label_1_strv = StringVar()
    output_1_label = ttk.Label(String_output_frame)
    output_1_label.configure(textvariable=output_label_1_strv, font=(13))
    output_1_label.grid(row=3, column=1, sticky=(E, W, N, S))

    Concatenation_button = ttk.Button(String_button_frame)
    Concatenation_button.configure(text="Concatenation", command=Concatenation)
    Concatenation_button.grid(row=1, column=1, sticky=(E, W, N, S))

    Repetition_button = ttk.Button(String_button_frame)
    Repetition_button.configure(text="Repetition_button", command=Repetition)
    Repetition_button.grid(row=1, column=2, sticky=(E, W, N, S))

    Reverse_button = ttk.Button(String_button_frame)
    Reverse_button.configure(text="Reverse", command=Reverse)
    Reverse_button.grid(row=1, column=3, sticky=(E, W, N, S))

    Copy_button = ttk.Button(String_button_frame)
    Copy_button.configure(text="Copy", command=Copy)
    Copy_button.grid(row=2, column=1, sticky=(E, W, N, S))

    Index_button = ttk.Button(String_button_frame)
    Index_button.configure(text="Index", command=Index)
    Index_button.grid(row=2, column=2, sticky=(E, W, N, S))

    Length_Button = ttk.Button(String_button_frame)
    Length_Button.configure(text="Length", command=Length)
    Length_Button.grid(row=2, column=3, sticky=(E, W, N, S))

    Uppercase_button = ttk.Button(String_button_frame)
    Uppercase_button.configure(text="Uppercase", command=Uppercase)
    Uppercase_button.grid(row=3, column=1, sticky=(E, W, N, S))

    Lowercase_button = ttk.Button(String_button_frame)
    Lowercase_button.configure(text="Lowercase", command=Lowercase)
    Lowercase_button.grid(row=3, column=2, sticky=(E, W, N, S))

    Capitalize_buttonome_button = ttk.Button(String_button_frame)
    Capitalize_buttonome_button.configure(text="Capitalize", command=Capitalize)
    Capitalize_buttonome_button.grid(row=3, column=3, sticky=(E, W, N, S))

    Replace_button = ttk.Button(String_button_frame)
    Replace_button.configure(text="Replace", command=Replace)
    Replace_button.grid(row=4, column=1, sticky=(E, W, N, S))

    Strip_button = ttk.Button(String_button_frame)
    Strip_button.configure(text="Strip", command=Strip)
    Strip_button.grid(row=6, column=1, sticky=(E, W, N, S))

    Find_button = ttk.Button(String_button_frame)
    Find_button.configure(text="Find", command=Find)
    Find_button.grid(row=4, column=3, sticky=(E, W, N, S))

    Start_With_button = ttk.Button(String_button_frame)
    Start_With_button.configure(text="Start_With ", command=Start_With)
    Start_With_button.grid(row=5, column=1, sticky=(E, W, N, S))

    End_With_button = ttk.Button(String_button_frame)
    End_With_button.configure(text="End_With", command=End_With)
    End_With_button.grid(row=5, column=2, sticky=(E, W, N, S))

    Count_button = ttk.Button(String_button_frame)
    Count_button.configure(text="Count", command=Count)
    Count_button.grid(row=5, column=3, sticky=(E, W, N, S))

    Remove_button = ttk.Button(String_button_frame)
    Remove_button.configure(text="Remove", command=Remove)
    Remove_button.grid(row=4, column=2, sticky=(E, W, N, S))

    clear_button = ttk.Button(String_button_frame)
    clear_button.configure(text="Clear All", command=clear)
    clear_button.grid(row=6, column=2, sticky=(E, W, N, S))

    exit_button = ttk.Button(String_button_frame)
    exit_button.configure(text="Exit", command=exit)
    exit_button.grid(row=6, column=3, sticky=(E, W, N, S))

    Home_button = ttk.Button(String_button_frame)
    Home_button.configure(text="Home", command=Home)
    Home_button.grid(row=7, column=1, sticky=(E, W, N, S))

def Exit():
    sys.exit()

disciption_label = ttk.Label(main_frame)
disciption_label.configure(text="Multi-Operations Application \nFor More Info Click Info Button",
                                    font=("Arial", 20), foreground="Black", background="Yellow")
disciption_label.grid(row=1, column=1)

label = ttk.Label(main_frame)
label.configure(text="")
label.grid(row=2, column=1, sticky=(E, W, N, S))

Info_button = ttk.Button(main_frame)
Info_button.configure(text="Info", command=Info_handler)
Info_button.grid(row=3, column=1)

list_button = ttk.Button(Button_frame)
list_button.configure(text="List Operations", command=List)
list_button.grid(row=2, column=1, sticky=(E, W, N, S))

Tuple_button = ttk.Button(Button_frame)
Tuple_button.configure(text="Tuple Operations", command=Tuple)
Tuple_button.grid(row=1, column=2, sticky=(E, W, N, S))


String_button = ttk.Button(Button_frame)
String_button.configure(text="String Operations", command=String)
String_button.grid(row=1, column=1, sticky=(E, W, N, S))

Exit_button = ttk.Button(Button_frame)
Exit_button.configure(text="Exit", command=Exit)
Exit_button.grid(row=2, column=2, sticky=(E, W, N, S))

for frames in root_window.winfo_children(): 
    frames.grid_configure(padx=3, pady=3)
    for widget in frames.winfo_children(): 
        widget.grid_configure(padx=5, pady=5)

root_window.mainloop()
