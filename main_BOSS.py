import tkinter as tk
from tkinter import messagebox
import Task1
import Task2
import Task3
import Task4
import Task5
import Task6
import Task7
import Task8
import Task9
# Create the main window
window = tk.Tk()
window.geometry("300x400")
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
    elif selected == 5:
        Task5.Task5_fun()
    elif selected == 6:
        Task6.Task6_fun()
    elif selected == 7:
        Task7.Task7_fun()
    elif selected == 8:
        Task8.Task8_fun()
    elif selected == 9:
        Task9.Task9_fun()
    else:
        show_message_box()


# Radio buttons for selecting Task 1 or Task 2 or else
selected_function = tk.IntVar(value=0)

task1_radio = tk.Radiobutton(window, text="Task 1", variable=selected_function, font=("Arial", 12), value=1)
task2_radio = tk.Radiobutton(window, text="Task 2", variable=selected_function, font=("Arial", 12), value=2)
task3_radio = tk.Radiobutton(window, text="Task 3", variable=selected_function, font=("Arial", 12), value=3)
task4_radio = tk.Radiobutton(window, text="Task 4", variable=selected_function, font=("Arial", 12), value=4)
task5_radio = tk.Radiobutton(window, text="Task 5", variable=selected_function, font=("Arial", 12), value=5)
task6_radio = tk.Radiobutton(window, text="Task 6", variable=selected_function, font=("Arial", 12), value=6)
task7_radio = tk.Radiobutton(window, text="Task 7", variable=selected_function, font=("Arial", 12), value=7)
task8_radio = tk.Radiobutton(window, text="Task 8", variable=selected_function, font=("Arial", 12), value=8)
task9_radio = tk.Radiobutton(window, text="Task 9", variable=selected_function, font=("Arial", 12), value=9)



task1_radio.grid(row=0, column=0, pady=10, padx=10)
task2_radio.grid(row=0, column=2, pady=10, padx=10)
task3_radio.grid(row=1, column=0, pady=10, padx=10)
task4_radio.grid(row=1, column=2, pady=10, padx=10)
task5_radio.grid(row=2, column=0, pady=10, padx=10)
task6_radio.grid(row=2, column=2, pady=10, padx=10)
task7_radio.grid(row=3, column=0, pady=10, padx=10)
task8_radio.grid(row=3, column=2, pady=10, padx=10)
task9_radio.grid(row=4, column=0, pady=10, padx=10)

# Button to open the task
exit_button = tk.Button(window, text="Exit", padx=15, pady=5, fg="black", bg="red", font=("Arial", 12), command=ex)
exit_button.grid(row=6, column=1, pady=10, padx=10)

open_task_button = tk.Button(window, text="GO", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                             command=button_task)
open_task_button.grid(row=5, column=1, pady=10, padx=10)

window.mainloop()
