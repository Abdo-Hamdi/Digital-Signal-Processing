import tkinter as tk
from tkinter import messagebox
import Task1
import Task2
import Task3
import Task4
# Create the main window
window = tk.Tk()
window.geometry("400x400")
window.title("The Main")
window.iconbitmap('D:\Project\Digital-Signal-Processing\signal_ icon.ico')


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
    elif selected == 3:
        Task3.Task3_fun()
    elif selected == 4:
        Task4.Task4_fun()
    else:
        show_message_box()


# Radio buttons for selecting Task 1 or Task 2 or else
selected_function = tk.IntVar(value=0)

task1_radio = tk.Radiobutton(window, text="Task 1", variable=selected_function, font=("Arial", 12), value=1)
task2_radio = tk.Radiobutton(window, text="Task 2", variable=selected_function, font=("Arial", 12), value=2)
task3_radio = tk.Radiobutton(window, text="Task 3", variable=selected_function, font=("Arial", 12), value=3)
task4_radio = tk.Radiobutton(window, text="Task 4", variable=selected_function, font=("Arial", 12), value=4)

task1_radio.pack(side="top", fill="both", expand=True)
task2_radio.pack(side="top", fill="both", expand=True)
task3_radio.pack(side="top", fill="both", expand=True)
task4_radio.pack(side="top", fill="both", expand=True)
# Button to open the task
exit_button = tk.Button(window, text="Exit", padx=15, pady=5, fg="black", bg="red", font=("Arial", 12), command=ex)
exit_button.pack(side="bottom", expand=True)

open_task_button = tk.Button(window, text="GO", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                             command=button_task)
open_task_button.pack(side="bottom", expand=True)

window.mainloop()
