import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
from tkinter import messagebox


def Add():
    # Create a tkinter window
    window = tk.Tk()
    window.title("Signal Addition")

    # Create labels
    label1 = tk.Label(window, text="Signal 1 File:")
    label1.pack()

    label2 = tk.Label(window, text="Signal 2 File:")
    label2.pack()

    # Entry widgets to display selected file paths
    entry1 = tk.Entry(window)
    entry1.pack()

    entry2 = tk.Entry(window)
    entry2.pack()
    # Function to add and plot signals
    def add_and_plot():
        file_path1 = entry1.get()
        file_path2 = entry2.get()

        # Read the second column of the first signal and the second signal
        signal1 = np.loadtxt(file_path1, skiprows=3, usecols=(1,))
        signal2 = np.loadtxt(file_path2, skiprows=3, usecols=(1,))

        # Add the signals
        result_signal = signal1 + signal2

        # Plot the first signal
        ax1.clear()
        ax1.plot(signal1, label='Signal 1')
        ax1.legend()

        # Plot the second signal
        ax2.clear()
        ax2.plot(signal2, label='Signal 2')
        ax2.legend()

        # Plot the result signal
        ax3.clear()
        ax3.plot(result_signal, label='Result Signal')
        ax3.legend()

        # Redraw the canvases
        canvas1.draw()
        canvas2.draw()
        canvas3.draw()

    # Button to perform addition and plotting
    add_button = tk.Button(window, text="Add and Plot", command=add_and_plot)
    add_button.pack()

    # Function to open file dialog and update entry widgets
    def open_file(entry):
        file_path = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

    # Buttons to open file dialogs
    browse_button1 = tk.Button(window, text="Browse", command=lambda: open_file(entry1))
    browse_button1.pack()

    browse_button2 = tk.Button(window, text="Browse", command=lambda: open_file(entry2))
    browse_button2.pack()

    # Initialize figures and axes for plotting
    fig1, ax1 = plt.subplots()
    canvas1 = FigureCanvasTkAgg(fig1, master=window)
    canvas_widget1 = canvas1.get_tk_widget()
    canvas_widget1.pack()

    fig2, ax2 = plt.subplots()
    canvas2 = FigureCanvasTkAgg(fig2, master=window)
    canvas_widget2 = canvas2.get_tk_widget()
    canvas_widget2.pack()

    fig3, ax3 = plt.subplots()
    canvas3 = FigureCanvasTkAgg(fig3, master=window)
    canvas_widget3 = canvas3.get_tk_widget()
    canvas_widget3.pack()

    # Modify the canvas_widget pack options for smaller canvases
    canvas_widget1 = canvas1.get_tk_widget()
    canvas_widget1.pack(side="left", fill="both", expand=True)

    canvas_widget2 = canvas2.get_tk_widget()
    canvas_widget2.pack(side="left", fill="both", expand=True)

    canvas_widget3 = canvas3.get_tk_widget()
    canvas_widget3.pack(side="right", fill="both", expand=True)

    # Run the tkinter main loop
    window.mainloop()
def Sub():
    # Create a tkinter window
    window = tk.Tk()
    window.title("Signal Subtraction")

    # Create labels
    label1 = tk.Label(window, text="Signal 1 File:")
    label1.pack()

    label2 = tk.Label(window, text="Signal 2 File:")
    label2.pack()

    # Entry widgets to display selected file paths
    entry1 = tk.Entry(window)
    entry1.pack()

    entry2 = tk.Entry(window)
    entry2.pack()

    # Function to subtract and plot signals
    def subtract_and_plot():
        file_path1 = entry1.get()
        file_path2 = entry2.get()

        # Read the second column of the first signal and the second signal
        signal1 = np.loadtxt(file_path1, skiprows=3, usecols=(1,))
        signal2 = np.loadtxt(file_path2, skiprows=3, usecols=(1,))

        # Subtract the signals
        result_signal = signal1 - signal2

        # Plot the first signal
        ax1.clear()
        ax1.plot(signal1, label='Signal 1')
        ax1.legend()

        # Plot the second signal
        ax2.clear()
        ax2.plot(signal2, label='Signal 2')
        ax2.legend()

        # Plot the result signal
        ax3.clear()
        ax3.plot(result_signal, label='Result Signal')
        ax3.legend()

        # Redraw the canvases
        canvas1.draw()
        canvas2.draw()
        canvas3.draw()

    # Button to perform subtraction and plotting
    subtract_button = tk.Button(window, text="Subtract and Plot", command=subtract_and_plot)
    subtract_button.pack()

    # Function to open file dialog and update entry widgets
    def open_file(entry):
        file_path = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

    # Buttons to open file dialogs
    browse_button1 = tk.Button(window, text="Browse", command=lambda: open_file(entry1))
    browse_button1.pack()

    browse_button2 = tk.Button(window, text="Browse", command=lambda: open_file(entry2))
    browse_button2.pack()

    # Initialize figures and axes for plotting
    fig1, ax1 = plt.subplots()
    canvas1 = FigureCanvasTkAgg(fig1, master=window)
    canvas_widget1 = canvas1.get_tk_widget()
    canvas_widget1.pack()

    fig2, ax2 = plt.subplots()
    canvas2 = FigureCanvasTkAgg(fig2, master=window)
    canvas_widget2 = canvas2.get_tk_widget()
    canvas_widget2.pack()

    fig3, ax3 = plt.subplots()
    canvas3 = FigureCanvasTkAgg(fig3, master=window)
    canvas_widget3 = canvas3.get_tk_widget()
    canvas_widget3.pack()

    # Modify the canvas_widget pack options for smaller canvases
    canvas_widget1 = canvas1.get_tk_widget()
    canvas_widget1.pack(side="left", fill="both", expand=True)

    canvas_widget2 = canvas2.get_tk_widget()
    canvas_widget2.pack(side="left", fill="both", expand=True)

    canvas_widget3 = canvas3.get_tk_widget()
    canvas_widget3.pack(side="right", fill="both", expand=True)

    # Run the tkinter main loop
    window.mainloop()

def Multiply():
    # Create a tkinter window
    window = tk.Tk()
    window.title("Signal Multiplication")

    # Create labels
    label1 = tk.Label(window, text="Signal File:")
    label1.pack()

    label2 = tk.Label(window, text="Constant:")
    label2.pack()

    # Entry widgets to display the selected file path and constant
    entry1 = tk.Entry(window)
    entry1.pack()

    entry2 = tk.Entry(window)
    entry2.pack()

    # Function to multiply and plot the signal
    def multiply_and_plot():
        file_path = entry1.get()
        constant = float(entry2.get())

        # Read the second column of the signal
        signal = np.loadtxt(file_path, skiprows=3, usecols=(1,))

        # Multiply the signal by the constant
        result_signal = signal * constant

        # Plot the original signal
        ax1.clear()
        ax1.plot(signal, label='Original Signal')
        ax1.legend()

        # Plot the result signal
        ax2.clear()
        ax2.plot(result_signal, label='Result Signal')
        ax2.legend()

        # Redraw the canvases
        canvas1.draw()
        canvas2.draw()

    # Button to perform multiplication and plotting
    multiply_button = tk.Button(window, text="Multiply and Plot", command=multiply_and_plot)
    multiply_button.pack()

    # Function to open a file dialog and update the entry widget
    def open_file(entry):
        file_path = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

    # Button to open a file dialog for selecting the signal file
    browse_button = tk.Button(window, text="Browse", command=lambda: open_file(entry1))
    browse_button.pack()

    # Initialize figures and axes for plotting
    fig1, ax1 = plt.subplots()
    canvas1 = FigureCanvasTkAgg(fig1, master=window)
    canvas_widget1 = canvas1.get_tk_widget()
    canvas_widget1.pack()

    fig2, ax2 = plt.subplots()
    canvas2 = FigureCanvasTkAgg(fig2, master=window)
    canvas_widget2 = canvas2.get_tk_widget()
    canvas_widget2.pack()

    canvas_widget1 = canvas1.get_tk_widget()
    canvas_widget1.pack(side="left", fill="both", expand=True)

    canvas_widget2 = canvas2.get_tk_widget()
    canvas_widget2.pack(side="left", fill="both", expand=True)

    # Run the tkinter main loop
    window.mainloop()
def Squre():
    # Create a tkinter window
    window = tk.Tk()
    window.title("Signal Power")

    # Create labels
    label1 = tk.Label(window, text="Signal File:")
    label1.pack()

    # Entry widgets to display the selected file path and constant
    entry1 = tk.Entry(window)
    entry1.pack()

    # Function to multiply and plot the signal
    def power_and_plot():
        file_path = entry1.get()

        # Read the second column of the signal
        signal = np.loadtxt(file_path, skiprows=3, usecols=(1,))

        # Multiply the signal by the constant
        result_signal = pow(signal,2)

        # Plot the original signal
        ax1.clear()
        ax1.plot(signal, label='Original Signal')
        ax1.legend()

        # Plot the result signal
        ax2.clear()
        ax2.plot(result_signal, label='Result Signal')
        ax2.legend()

        # Redraw the canvases
        canvas1.draw()
        canvas2.draw()

    # Button to perform multiplication and plotting
    power_button = tk.Button(window, text="Power and Plot", command=power_and_plot)
    power_button.pack()

    # Function to open a file dialog and update the entry widget
    def open_file(entry):
        file_path = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

    # Button to open a file dialog for selecting the signal file
    browse_button = tk.Button(window, text="Browse", command=lambda: open_file(entry1))
    browse_button.pack()

    # Initialize figures and axes for plotting
    fig1, ax1 = plt.subplots()
    canvas1 = FigureCanvasTkAgg(fig1, master=window)
    canvas_widget1 = canvas1.get_tk_widget()
    canvas_widget1.pack()

    fig2, ax2 = plt.subplots()
    canvas2 = FigureCanvasTkAgg(fig2, master=window)
    canvas_widget2 = canvas2.get_tk_widget()
    canvas_widget2.pack()

    canvas_widget1 = canvas1.get_tk_widget()
    canvas_widget1.pack(side="left", fill="both", expand=True)

    canvas_widget2 = canvas2.get_tk_widget()
    canvas_widget2.pack(side="left", fill="both", expand=True)
    # Run the tkinter main loop
    window.mainloop()


def Shift():
    # Create a tkinter window
    window = tk.Tk()
    window.title("Signal Shifting")

    # Create labels
    label1 = tk.Label(window, text="Signal File:")
    label1.pack()

    label2 = tk.Label(window, text="Constant:")
    label2.pack()

    # Entry widgets to display the selected file path and constant
    entry1 = tk.Entry(window)
    entry1.pack()

    entry2 = tk.Entry(window)
    entry2.pack()

    # Function to multiply and plot the signal
    def Shift_and_plot():
        file_path = entry1.get()
        constant = float(entry2.get())

        # Read the second column of the signal
        signal = np.loadtxt(file_path, skiprows=3, usecols=0)

        # Multiply the signal by the constant
        result_signal = signal + constant

        # Plot the original signal
        ax1.clear()
        ax1.plot(signal, label='Original Signal')
        ax1.legend()

        # Plot the result signal
        ax2.clear()
        ax2.plot(result_signal, label='Result Signal')
        ax2.legend()

        # Redraw the canvases
        canvas1.draw()
        canvas2.draw()

    # Button to perform multiplication and plotting
    shift_button = tk.Button(window, text="Shift and Plot", command=Shift_and_plot)
    shift_button.pack()

    # Function to open a file dialog and update the entry widget
    def open_file(entry):
        file_path = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

    # Button to open a file dialog for selecting the signal file
    browse_button = tk.Button(window, text="Browse", command=lambda: open_file(entry1))
    browse_button.pack()

    # Initialize figures and axes for plotting
    fig1, ax1 = plt.subplots()
    canvas1 = FigureCanvasTkAgg(fig1, master=window)
    canvas_widget1 = canvas1.get_tk_widget()
    canvas_widget1.pack()

    fig2, ax2 = plt.subplots()
    canvas2 = FigureCanvasTkAgg(fig2, master=window)
    canvas_widget2 = canvas2.get_tk_widget()
    canvas_widget2.pack()

    canvas_widget1 = canvas1.get_tk_widget()
    canvas_widget1.pack(side="left", fill="both", expand=True)

    canvas_widget2 = canvas2.get_tk_widget()
    canvas_widget2.pack(side="left", fill="both", expand=True)
    # Run the tkinter main loop
    window.mainloop()
def Task3_fun():
    task3_window = tk.Toplevel()
    task3_window.geometry("600x400")
    task3_window.title("Task 3")

    def exit_application():
        exit()

    def show_error_message():
        message = "Please Choose One Operation"
        messagebox.showinfo("Error", message)

    def perform_task():
        selected_operation = selected_operation_var.get()
        if selected_operation == 1:
            Add()
        elif selected_operation == 2:
            Sub()
        elif selected_operation == 3:
            Multiply()
        elif selected_operation == 4:
            Squre()
        elif selected_operation == 5:
            Shift()
        else:
            show_error_message()

    # Radio buttons for selecting add, sub, or multiply
    selected_operation_var = tk.IntVar(value=0)

    add_radio = tk.Radiobutton(task3_window, text="Add", variable=selected_operation_var, font=("Arial", 12), value=1)
    sub_radio = tk.Radiobutton(task3_window, text="Sub", variable=selected_operation_var, font=("Arial", 12), value=2)
    multiply_radio = tk.Radiobutton(task3_window, text="Multiply", variable=selected_operation_var, font=("Arial", 12), value=3)
    squre_radio = tk.Radiobutton(task3_window, text="Squre", variable=selected_operation_var, font=("Arial", 12), value=4)
    shift_radio = tk.Radiobutton(task3_window, text="Shift", variable=selected_operation_var, font=("Arial", 12), value=5)

    add_radio.pack(side="top", fill="both", expand=True)
    sub_radio.pack(side="top", fill="both", expand=True)
    multiply_radio.pack(side="top", fill="both", expand=True)
    squre_radio.pack(side="top", fill="both", expand=True)
    shift_radio.pack(side="top", fill="both", expand=True)

    # Button to exit the application
    exit_button = tk.Button(task3_window, text="Exit", padx=15, pady=5, fg="black", bg="red", font=("Arial", 12), command=exit_application)
    exit_button.pack(side="bottom", expand=True)

    open_task_button = tk.Button(task3_window, text="GO", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12), command=perform_task)
    open_task_button.pack(side="bottom", expand=True)

    task3_window.mainloop()
