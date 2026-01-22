import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
from datetime import datetime

root = tk.Tk()
root.title("Clock")
root.iconbitmap("My_Icon.ico")
root.geometry("400x300")

# Notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# ---------------- CLOCK ----------------
clock_frame = ttk.Frame(notebook)
notebook.add(clock_frame, text='Clock')

clock_label = ttk.Label(clock_frame, font=('Helvetica', 48))
clock_label.pack(expand=True)

def update_clock():
    now = time.strftime('%H:%M:%S')
    clock_label.config(text=now)
    clock_label.after(1000, update_clock)

update_clock()

# ---------------- STOPWATCH ----------------
stopwatch_frame = ttk.Frame(notebook)
notebook.add(stopwatch_frame, text='Stopwatch')

sw_label = ttk.Label(stopwatch_frame, font=('Helvetica', 36))
sw_label.pack()

sw_running = False
sw_seconds = 0

def update_stopwatch():
    if sw_running:
        global sw_seconds
        sw_seconds += 1
        mins, secs = divmod(sw_seconds, 60)
        sw_label.config(text=f'{mins:02}:{secs:02}')
        sw_label.after(1000, update_stopwatch)

def start_stopwatch():
    global sw_running
    if not sw_running:
        sw_running = True
        update_stopwatch()

def stop_stopwatch():
    global sw_running
    sw_running = False

def reset_stopwatch():
    global sw_seconds
    sw_seconds = 0
    sw_label.config(text='00:00')

ttk.Button(stopwatch_frame, text='Start', command=start_stopwatch).pack(side='left', padx=10)
ttk.Button(stopwatch_frame, text='Stop', command=stop_stopwatch).pack(side='left', padx=10)
ttk.Button(stopwatch_frame, text='Reset', command=reset_stopwatch).pack(side='left', padx=10)

# ---------------- TIMER ----------------
timer_frame = ttk.Frame(notebook)
notebook.add(timer_frame, text='Timer')

timer_label = ttk.Label(timer_frame, font=('Helvetica', 36))
timer_label.pack()

timer_entry = ttk.Entry(timer_frame)
timer_entry.pack()
timer_entry.insert(0, "60")  # default 60 seconds

timer_running = False
timer_seconds = 0

def update_timer():
    global timer_seconds
    if timer_running and timer_seconds > 0:
        timer_seconds -= 1
        mins, secs = divmod(timer_seconds, 60)
        timer_label.config(text=f'{mins:02}:{secs:02}')
        timer_label.after(1000, update_timer)
    elif timer_seconds == 0:
        messagebox.showinfo("Timer", "Time's up!")

def start_timer():
    global timer_running, timer_seconds
    try:
        timer_seconds = int(timer_entry.get())
        timer_running = True
        update_timer()
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

# Timer controls
ttk.Button(timer_frame, text='Start Timer', command=start_timer).pack(pady=10)

# ---------------- ALARM ----------------
alarm_frame = ttk.Frame(notebook)
notebook.add(alarm_frame, text='Alarm')

alarm_entry = ttk.Entry(alarm_frame)
alarm_entry.pack()
alarm_entry.insert(0, "HH:MM")  # placeholder

def check_alarm():
    while True:
        now = datetime.now().strftime('%H:%M')
        alarm_time = alarm_entry.get()
        if now == alarm_time:
            messagebox.showinfo("Alarm", f"It's {alarm_time}!")
            break
        time.sleep(30)

def set_alarm():
    threading.Thread(target=check_alarm, daemon=True).start()
    messagebox.showinfo("Alarm", "Alarm set!")

ttk.Button(alarm_frame, text='Set Alarm', command=set_alarm).pack(pady=10)

root.mainloop()