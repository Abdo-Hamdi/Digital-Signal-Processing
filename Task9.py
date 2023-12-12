import CompareSignal
import ConvTest
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt

def Task9_fun():
    def dft(signal):
        N = len(signal)
        dft_result = np.zeros(N, dtype=np.complex128)

        for k in range(N):
            for n in range(N):
                angle = -2 * np.pi * k * n / N
                dft_result[k] += signal[n] * np.exp(1j * angle)

        return dft_result

    def idft(signal):
        N = len(signal)
        idft_result = np.zeros(N, dtype=np.complex128)

        for n in range(N):
            for k in range(N):
                angle = 2 * np.pi * k * n / N
                idft_result[n] += signal[k] * np.exp(1j * angle)

        return idft_result / N

    def Fast_Correlation():
        selected = selected_function.get()
        file_path1 = filedialog.askopenfilename(title="Select Signal File 1", filetypes=[("Text files", "*.txt")])
        file_path2 = filedialog.askopenfilename(title="Select Signal File 2", filetypes=[("Text files", "*.txt")])

        if file_path1 and file_path2:
            try:
                signal1 = np.loadtxt(file_path1, skiprows=3, usecols=1)
                signal2 = np.loadtxt(file_path2, skiprows=3, usecols=1)

                if len(signal1) != len(signal2):
                    total_length = len(signal1) + len(signal2) - 1
                    signal1 = np.pad(signal1, (0, total_length - len(signal1)), 'constant')
                    signal2 = np.pad(signal2, (0, total_length - len(signal2)), 'constant')
                    ind = np.array(range(total_length))
                else:
                    ind = np.array(range(0, len(signal1)))

                signal1dft = dft(signal1)
                signal2dft = dft(signal2)

                fre_corr = np.conjugate(signal1dft) * signal2dft

                res_signal = idft(fre_corr)

                res_signal = np.round(res_signal.real).astype(int)

                if selected == 1:
                    normalization_factor = np.sqrt(np.sum(signal1 ** 2)) * np.sqrt(np.sum(signal2 ** 2))
                    normalized_corr_result = res_signal / normalization_factor
                    res_signal = normalized_corr_result
                    CompareSignal.Compare_Signals("CorrOutput.txt", ind, normalized_corr_result)
                if selected == 2:
                    CompareSignal.Compare_Signals("Corr_Output.txt", ind, res_signal/len(res_signal))
                fig, axes = plt.subplots(3, 1, figsize=(10, 9))
                axes[0].plot(ind, signal1)
                axes[0].set_title('Signal 1')
                axes[1].plot(ind, signal2)
                axes[1].set_title('Signal 2')
                axes[2].plot(ind, res_signal)
                axes[2].set_title('Result')
                plt.tight_layout()
                plt.show()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please ensure the signals have the same length.")


    def Fast_Conv():
        file_path1 = filedialog.askopenfilename(title="Select Signal File 1", filetypes=[("Text files", "*.txt")])
        file_path2 = filedialog.askopenfilename(title="Select Signal File 2", filetypes=[("Text files", "*.txt")])

        if file_path1 and file_path2:
            data_x = np.loadtxt(file_path1, skiprows=3)
            x_ind = data_x[:, 0]
            x = data_x[:, 1]

            data_h = np.loadtxt(file_path2, skiprows=3)
            h_ind = data_h[:, 0]
            h = data_h[:, 1]
            total_length = len(x) + len(h) - 1
            x_pad = np.pad(x, (0, total_length - len(x)), 'constant')
            h_pad = np.pad(h, (0, total_length - len(h)), 'constant')
            result_ind = list(range(int(min(x_ind) + min(h_ind)), int(max(x_ind) + max(h_ind) + 1)))

            signal1dft = dft(x_pad)
            signal2dft = dft(h_pad)

            fre_conv = signal1dft * signal2dft

            res_signal = idft(fre_conv)

            res_signal = np.round(res_signal.real).astype(int)

            ConvTest.ConvTest(result_ind, res_signal)

            fig, axes = plt.subplots(3, 1, figsize=(12, 10))
            axes[0].plot(x_ind, x)
            axes[0].set_title('X Signal')
            axes[1].plot(h_ind, h)
            axes[1].set_title('H Filter')
            axes[2].plot(result_ind, res_signal)
            axes[2].set_title('Result')
            plt.tight_layout()
            plt.show()

    window = tk.Toplevel()
    window.geometry("470x470")
    window.title("Task 8")

    selected_function = tk.IntVar()
    label_corr = tk.Label(window, text="Correlation", font=("Arial", 25))
    label_corr.grid(row=0, column=1, pady=10, padx=10)

    radio_button1 = tk.Radiobutton(window, text="With Norm", variable=selected_function, font=("Arial", 12), value=1)
    radio_button1.grid(row=1, column=0, pady=10, padx=10)

    radio_button2 = tk.Radiobutton(window, text="Without Norm", variable=selected_function, font=("Arial", 12), value=2)
    radio_button2.grid(row=1, column=2, pady=10, padx=10)

    import_button = tk.Button(window, text="Correlation", padx=15, pady=5, fg="black", bg="lightblue", font=("Arial", 12), command=Fast_Correlation)
    import_button.grid(row=2, column=1, pady=10, padx=10)

    label_conv = tk.Label(window, text="Convolution", font=("Arial", 25))
    label_conv.grid(row=3, column=1, pady=10, padx=10)

    import_button = tk.Button(window, text="Convolution", padx=15, pady=5, fg="black", bg="lightblue", font=("Arial", 12), command=Fast_Conv)
    import_button.grid(row=4, column=1, pady=10, padx=10)

    label_conv = tk.Label(window, text="Exit", font=("Arial", 25))
    label_conv.grid(row=5, column=1, pady=10, padx=10)

    import_button = tk.Button(window, text="Exit", padx=15, pady=5, fg="black", bg="red", font=("Arial", 12), command=window.destroy)
    import_button.grid(row=6, column=1, pady=10, padx=10)

    window.mainloop()