from tkinter import filedialog, messagebox
import tkinter as tk
import numpy as np

file_path = None
num = 0


def Task4_fun():
    global file_path
    global num

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
                    out2.append(listmidpoint[j])
                    break

        data = np.column_stack((out1, out2))
        header = f"0\n0\n{n}"
        file_name = "output1.txt"
        np.savetxt(file_name, data, header=header, comments='', fmt='%s', delimiter='\t', encoding='utf-8')

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
                    out_error.append("{:.3f}".format(float(listmidpoint[j]) - s))
                    break

        data = np.column_stack((out_level, out_level_bin, out_mid, out_error))
        header = f"0\n0\n{n}"
        file_name = "output2.txt"
        np.savetxt(file_name, data, header=header, comments='', fmt='%s', delimiter='\t', encoding='utf-8')

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

