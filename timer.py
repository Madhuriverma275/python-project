import tkinter as tk
from tkinter import messagebox

def start_timer():
    try:
        total_seconds = int(minutes_entry.get()) * 60 + int(seconds_entry.get())
        countdown(total_seconds)
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter valid numbers!")

def countdown(time_left):
    if time_left >= 0:
        mins, secs = divmod(time_left, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        timer_label.config(text=time_format)
        root.after(1000, countdown, time_left - 1)
    else:
        messagebox.showinfo("Time's up!", "Timer finished!")

def reset_timer():
    timer_label.config(text="00:00")

# GUI
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("350x300")

tk.Label(root, text="Countdown Timer", font=("Arial", 18, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Minutes").grid(row=0, column=0)
tk.Label(frame, text="Seconds").grid(row=0, column=1)

minutes_entry = tk.Entry(frame, width=5)
minutes_entry.grid(row=1, column=0, padx=5)

seconds_entry = tk.Entry(frame, width=5)
seconds_entry.grid(row=1, column=1, padx=5)

timer_label = tk.Label(root, text="00:00", font=("Arial", 30, "bold"))
timer_label.pack(pady=20)

tk.Button(root, text="Start", width=10, command=start_timer).pack(pady=5)
tk.Button(root, text="Reset", width=10, command=reset_timer).pack()

root.mainloop()
