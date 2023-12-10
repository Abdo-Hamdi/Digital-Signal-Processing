import CompareSignal
import ConvTest
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

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
        file_path1 = filedialog.askopenfilename(title="Select Signal File 1", filetypes=[("Text files", "*.txt")])
        file_path2 = filedialog.askopenfilename(title="Select Signal File 2", filetypes=[("Text files", "*.txt")])

        if file_path1 and file_path2:
            try:
                signal1 = np.loadtxt(file_path1, skiprows=3, usecols=1)
                signal2 = np.loadtxt(file_path2, skiprows=3, usecols=1)

                signal1dft = dft(signal1)
                signal2dft = dft(signal2)

                fre_domin_corr = signal1dft * np.conjugate(signal2dft)
                res_signal = idft(fre_domin_corr)
                res_signal = np.round(res_signal.real).astype(int)

                ind = np.array(range(0, len(res_signal)))

                normalization_factor = np.sqrt(np.sum(signal1 ** 2)) * np.sqrt(np.sum(signal2 ** 2))
                normalized_corr_result = res_signal / normalization_factor
                correlation_results = np.zeros(5)
                correlation_results[0] = normalized_corr_result[0]
                cnt = 1
                for i in range(1, 5):
                    correlation_results[cnt] = normalized_corr_result[4 - i + 1]
                    cnt += 1
                CompareSignal.Compare_Signals("CorrOutput.txt", ind, correlation_results)
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please ensure the signals have the same length.")

    def Fast_Covo():
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
            x_padded = np.pad(x, (0, total_length - len(x)), 'constant')
            h_padded = np.pad(h, (0, total_length - len(h)), 'constant')
            result_ind = list(range(int(min(x_ind) + min(h_ind)), int(max(x_ind) + max(h_ind) + 1)))
            signal1dft = dft(x_padded)
            signal2dft = dft(h_padded)
            fre_domin_conv = signal1dft * signal2dft
            res_signal = idft(fre_domin_conv)
            res_signal = np.round(res_signal.real).astype(int)
            ConvTest.ConvTest(result_ind, res_signal)

    window = tk.Tk()
    window.geometry("400x150")
    window.title("Task 8")
    import_button = tk.Button(window, text="Correlation", padx=15, pady=5, fg="black", bg="lightblue", font=("Arial", 12), command=Fast_Correlation)
    import_button.grid(row=0, column=0, pady=10, padx=10)

    import_button = tk.Button(window, text="Convolution", padx=15, pady=5, fg="black", bg="lightblue", font=("Arial", 12), command=Fast_Covo)
    import_button.grid(row=0, column=2, pady=10, padx=10)

    import_button = tk.Button(window, text="Exit", padx=15, pady=5, fg="black", bg="red", font=("Arial", 12), command=exit)
    import_button.grid(row=1, column=1, pady=10, padx=10)

    window.mainloop()