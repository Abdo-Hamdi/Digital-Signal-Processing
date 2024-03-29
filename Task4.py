from tkinter import filedialog, messagebox
import tkinter as tk
import numpy as np
file_path = None
num = 0


def Task4_fun():
    global file_path
    global num

    def QuantizationTest1(file_name, Your_EncodedValues, Your_QuantizedValues):
        expectedEncodedValues = []
        expectedQuantizedValues = []
        with open(file_name, 'r') as f:
            line = f.readline()
            line = f.readline()
            line = f.readline()
            line = f.readline()
            while line:
                # process line
                L = line.strip()
                if len(L.split(' ')) == 2:
                    L = line.split(' ')
                    V2 = str(L[0])
                    V3 = float(L[1])
                    expectedEncodedValues.append(V2)
                    expectedQuantizedValues.append(V3)
                    line = f.readline()
                else:
                    break
        if ((len(Your_EncodedValues) != len(expectedEncodedValues)) or (
                len(Your_QuantizedValues) != len(expectedQuantizedValues))):
            print("QuantizationTest1 Test case failed, your signal have different length from the expected one")
            return
        for i in range(len(Your_EncodedValues)):
            if (Your_EncodedValues[i] != expectedEncodedValues[i]):
                print(
                    "QuantizationTest1 Test case failed, your EncodedValues have different EncodedValues from the expected one")
                return
        for i in range(len(expectedQuantizedValues)):
            if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
                continue
            else:
                print(
                    "QuantizationTest1 Test case failed, your QuantizedValues have different values from the expected one")
                return
        print("QuantizationTest1 Test case passed successfully")

    def QuantizationTest2(file_name, Your_IntervalIndices, Your_EncodedValues, Your_QuantizedValues, Your_SampledError):
        expectedIntervalIndices = []
        expectedEncodedValues = []
        expectedQuantizedValues = []
        expectedSampledError = []
        with open(file_name, 'r') as f:
            line = f.readline()
            line = f.readline()
            line = f.readline()
            line = f.readline()
            while line:
                # process line
                L = line.strip()
                if len(L.split(' ')) == 4:
                    L = line.split(' ')
                    V1 = int(L[0])
                    V2 = str(L[1])
                    V3 = float(L[2])
                    V4 = float(L[3])
                    expectedIntervalIndices.append(V1)
                    expectedEncodedValues.append(V2)
                    expectedQuantizedValues.append(V3)
                    expectedSampledError.append(V4)
                    line = f.readline()
                else:
                    break
        if (len(Your_IntervalIndices) != len(expectedIntervalIndices)
                or len(Your_EncodedValues) != len(expectedEncodedValues)
                or len(Your_QuantizedValues) != len(expectedQuantizedValues)
                or len(Your_SampledError) != len(expectedSampledError)):
            print("QuantizationTest2 Test case failed, your signal have different length from the expected one")
            return
        for i in range(len(Your_IntervalIndices)):
            if (Your_IntervalIndices[i] != expectedIntervalIndices[i]):
                print("QuantizationTest2 Test case failed, your signal have different indicies from the expected one")
                return
        for i in range(len(Your_EncodedValues)):
            if (Your_EncodedValues[i] != expectedEncodedValues[i]):
                print(
                    "QuantizationTest2 Test case failed, your EncodedValues have different EncodedValues from the expected one")
                return

        for i in range(len(expectedQuantizedValues)):
            if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
                continue
            else:
                print(
                    "QuantizationTest2 Test case failed, your QuantizedValues have different values from the expected one")
                return
        for i in range(len(expectedSampledError)):
            if abs(Your_SampledError[i] - expectedSampledError[i]) < 0.01:
                continue
            else:
                print(
                    "QuantizationTest2 Test case failed, your SampledError have different values from the expected one")
                return
        print("QuantizationTest2 Test case passed successfully")
    window = tk.Tk()
    window.title("Task 4")
    window.geometry("400x250")

    def exit_application():
        exit()

    def show_error_message():
        message = "Please Choose One Operation"
        messagebox.showinfo("Error", message)

    def open_file(entry):
        global file_path
        file_path = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

    def Task_bits():
        if file_path is None:
            messagebox.showerror("Error", "Please select a signal file.")
            return

        num_bits = entry2.get()
        try:
            num = int(num_bits)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of levels.")
            return

        signal = np.loadtxt(file_path, skiprows=3, usecols=(1,))
        n = len(signal)
        minofsignal = np.min(signal)
        maxofsignal = np.max(signal)
        numoflevel = 2 ** num
        delta = (maxofsignal - minofsignal) / numoflevel
        listminlevel = []
        listmaxlevel = []
        listmidpoint = []
        for i in range(numoflevel):
            listminlevel.append(minofsignal + i * delta)
            listmaxlevel.append(minofsignal + (i + 1) * delta)
            listmidpoint.append("{:.2f}".format((listminlevel[i] + listmaxlevel[i]) / 2))

        out1 = []
        out2 = []

        for s in signal:
            for j in range(numoflevel):
                if listminlevel[j] <= s <= listmaxlevel[j]:
                    binary_repr = bin(j)[2:].zfill(num)
                    out1.append(binary_repr)
                    out2.append(float(listmidpoint[j]))
                    break

        data = np.column_stack((out1, out2))
        header = f"0\n0\n{n}"
        file_name = "output1.txt"
        np.savetxt(file_name, data, header=header, comments='', fmt='%s', delimiter='\t', encoding='utf-8')
        QuantizationTest1("Quan1_Out.txt",out1,out2)
        print("Finished")

    def Task_levels():
        if file_path is None:
            messagebox.showerror("Error", "Please select a signal file.")
            return

        num_bits = entry2.get()
        try:
            num = int(num_bits)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of levels.")
            return

        signal = np.loadtxt(file_path, skiprows=3, usecols=(1,))
        n = len(signal)
        minofsignal = np.min(signal)
        maxofsignal = np.max(signal)
        numoflevel = num
        delta = (maxofsignal - minofsignal) / numoflevel
        delta = np.round(delta, 2)  # Round delta to 3 decimal places
        listminlevel = []
        listmaxlevel = []
        listmidpoint = []
        for i in range(numoflevel):
            listminlevel.append("{:.2f}".format(minofsignal + i * delta))
            listmaxlevel.append("{:.2f}".format(minofsignal + (i + 1) * delta))
            listmidpoint.append("{:.3f}".format((float(listminlevel[i]) + float(listmaxlevel[i])) / 2))

        out_level = []
        out_level_bin = []
        out_mid = []
        out_error = []
        num = int(np.log2(num))
        for s in signal:
            for j in range(numoflevel):
                if float(listminlevel[j]) <= s <= float(listmaxlevel[j]):
                    binary_repr = bin(j)[2:].zfill(num)
                    out_level.append(j + 1)
                    out_level_bin.append(binary_repr)
                    out_mid.append(float(listmidpoint[j]))
                    out_error.append(float("{:.3f}".format(float(listmidpoint[j]) - s)))
                    break

        data = np.column_stack((out_level, out_level_bin, out_mid, out_error))
        header = f"0\n0\n{n}"
        file_name = "output2.txt"
        np.savetxt(file_name, data, header=header, comments='', fmt='%s', delimiter='\t', encoding='utf-8')
        QuantizationTest2("Quan2_Out.txt",out_level,out_level_bin,out_mid,out_error)
        print("Finished")

    # Create labels
    label1 = tk.Label(window, text="Signal File:")
    label1.grid(row=0, column=0, padx=10, pady=10, sticky='e')

    label2 = tk.Label(window, text="Number:")
    label2.grid(row=1, column=0, padx=10, pady=10, sticky='e')

    # Entry widgets to display selected file paths
    entry1 = tk.Entry(window)
    entry1.grid(row=0, column=1, padx=10, pady=10)

    entry2 = tk.Entry(window)
    entry2.grid(row=1, column=1, padx=10, pady=10)

    browse_button1 = tk.Button(window, text="Browse", command=lambda: open_file(entry1))
    browse_button1.grid(row=0, column=2, padx=10, pady=10)

    exit_button = tk.Button(window, text="Exit", padx=15, pady=5, fg="black", bg="red", font=("Arial", 12),
                            command=exit_application)
    exit_button.grid(row=2, column=2, padx=10, pady=10)

    open_task_button1 = tk.Button(window, text="Bits", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                 command=Task_bits)
    open_task_button1.grid(row=2, column=0, padx=10, pady=10)

    open_task_button2 = tk.Button(window, text="Levels", padx=15, pady=5, fg="black", bg="gray", font=("Arial", 12),
                                 command=Task_levels)
    open_task_button2.grid(row=2, column=1, padx=10, pady=10)

    window.mainloop()

