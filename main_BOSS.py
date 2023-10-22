import tkinter as tk
from tkinter import messagebox
import Task1 ,Task2

# Create the main window
window = tk.Tk()
window.geometry("300x200")
window.title("The Main")
window.iconbitmap('D:\Digital-Signal-Processing\signal_ icon.ico')


def ex():
    exit()

def show_message_box():
    message = "Please Choose One Task"
    messagebox.showinfo("Error", message)

# Function of the "GO" button
def button_task():
    selected = selected_function.get()
    if selected == 1:
        Task1.Task1_fun()
    elif selected == 2:
        Task2.Task2_fun()
    else:
        show_message_box()


# Radio buttons for selecting Task 1 or Task 2
selected_function = tk.IntVar(value=0)

task1_radio = tk.Radiobutton(window, text="Task 1", variable=selected_function, font=("Arial", 12), value=1)
task2_radio = tk.Radiobutton(window, text="Task 2", variable=selected_function, font=("Arial", 12), value=2)

task1_radio.place(x=60, y=40)
task2_radio.place(x=185, y=40)

# Button to open the task
open_task_button = tk.Button(window, text="GO", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12), command=button_task)
open_task_button.place(x = 80, y = 100)

exit_button = tk.Button(window, text="Exit", padx=15, pady=5, fg="black", bg="red", font=("Arial", 12), command=ex)
exit_button.place(x = 180, y = 100)

window.mainloop()
