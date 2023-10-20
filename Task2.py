import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
def  Task2_fun() :
    def generate_signal():
        signal_type = selected_signal.get()
        A = float(amplitude_entry.get())
        theta = float(phase_entry.get())
        analog_freq = float(analog_freq_entry.get())
        sampling_freq = float(sampling_freq_entry.get())
        if analog_freq == 0:
            message = "امسح يسطا"
            messagebox.showinfo("Error", message)
            return
        elif sampling_freq == 0:
            # Show continuous signal only when sampling_freq is 0
            t_continuous = np.arange(0, 0.5, 10 / (100 * analog_freq))

            if signal_type == "cos":
                signal_continuous = A * np.cos(2 * np.pi * analog_freq * t_continuous + theta)
                signal_name = "Cos"
            else:
                signal_continuous = A * np.sin(2 * np.pi * analog_freq * t_continuous + theta)
                signal_name = "Sin"

            plt.figure()
            plt.plot(t_continuous, signal_continuous, label=f"Continuous {signal_name} Signal")
            plt.xlabel("Time")
            plt.ylabel("Amplitude")
            plt.legend()

            canvas = FigureCanvasTkAgg(plt.gcf(), master=app)
            canvas.get_tk_widget().grid(row=6, column=0, columnspan=2)
            canvas.draw()
        elif sampling_freq < 2 * analog_freq:
            message = "Sampling frequency must be greater than or equal to 2 * Analog Frequency."
            messagebox.showinfo("Error", message)
            return
        else:
            # Handle the case when sampling_freq is valid for both continuous and discrete signals
            t_continuous = np.arange(0, 0.5, 10 / (100 * analog_freq))
            t_discrete = np.arange(0, 0.5, 1 / sampling_freq)

            if signal_type == "cos":
                signal_continuous = A * np.cos(2 * np.pi * analog_freq * t_continuous + theta)
                signal_discrete = A * np.cos(2 * np.pi * analog_freq * t_discrete + theta)
                signal_name = "Cos"
            else:
                signal_continuous = A * np.sin(2 * np.pi * analog_freq * t_continuous + theta)
                signal_discrete = A * np.sin(2 * np.pi * analog_freq * t_discrete + theta)
                signal_name = "Sin"

            plt.figure()
            plt.subplot(2, 1, 1)
            plt.plot(t_continuous, signal_continuous, label=f"Continuous {signal_name} Signal")
            plt.xlabel("Time")
            plt.ylabel("Amplitude")
            plt.legend()

            plt.subplot(2, 1, 2)
            plt.stem(t_discrete, signal_discrete, linefmt='-b', markerfmt='ro', basefmt=' ')
            plt.xlabel("Time")
            plt.ylabel("Amplitude")
            plt.title(f"Discrete {signal_name} Signal")

            plt.tight_layout()

            canvas = FigureCanvasTkAgg(plt.gcf(), master=app)
            canvas.get_tk_widget().grid(row=6, column=0, columnspan=2)
            canvas.draw()

    # Create the main application window
    app = tk.Tk()
    app.title("Signal Generator")

    # Add the rest of your GUI elements here...
    # Add a label for signal type selection
    signal_type_label = ttk.Label(app, text="Select Signal Type:")
    signal_type_label.grid(row=0, column=0, columnspan=2)

    # Create radio buttons for selecting sine or cosine
    selected_signal = tk.StringVar(value="cos")  # Default to cosine
    cosine_radio = ttk.Radiobutton(app, text="Cos", variable=selected_signal, value="cos")
    sine_radio = ttk.Radiobutton(app, text="Sin", variable=selected_signal, value="sin")
    cosine_radio.grid(row=1, column=0)
    sine_radio.grid(row=1, column=1)

    # Add input fields for user parameters
    amplitude_label = ttk.Label(app, text="Amplitude (A):")
    amplitude_label.grid(row=2, column=0)
    amplitude_entry = ttk.Entry(app)
    amplitude_entry.grid(row=2, column=1)

    phase_label = ttk.Label(app, text="Phase Shift (theta):")
    phase_label.grid(row=3, column=0)
    phase_entry = ttk.Entry(app)
    phase_entry.grid(row=3, column=1)

    analog_freq_label = ttk.Label(app, text="Analog Frequency:")
    analog_freq_label.grid(row=4, column=0)
    analog_freq_entry = ttk.Entry(app)
    analog_freq_entry.grid(row=4, column=1)

    sampling_freq_label = ttk.Label(app, text="Sampling Frequency (must be > 2 * Analog Frequency):")
    sampling_freq_label.grid(row=5, column=0)
    sampling_freq_entry = ttk.Entry(app)
    sampling_freq_entry.grid(row=5, column=1)

    # Create a button to generate the signal
    generate_button = ttk.Button(app, text="Generate Signal", command=generate_signal)
    generate_button.grid(row=7, column=0, columnspan=2)

    # Start the GUI application
    app.mainloop()