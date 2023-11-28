import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import Shift_Fold_Signal
import comparesignal2
import comparesignals
import ConvTest

def Task7_fun():

    def shift_right():
        file_path = filedialog.askopenfilename(title="Select a signal file")
        col1_r = []
        col2_r = []
        col1_after_shift=[]
        shift_value = int(shiftvaluenofolding_entry.get())
        if file_path:
            with open(file_path, 'r') as file:
                data = np.loadtxt(file, skiprows=3)
                col1_r = data[:, 0]
                col2_r = data[:, 1]
        col1_after_shift = col1_r - shift_value

        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        axes[0].plot(col1_r, col2_r)
        axes[0].set_title('Original Signal')
        axes[1].plot(col1_after_shift, col2_r)
        axes[1].set_title('Shifted Signal')
        plt.tight_layout()
        plt.show()


    def shift_left():
        file_path = filedialog.askopenfilename(title="Select a signal file")
        col1_l = []
        col2_l = []
        col1_after_shift = []
        shift_value = int(shiftvaluenofolding_entry.get())
        if file_path:
            with open(file_path, 'r') as file:
                data = np.loadtxt(file, skiprows=3)
                col1_l = data[:, 0]
                col2_l = data[:, 1]
        col1_after_shift = col1_l + shift_value

        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        axes[0].plot(col1_l, col2_l)
        axes[0].set_title('Original Signal')
        axes[1].plot(col1_after_shift, col2_l)
        axes[1].set_title('Shifted Signal')
        plt.tight_layout()
        plt.show()


    col1 = []
    col2 = []
    col2_after_fold = []
    def fold():
        global col1, col2, col2_after_fold
        file_path = filedialog.askopenfilename(title="Select a signal file")
        if file_path:
            with open(file_path, 'r') as file:
                data = np.loadtxt(file, skiprows=3)
                col1 = data[:, 0]
                col2 = data[:, 1]
        col2_after_fold = col2[::-1]
        Shift_Fold_Signal.Shift_Fold_Signal("Output_fold.txt", col1, col2_after_fold)
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        axes[0].plot(col1, col2)
        axes[0].set_title('Original Signal')
        axes[1].plot(col1, col2_after_fold)
        axes[1].set_title('Folded Signal')
        plt.tight_layout()
        plt.show()

    def shift_right_after():
        global col1, col2, col2_after_fold
        shift_value = int(shiftvaluefolding_entry.get())
        col1_1 = col1
        col2_1 = col2
        col2_fold = col2_after_fold
        col1_after_shift = col1 + shift_value
        Shift_Fold_Signal.Shift_Fold_Signal("Output_ShifFoldedby500.txt", col1_after_shift, col2_fold)
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        axes[0].plot(col1_1, col2_1)
        axes[0].set_title('Original Signal')
        axes[1].plot(col1_after_shift, col2_fold)
        axes[1].set_title('Shifted, Folded Signal')
        plt.tight_layout()
        plt.show()

    def shift_left_after():
        global col1, col2, col2_after_fold
        shift_value = int(shiftvaluefolding_entry.get())
        col1_1 = col1
        col2_1 = col2
        col2_fold = col2_after_fold
        col1_after_shift = col1 - shift_value
        Shift_Fold_Signal.Shift_Fold_Signal("Output_ShiftFoldedby-500.txt", col1_after_shift, col2_fold)
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        axes[0].plot(col1_1, col2_1)
        axes[0].set_title('Original Signal')
        axes[1].plot(col1_after_shift, col2_fold)
        axes[1].set_title('Shifted, Folded Signal')
        plt.tight_layout()
        plt.show()


    def DC_Remover():
        file_path = filedialog.askopenfilename(title="Select a signal file")
        signal = []
        signal_after = []
        if file_path:
            with open(file_path, 'r') as file:
                signal = np.loadtxt(file, skiprows=3, usecols=(1,))
                N = len(signal)
                dft_result = np.zeros(N, dtype=np.complex128)
                idft_result = np.zeros(N, dtype=np.complex128)
                for k in range(N):
                    for n in range(N):
                        angle = 2 * np.pi * k * n / N
                        dft_result[k] += signal[n] * np.exp(-1j * angle)

                dft_result[0] = 0

                for n in range(N):
                    for k in range(N):
                        angle = 2 * np.pi * k * n / N
                        idft_result[n] += dft_result[k] * np.exp(1j * angle)
                idft_result /= N
                signal_after = idft_result
        comparesignal2.SignalSamplesAreEqual("DC_component_output.txt",signal_after)
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        axes[0].plot(signal)
        axes[0].set_title('Original Signal')
        axes[1].plot(signal_after.real)
        axes[1].set_title('Signal after DC Component Removal')
        plt.tight_layout()
        plt.show()


    def moving_avg():
        file_path = filedialog.askopenfilename(title="Select a signal file")
        data = []
        if file_path:
            with open(file_path, 'r') as file:
                data = np.loadtxt(file, skiprows=3)
                in1 = data[:, 0]
                in2 = data[:, 1]
        windowsize = int(windowsizeentry.get())
        out1 = []
        out2 = []
        out1 = in1[:-(windowsize - 1)]
        for i in range(len(in2) - windowsize + 1):
            result = np.sum(in2[i:i+windowsize]) / windowsize
            rounded_result = np.round(result, 6)
            out2.append(rounded_result)
        if(windowsize == 3):
            comparesignals.SignalSamplesAreEqual("OutMovAvgTest1.txt",out1,out2)
        else:
            comparesignals.SignalSamplesAreEqual("OutMovAvgTest2.txt", out1, out2)



    def Convolution():
        data_x = []
        data_h = []
        x = []
        x_ind = []
        h = []
        h_ind = []
        file_path = filedialog.askopenfilename(title="Select a x file")
        if file_path:
            with open(file_path, 'r') as file:
                data_x = np.loadtxt(file, skiprows=3)
                x_ind = data_x[:, 0]
                x = data_x[:, 1]
        file_path = filedialog.askopenfilename(title="Select a x file")
        if file_path:
            with open(file_path, 'r') as file:
                data_h = np.loadtxt(file, skiprows=3)
                h_ind = data_h[:, 0]
                h = data_h[:, 1]

        x_len = len(x)
        h_len = len(h)
        result_length = x_len + h_len - 1
        result_ind =[]
        result_ind = list(range(int(min(x_ind) + min(h_ind)), int(max(x_ind) + max(h_ind) + 1)))
        result = [0] * result_length

        for n in result_ind:
            for j, k in zip(x_ind, range(h_len)):
                if (n - j) >= 0 and (n - j) < h_len:
                    result[int(n - min(result_ind))] += x[int(j - min(x_ind))] * h[int(n - j)]

        ConvTest.ConvTest(result_ind,result)
        fig, axes = plt.subplots(3, 1, figsize=(12, 10))
        axes[0].plot(x_ind, x)
        axes[0].set_title('X Signal')
        axes[1].plot(h_ind, h)
        axes[1].set_title('H Filter')
        axes[2].plot(result_ind, result)
        axes[2].set_title('Result')
        plt.tight_layout()
        plt.show()


    def DerivativeSignal():
        InputSignal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                       28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                       53,
                       54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
                       79,
                       80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
        expectedOutput_first = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1]
        expectedOutput_second = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0]

        """
        Write your Code here:
        Start
        """
        FirstDrev = []
        # Y(n) = x(n)-x(n-1)
        for i in range(1, len(InputSignal)):
            diff = InputSignal[i] - InputSignal[i - 1]
            FirstDrev.append(diff)
        SecondDrev = []
        # Y(n)= x(n+1)-2x(n)+x(n-1)
        for i in range(1, len(InputSignal) - 1):
            diff = -2 * InputSignal[i] + InputSignal[i - 1] + InputSignal[i + 1]
            SecondDrev.append(diff)

        """
        End
        """
        fig, axes = plt.subplots(3, 1, figsize=(12, 10))
        axes[0].plot(InputSignal)
        axes[0].set_title('X Signal')
        axes[1].plot(FirstDrev)
        axes[1].set_title('First')
        axes[2].plot(SecondDrev)
        axes[2].set_title('Second')
        plt.tight_layout()
        plt.show()
        """
        Testing your Code
        """
        if ((len(FirstDrev) != len(expectedOutput_first)) or (len(SecondDrev) != len(expectedOutput_second))):
            print("mismatch in length")
            return
        first = second = True
        for i in range(len(expectedOutput_first)):
            if abs(FirstDrev[i] - expectedOutput_first[i]) < 0.01:
                continue
            else:
                first = False
                print("1st derivative wrong")
                return
        for i in range(len(expectedOutput_second)):
            if abs(SecondDrev[i] - expectedOutput_second[i]) < 0.01:
                continue
            else:
                second = False
                print("2nd derivative wrong")
                return
        if (first and second):
            print("Derivative Test case passed successfully")
        else:
            print("Derivative Test case failed")
        return

    def Exit():
        exit()


    window = tk.Tk()
    window.geometry("550x600")
    window.title("Task 7")

    shiftvaluenofolding = tk.Label(window, text="Enter Shift Value :")
    shiftvaluenofolding.grid(row=0, column=0, padx=10, pady=10, sticky='e')

    shiftvaluenofolding_entry = tk.Entry(window)
    shiftvaluenofolding_entry.grid(row=0, column=1, padx=10, pady=10)

    open_task_button1 = tk.Button(window, text="Shift Right", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                     command=shift_right)
    open_task_button1.grid(row=1, column=0, padx=10, pady=10)
    open_task_button2 = tk.Button(window, text="Shift Left", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                     command=shift_left)
    open_task_button2.grid(row=1, column=2, padx=10, pady=10)
    open_task_button3 = tk.Button(window, text="Fold", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                     command=fold)
    open_task_button3.grid(row=2, column=1, padx=10, pady=10)
    shiftvaluefolding = tk.Label(window, text="Enter Shift Value after Fold :")
    shiftvaluefolding.grid(row=3, column=0, padx=10, pady=10, sticky='e')

    shiftvaluefolding_entry = tk.Entry(window)
    shiftvaluefolding_entry.grid(row=3, column=1, padx=10, pady=10)
    open_task_button4 = tk.Button(window, text="Shift Right After", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                     command=shift_right_after)
    open_task_button4.grid(row=4, column=0, padx=10, pady=10)
    open_task_button5 = tk.Button(window, text="Shift Left After", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                     command=shift_left_after)
    open_task_button5.grid(row=4, column=2, padx=10, pady=10)
    open_task_button6 = tk.Button(window, text="Dc Remover", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                     command=DC_Remover)
    open_task_button6.grid(row=5, column=1, padx=10, pady=10)

    windowsizelabel = tk.Label(window, text="Enter Window Size :")
    windowsizelabel.grid(row=6, column=0, padx=10, pady=10, sticky='e')

    windowsizeentry = tk.Entry(window)
    windowsizeentry.grid(row=6, column=1, padx=10, pady=10)
    open_task_button7 = tk.Button(window, text="Moving Average", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                     command=moving_avg)
    open_task_button7.grid(row=7, column=1, padx=10, pady=10)
    open_task_button8 = tk.Button(window, text="Convolution", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                     command=Convolution)
    open_task_button8.grid(row=8, column=1, padx=10, pady=10)
    open_task_button9 = tk.Button(window, text="Derivative", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                     command=DerivativeSignal)
    open_task_button9.grid(row=9, column=1, padx=10, pady=10)
    open_task_button10 = tk.Button(window, text="Exit", padx=15, pady=5, fg="black", bg="red", font=("Arial", 12),
                                     command=Exit)
    open_task_button10.grid(row=10, column=1, padx=10, pady=10)
    window.mainloop()