import comparesignal2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def Task6_fun():

    def handle_file():
        file_path = filedialog.askopenfilename(title="Select a signal file")
        signal = []
        if file_path:
            with open(file_path, 'r') as file:
                signal = np.loadtxt(file, skiprows=3, usecols=(1,))
        return signal


    def CALC_DCT():
        signal = handle_file()
        N = len(signal)
        result = []
        for K in range(N):
            Sum = 0
            for n in range(N):
                ang = (np.pi / (4 * N)) * (2*n - 1) * (2*K - 1)
                Sum += signal[n] * np.cos(ang)
            r = np.sqrt(2 / N) * Sum
            result.append(float(r))
        comparesignal2.SignalSamplesAreEqual("DCT_output.txt", result)

    def CALC_DC ():
        signal = handle_file()
        N = len(signal)
        Sum = 0.0
        Avarge = 0.0
        result = []
        for i in range(N):
            Sum += signal[i]
            Avarge = Sum / N

        for z in range(N):
            result.append(signal[z] - Avarge)

        comparesignal2.SignalSamplesAreEqual("DC_component_output.txt",result)

        # Plotting the signals side by side
        fig, axs = plt.subplots(1, 2, figsize=(12, 4))

        # Plotting the original signal
        axs[0].plot(signal)
        axs[0].set_title('Original Signal')
        axs[0].set_xlabel('Time')
        axs[0].set_ylabel('Amplitude')

        # Plotting the signal after DC component removal
        axs[1].plot(result)
        axs[1].set_title('Signal after DC Component Removal')
        axs[1].set_xlabel('Time')
        axs[1].set_ylabel('Amplitude')

        # Display the plots
        plt.show()

    def exit_application():
        exit()

    window = tk.Tk()
    window.title("Task 6")
    window.geometry("400x250")

    exit_button = tk.Button(window, text="Exit", padx=15, pady=5, fg="black", bg="red", font=("Arial", 12),
                            command=exit_application)
    exit_button.grid(row=1, column=1, padx=10, pady=10)

    open_task_button1 = tk.Button(window, text="DCT", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                 command=CALC_DCT)
    open_task_button1.grid(row=0, column=0, padx=10, pady=10)

    open_task_button2 = tk.Button(window, text="DC Remover", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                 command=CALC_DC)
    open_task_button2.grid(row=0, column=2, padx=10, pady=10)

    window.mainloop()