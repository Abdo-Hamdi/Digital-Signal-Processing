import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
from tkinter import messagebox
class SignalAddition:
    def __init__(self):
        # Create a tkinter window
        self.window = tk.Tk()
        self.window.title("Signal Addition")

        # Create labels
        self.label1 = tk.Label(self.window, text="Signal 1 File:")
        self.label1.pack()

        self.label2 = tk.Label(self.window, text="Signal 2 File:")
        self.label2.pack()

        # Entry widgets to display selected file paths
        self.entry1 = tk.Entry(self.window)
        self.entry1.pack()

        self.entry2 = tk.Entry(self.window)
        self.entry2.pack()

        # Initialize figures and axes for plotting
        self.fig1, self.ax1 = plt.subplots()
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.window)
        self.canvas_widget1 = self.canvas1.get_tk_widget()

        self.fig2, self.ax2 = plt.subplots()
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.window)
        self.canvas_widget2 = self.canvas2.get_tk_widget()

        self.fig3, self.ax3 = plt.subplots()
        self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self.window)
        self.canvas_widget3 = self.canvas3.get_tk_widget()

        # Place the canvases side by side
        self.canvas_widget1.pack(side="left", fill="both", expand=True)
        self.canvas_widget2.pack(side="left", fill="both", expand=True)
        self.canvas_widget3.pack(side="right", fill="both", expand=True)

        # Create a button to perform addition and plotting
        self.add_button = tk.Button(self.window, text="Add and Plot", command=self.add_and_plot)
        self.add_button.pack()

        # Create buttons to open file dialogs
        self.browse_button1 = tk.Button(self.window, text="Browse", command=self.open_file(self.entry1))
        self.browse_button1.pack()

        self.browse_button2 = tk.Button(self.window, text="Browse", command=self.open_file(self.entry2))
        self.browse_button2.pack()

    def add_and_plot(self):
        file_path1 = self.entry1.get()
        file_path2 = self.entry2.get()

        # Read the second column of the first signal and the second signal
        signal1 = np.loadtxt(file_path1, skiprows=3, usecols=(1,))
        signal2 = np.loadtxt(file_path2, skiprows=3, usecols=(1,))

        # Add the signals
        result_signal = signal1 + signal2

        # Plot the first signal
        self.ax1.clear()
        self.ax1.plot(signal1, label='Signal 1')
        self.ax1.legend()

        # Plot the second signal
        self.ax2.clear()
        self.ax2.plot(signal2, label='Signal 2')
        self.ax2.legend()

        # Plot the result signal
        self.ax3.clear()
        self.ax3.plot(result_signal, label='Result Signal')
        self.ax3.legend()

        # Redraw the canvases
        self.canvas1.draw()
        self.canvas2.draw()
        self.canvas3.draw()

    def open_file(self, entry):
        file_path = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    signal_addition = SignalAddition()
    signal_addition.run()
