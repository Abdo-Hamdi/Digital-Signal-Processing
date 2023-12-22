import tkinter as tk
from tkinter import ttk
import numpy as np
import CompareSignalFIR
from tkinter import filedialog,messagebox
import Uitlites as ui

def Task10_fun():
    window = tk.Toplevel()
    window.geometry("450x600")
    window.title("Task 9")


    def low_pass(FS, StopBandAttenuation, FC, TransitionBand):
        result_ind, res_signal = ui.Low_pass(FS, StopBandAttenuation, FC, TransitionBand)
        CompareSignalFIR.Compare_Signals("ecg_low_pass_filtered.txt", result_ind, res_signal)

    def high_pass(FS, StopBandAttenuation, FC, TransitionBand):
        result_ind, res_signal=ui.High_pass(FS, StopBandAttenuation, FC, TransitionBand)
        CompareSignalFIR.Compare_Signals("ecg_high_pass_filtered.txt", result_ind, res_signal)


    def band_pass(FS, StopBandAttenuation, F1, F2, TransitionBand):
        result_ind, res_signal = ui.Band_pass(FS, StopBandAttenuation, F1, F2, TransitionBand)
        CompareSignalFIR.Compare_Signals("ecg_band_pass_filtered.txt", result_ind, res_signal)


    def band_stop(FS, StopBandAttenuation, F1, F2, TransitionBand):
        result_ind, res_signal = ui.Band_stop(FS, StopBandAttenuation, F1, F2, TransitionBand)
        CompareSignalFIR.Compare_Signals("ecg_band_stop_filtered.txt", result_ind, res_signal)

    def Resample():
        global fs, stopband, TransBand, fc
        fc = int(entry1.get() or 0)
        fs = int(entry4.get() or 0)
        stopband = int(entry5.get() or 0)
        TransBand = int(entry6.get() or 0)
        L = int(entry7.get() or 0)
        M = int(entry8.get() or 0)

        if L != 0 and M == 0:
            file_path = filedialog.askopenfilename(title="Select Signal File", filetypes=[("Text files", "*.txt")])
            if file_path:
                x = np.loadtxt(file_path, skiprows=3, usecols=1).astype(int)
            res = []
            for i in range(len(x)):
                res.append(x[i])
                if i == len(x) - 1:
                    break;
                for j in range(L - 1):
                    res.append(0)
            newx_ind = list(range(0, len(res)))
            data = np.column_stack((newx_ind, res))
            header = f"0\n0\n{len(res)}"
            file_name = "upsample.txt"
            np.savetxt(file_name, data, header=header, comments='', fmt='%s', delimiter='\t', encoding='utf-8')
            res_ind , res = ui.Low_pass(fs,stopband,fc,TransBand)
            CompareSignalFIR.Compare_Signals("Sampling_Up.txt",res_ind,res)

        elif M != 0 and L == 0:
            res_ind, res = ui.Low_pass(fs, stopband, fc, TransBand)
            result = []
            for i in range(0, len(res), M):
                result.append(res[i])
            newx_ind = list(range(res_ind[0], len(result) + res_ind[0]))
            CompareSignalFIR.Compare_Signals("Sampling_Down.txt",newx_ind,result)

        elif M != 0 and L != 0:
            file_path = filedialog.askopenfilename(title="Select Signal File", filetypes=[("Text files", "*.txt")])
            if file_path:
                x = np.loadtxt(file_path, skiprows=3, usecols=1).astype(int)
            res = []
            for i in range(len(x)):
                res.append(x[i])
                if i == len(x) - 1:
                    break;
                for j in range(L - 1):
                    res.append(0)
            newx_ind = list(range(0, len(res)))
            data = np.column_stack((newx_ind, res))
            header = f"0\n0\n{len(res)}"
            file_name = "upsample.txt"
            np.savetxt(file_name, data, header=header, comments='', fmt='%s', delimiter='\t', encoding='utf-8')
            res_ind, res = ui.Low_pass(fs, stopband, fc, TransBand)
            result = []
            for i in range(0, len(res), M):
                result.append(res[i])
            newx_ind = list(range(res_ind[0], len(result) + res_ind[0]))
            print(newx_ind)
            print(result)
            CompareSignalFIR.Compare_Signals("Sampling_Up_Down.txt",newx_ind,result)

        else:
            messagebox.showerror("Invaild Values")
    def toggle_entry_state1():
        if var1.get() == 1:
            entry1.config(state=tk.NORMAL)
        else:
            entry1.config(state=tk.DISABLED)

    def toggle_entry_state2():
        if var2.get() == 1:
            entry2.config(state=tk.NORMAL)
            entry3.config(state=tk.NORMAL)
        else:
            entry2.config(state=tk.DISABLED)
            entry3.config(state=tk.DISABLED)

    def browse_test():
        global fs, stopband, TransBand, fc, f1, f2
        fc = int(entry1.get() or 0)
        fs = int(entry4.get() or 0)
        f1 = int(entry2.get() or 0)
        f2 = int(entry3.get() or 0)
        stopband = int(entry5.get() or 0)
        TransBand = int(entry6.get() or 0)
        if feature1.get() == "Low":
            low_pass(fs, stopband, fc, TransBand)
        elif feature1.get() == "High":
            high_pass(fs, stopband, fc, TransBand)
        elif feature1.get() == "Band Pass":
            band_pass(fs, stopband, f1, f2, TransBand)
        elif feature1.get() == "Band Stop":
            band_stop(fs, stopband, f1, f2, TransBand)

    feature1 = tk.StringVar()
    var1 = tk.IntVar()
    var2 = tk.IntVar()

    tk.Label(window, text="Select The Filter : ").grid(row=0, column=0, pady=10, padx=10)

    feature1_combobox = ttk.Combobox(window, textvariable=feature1, values=["Low", "High", "Band Pass", "Band Stop"])
    feature1_combobox.grid(row=0, column=1, pady=10, padx=10)

    radio_button = tk.Checkbutton(window, text="Low or High", variable=var1, command=toggle_entry_state1)
    radio_button.grid(row=1, column=0, pady=10, padx=10)

    label = tk.Label(window, text="Enter Fc:")
    label.grid(row=2, column=0, pady=10, padx=10)

    entry1 = tk.Entry(window, state=tk.DISABLED)
    entry1.grid(row=2, column=1, pady=10, padx=10)

    radio_button = tk.Checkbutton(window, text="Band Pass or Band Stop", variable=var2, command=toggle_entry_state2)
    radio_button.grid(row=3, column=0, pady=10, padx=20)

    label = tk.Label(window, text="Enter F1:")
    label.grid(row=4, column=0, pady=10, padx=10)
    label = tk.Label(window, text="Enter F2:")
    label.grid(row=5, column=0, pady=10, padx=10)

    entry2 = tk.Entry(window, state=tk.DISABLED)
    entry2.grid(row=4, column=1, pady=10, padx=10)
    entry3 = tk.Entry(window, state=tk.DISABLED)
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

    label = tk.Label(window, text="Enter L :")
    label.grid(row=9, column=0, pady=10, padx=10)
    label = tk.Label(window, text="Enter M :")
    label.grid(row=10, column=0, pady=10, padx=10)
    entry7 = tk.Entry(window, state=tk.NORMAL)
    entry7.grid(row=9, column=1, pady=10, padx=10)
    entry8 = tk.Entry(window, state=tk.NORMAL)
    entry8.grid(row=10, column=1, pady=10, padx=10)

    open_task_button = tk.Button(window, text="FIR", padx=15, pady=10, command=browse_test)
    open_task_button.grid(row=11, column=0, pady=10, padx=10)
    open_task_button = tk.Button(window, text="ReSampling", padx=15, pady=10, command=Resample)
    open_task_button.grid(row=11, column=1, pady=10, padx=10)
    open_task_button = tk.Button(window, text="Exit", padx=15, pady=10, command=window.destroy)
    open_task_button.grid(row=11, column=2, pady=10, padx=10)
    window.mainloop()
