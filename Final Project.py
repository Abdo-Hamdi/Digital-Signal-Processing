import tkinter as tk
import numpy as np
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import os
import Uitlites as ui
from scipy.signal import resample


def filesCollect():
    folder_path1 = filedialog.askdirectory(title="Select Folder Containing Text Files")
    folder_path2 = filedialog.askdirectory(title="Select Folder Containing Text Files")
    # Get a list of all files in the folder
    file_list1 = os.listdir(folder_path1)
    file_list2 = os.listdir(folder_path2)
    # Filter out only the text files
    text_files1 = [file for file in file_list1 if file.endswith('.txt')]
    text_files2 = [file for file in file_list2 if file.endswith('.txt')]
    # Initialize a list to store signals
    all_signals1 = []
    all_signals2 = []
    # Loop through each text file and read the signal
    for file_name in text_files1:
        file_path = os.path.join(folder_path1, file_name)
        try:
            # Assuming the signal is in the second column (change as needed)
            signal = np.loadtxt(file_path)
            fig, axes = plt.subplots(1, 1, figsize=(5, 5))
            axes.plot(signal)
            axes.set_title('Signal 1')
            plt.tight_layout()
            plt.show()
            # Append the signal to the list
            all_signals1.append(signal)
        except Exception as e:
            print(f"Error reading {file_name}: {e}")
    for file_name in text_files2:
        file_path = os.path.join(folder_path2, file_name)
        try:
            # Assuming the signal is in the second column (change as needed)
            signal = np.loadtxt(file_path)
            fig, axes = plt.subplots(1, 1, figsize=(5, 5))
            axes.plot(signal)
            axes.set_title('Signal 2')
            plt.tight_layout()
            plt.show()
            # Append the signal to the list
            all_signals2.append(signal)
        except Exception as e:
            print(f"Error reading {file_name}: {e}")
    return all_signals1, all_signals2


def band_pass2(FS, StopBandAttenuation, F1, F2, TransitionBand, newfs):
    TS = TransitionBand / FS
    N, window = ui.generate_window(TS, StopBandAttenuation)
    cutoff_freq1 = F1 - (TransitionBand / 2)
    cutoff_freq2 = F2 + (TransitionBand / 2)
    cutoff_freq1 /= FS
    cutoff_freq2 /= FS
    st = (N // 2)
    taps = np.zeros(st + 1)
    coff1 = np.zeros(st + 1)

    for i in range(0, st + 1):
        if i == 0:
            taps[i] = 2 * (cutoff_freq2 - cutoff_freq1)
        else:
            taps[i] = (np.sin(2 * np.pi * cutoff_freq2 * i) / (np.pi * i)) - (
                    np.sin(2 * np.pi * cutoff_freq1 * i) / (np.pi * i))
        coff1[i] = taps[i] * window[i]

    coff2 = coff1[1:][::-1]
    coff = np.concatenate((coff2, coff1))
    A, B = filesCollect()
    res_signalA = []
    res_signalB = []
    for i in range(len(A)):
        res_signal = ui.Convo(A[i], coff)
        res_signalA.append(res_signal)

    for i in range(len(B)):
        res_signal = ui.Convo(B[i], coff)
        res_signalB.append(res_signal)
    print("Conv A and B")
    resample2(FS, newfs, res_signalA, res_signalB, A, B)


def resample2(FS, newFS, res_signalA, res_signalB, A, B):
    if newFS >= 2 * FS:
        L = int(newFS / FS)
        M = int(FS / newFS)

        if L > 0:
            upsampled_signals_A = []
            for signal in A:
                upsampled_signal_A = resample(signal, L * len(signal))
                upsampled_signals_A.append(upsampled_signal_A)
            upsampled_signals_B = []
            for signal in B:
                upsampled_signal_B = resample(signal, L * len(signal))
                upsampled_signals_B.append(upsampled_signal_B)

            print("up sampling A and B")
            A_DC = []
            B_DC = []
            for i in range(0, len(upsampled_signals_A)):
                t = ui.CALC_DC(upsampled_signals_A[i])
                A_DC.append(t)
            for i in range(0, len(upsampled_signals_B)):
                t = ui.CALC_DC(upsampled_signals_B[i])
                B_DC.append(t)
            print("DC A and B")
            A_norm = []
            B_norm = []
            for i in range(0, len(A_DC)):
                t = (A_DC[i] - np.mean(A_DC[i])) / np.std(A_DC[i])
                A_norm.append(t)
            for i in range(0, len(B_DC)):
                t = (B_DC[i] - np.mean(B_DC[i])) / np.std(B_DC[i])
                B_norm.append(t)
            print("Norm A and B")
            A_corr = []
            B_corr = []
            for i in range(0, len(A_norm)):
                t = ui.Correlation(A_norm[i], A_norm[i])
                A_corr.append(t)
            for i in range(0, len(B_norm)):
                t = ui.Correlation(B_norm[i], B_norm[i])
                B_corr.append(t)
            print("Corr A and B")
            A_coff = []
            B_coff = []
            for i in range(0, len(A_corr)):
                midpo = len(A_corr) // 2
                t = A_corr[midpo:]
                A_coff.append(t)
            for i in range(0, len(B_corr)):
                midpo = len(B_corr) // 2
                t = B_corr[midpo:]
                B_coff.append(t)
            print("Coff A and B")

            A_Dct = []
            B_Dct = []
            for i in range(0, len(A_coff)):
                for value in A_coff[i]:
                    t = ui.CALC_DCT(value)
                    A_Dct.append(t)
            for i in range(0, len(B_coff)):
                for value in A_coff[i]:
                    t = ui.CALC_DCT(value)
                    B_Dct.append(t)
            print("Dct A and B")

            ui.temp_match(A_Dct , B_Dct)

        elif M > 0:
            resultA = []
            resultB = []
            for j in range(0, len(res_signalA)):
                for i in range(0, len(res_signalA[j]), M):
                    result = (res_signalA[j][i])
                    resultA.append(result)
            for j in range(0, len(res_signalB)):
                for i in range(0, len(res_signalB[j]), M):
                    result = (res_signalB[j][i])
                    resultB.append(result)
            print("Down Sampling A and B")
            A_DC = []
            B_DC = []
            for i in range(0, len(resultA)):
                t = ui.CALC_DC(resultA[i])
                A_DC.append(t)
            for i in range(0, len(resultB)):
                t = ui.CALC_DC(resultB[i])
                B_DC.append(t)
            print("DC A and B")
            A_norm = []
            B_norm = []
            for i in range(0, len(A_DC)):
                t = (A_DC[i] - np.mean(A_DC[i])) / np.std(A_DC[i])
                A_norm.append(t)
            for i in range(0, len(B_DC)):
                t = (B_DC[i] - np.mean(B_DC[i])) / np.std(B_DC[i])
                B_norm.append(t)
            print("Norm A and B")
            A_corr = []
            B_corr = []
            for i in range(0, len(A_norm)):
                t = ui.Correlation(A_norm[i], A_norm[i])
                A_corr.append(t)
            for i in range(0, len(B_norm)):
                t = ui.Correlation(B_norm[i], B_norm[i])
                B_corr.append(t)
            print("Corr A and B")
            A_coff = []
            B_coff = []
            for i in range(0, len(A_corr)):
                midpo = len(A_corr) // 2
                t = A_corr[midpo:]
                A_coff.append(t)
            for i in range(0, len(B_corr)):
                midpo = len(B_corr) // 2
                t = B_corr[midpo:]
                B_coff.append(t)
            print("Coff A and B")

            A_Dct = []
            B_Dct = []
            for i in range(0, len(A_coff)):
                t = ui.CALC_DCT(A_coff[i])
                A_Dct.append(t)
            for i in range(0, len(B_coff)):
                t = ui.CALC_DCT(B_coff[i])
                B_Dct.append(t)
            print("Dct A and B")

            ui.temp_match(A_Dct, B_Dct)
    else:
        print("No Sample A and B")
        messagebox.showwarning("newFs is not valid.")
        A_DC = []
        B_DC = []
        for i in range(0, len(res_signalA)):
            t = ui.CALC_DC(res_signalA[i])
            A_DC.append(t)
        for i in range(0, len(res_signalB)):
            t = ui.CALC_DC(res_signalB[i])
            B_DC.append(t)
        print("DC A and B")
        A_norm = []
        B_norm = []
        for i in range(0, len(A_DC)):
            t = (A_DC[i] - np.mean(A_DC[i])) / np.std(A_DC[i])
            A_norm.append(t)
        for i in range(0, len(B_DC)):
            t = (B_DC[i] - np.mean(B_DC[i])) / np.std(B_DC[i])
            B_norm.append(t)
        print("Norm A and B")
        A_corr = []
        B_corr = []
        for i in range(0, len(A_norm)):
            t = ui.Correlation(A_norm[i], A_norm[i])
            A_corr.append(t)
        for i in range(0, len(B_norm)):
            t = ui.Correlation(B_norm[i], B_norm[i])
            B_corr.append(t)
        print("Corr A and B")
        A_coff = []
        B_coff = []
        for i in range(0, len(A_corr)):
            midpo = len(A_corr) // 2
            t = A_corr[midpo:]
            A_coff.append(t)
        for i in range(0, len(B_corr)):
            midpo = len(B_corr) // 2
            t = B_corr[midpo:]
            B_coff.append(t)
        print("Coff A and B")

        A_Dct = []
        B_Dct = []
        for i in range(0, len(A_coff)):
            t = ui.CALC_DCT(A_coff[i])
            A_Dct.append(t)
        for i in range(0, len(B_coff)):
            t = ui.CALC_DCT(B_coff[i])
            B_Dct.append(t)
        print("Dct A and B")

        ui.temp_match(A_Dct, B_Dct)

def browse_test():
    global fs, stopband, TransBand, f1, f2, newfs
    fs = int(entry4.get() or 0)
    f1 = int(entry2.get() or 0)
    f2 = int(entry3.get() or 0)
    stopband = int(entry5.get() or 0)
    TransBand = int(entry6.get() or 0)
    newfs = int(entry7.get() or 0)
    band_pass2(fs, stopband, f1, f2, TransBand, newfs)


window = tk.Tk()
window.geometry("350x400")
window.title("Final Project")

label = tk.Label(window, text="Enter F1:")
label.grid(row=4, column=0, pady=10, padx=10)
label = tk.Label(window, text="Enter F2:")
label.grid(row=5, column=0, pady=10, padx=10)

entry2 = tk.Entry(window, state=tk.NORMAL)
entry2.grid(row=4, column=1, pady=10, padx=10)
entry3 = tk.Entry(window, state=tk.NORMAL)
entry3.grid(row=5, column=1, pady=10, padx=10)

label = tk.Label(window, text="Enter FS:")
label.grid(row=6, column=0, pady=10, padx=10)
label = tk.Label(window, text="Enter StopBandAttenuation:")
label.grid(row=7, column=0, pady=10, padx=10)
label = tk.Label(window, text="Enter TransitionBand:")
label.grid(row=8, column=0, pady=10, padx=10)

entry4 = tk.Entry(window, state=tk.NORMAL)
entry4.grid(row=6, column=1, pady=10, padx=10)
entry5 = tk.Entry(window, state=tk.NORMAL)
entry5.grid(row=7, column=1, pady=10, padx=10)
entry6 = tk.Entry(window, state=tk.NORMAL)
entry6.grid(row=8, column=1, pady=10, padx=10)

label = tk.Label(window, text="Enter New FS :")
label.grid(row=9, column=0, pady=10, padx=10)
entry7 = tk.Entry(window, state=tk.NORMAL)
entry7.grid(row=9, column=1, pady=10, padx=10)

open_task_button = tk.Button(window, text="Browse", padx=15, pady=10, command=browse_test)
open_task_button.grid(row=11, column=0, pady=10, padx=10)
open_task_button = tk.Button(window, text="Exit", padx=15, pady=10, command=window.destroy)
open_task_button.grid(row=11, column=1, pady=10, padx=10)
window.mainloop()
