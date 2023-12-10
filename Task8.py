import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import CompareSignal
import os

def Task8_fun():

    def normalized_cross_correlation(signal1, signal2):
        numerator = np.sum(signal1 * signal2)

        denominator_signal1 = np.sqrt(np.sum(signal1**2))
        denominator_signal2 = np.sqrt(np.sum(signal2**2))

        # Compute normalized cross-correlation
        correlation_result_normalized = numerator / (denominator_signal1 * denominator_signal2)
        return correlation_result_normalized

    def import_signals_and_compute_correlation():
        # Open file dialogs to select two signal files
        file_path1 = filedialog.askopenfilename(title="Select Signal File 1", filetypes=[("Text files", "*.txt")])
        file_path2 = filedialog.askopenfilename(title="Select Signal File 2", filetypes=[("Text files", "*.txt")])

        if file_path1 and file_path2:
            try:
                # Load original signals
                signal1 = np.loadtxt(file_path1, skiprows=3, usecols=1)
                signal2_original = np.loadtxt(file_path2, skiprows=3, usecols=1)

                # Initialize an array to store correlation results
                correlation_results = []

                # Compute and store the normalized cross-correlation for the original signals
                correlation_result_original = normalized_cross_correlation(signal1, signal2_original)
                correlation_results.append(correlation_result_original)

                # Perform additional correlations for shifted signals
                for shift in range(1, 5):
                    # Compute and store the normalized cross-correlation for the shifted signal
                    correlation_result_shifted = normalized_cross_correlation(signal1, np.roll(signal2_original, shift=-shift))
                    correlation_results.append(correlation_result_shifted)

                # Save results to a file
                with open("correlation_results.txt", "w") as file:
                    for i, result in enumerate(correlation_results):
                        file.write(f'Normalized Cross-Correlation Result {i + 1}:\n{result}\n')

                # Display success message
                messagebox.showinfo("Success", "Normalized Cross-Correlation Results saved to 'correlation_results.txt'")
                indices = [0, 1, 2, 3, 4]
                CompareSignal.Compare_Signals("CorrOutput.txt", indices, correlation_results)

            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please ensure the signals have the same length.")


    def time_delay():
        # Open file dialogs to select two signal files
        file_path1 = filedialog.askopenfilename(title="Select Signal File 1", filetypes=[("Text files", "*.txt")])
        file_path2 = filedialog.askopenfilename(title="Select Signal File 2", filetypes=[("Text files", "*.txt")])

        if file_path1 and file_path2:
            try:
                # Load original signals
                signal1 = np.loadtxt(file_path1, skiprows=3, usecols=1)
                signal2_original = np.loadtxt(file_path2, skiprows=3, usecols=1)

                # Initialize an array to store correlation results
                correlation_results = []

                # Compute and store the normalized cross-correlation for the original signals
                correlation_result_original = normalized_cross_correlation(signal1, signal2_original)
                correlation_results.append(correlation_result_original)

                # Perform additional correlations for shifted signals
                for shift in range(1, 10):
                    # Compute and store the normalized cross-correlation for the shifted signal
                    correlation_result_shifted = normalized_cross_correlation(signal1, np.roll(signal2_original, shift=-shift))
                    correlation_results.append(correlation_result_shifted)

                sampling_period = int(entry_sam.get())
                max_correlation_index = np.argmax(correlation_results)
                time_delay = max_correlation_index / sampling_period
                print(time_delay)

            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please ensure the signals have the same length.")

    def browse():
        file_path = filedialog.askopenfilename(title="Select Signal File Test", filetypes=[("Text files", "*.txt")])
        test = []
        if file_path:
            test = np.loadtxt(file_path)

        return test
    def temp_match():
        # Ask the user to select a folder
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

                # Append the signal to the list
                all_signals1.append(signal)
            except Exception as e:
                print(f"Error reading {file_name}: {e}")

        average_signal1 = np.mean(all_signals1, axis=0)

        for file_name in text_files2:
            file_path = os.path.join(folder_path2, file_name)
            try:
                # Assuming the signal is in the second column (change as needed)
                signal = np.loadtxt(file_path)

                # Append the signal to the list
                all_signals2.append(signal)
            except Exception as e:
                print(f"Error reading {file_name}: {e}")


        average_signal2 = np.mean(all_signals2, axis=0)
        test = browse()

        correlation_results1 = []
        correlation_results2 = []
        # Compute and store the normalized cross-correlation for the original signals
        corr1 = normalized_cross_correlation(average_signal1, test)
        correlation_results1.append(corr1)

        corr2 = normalized_cross_correlation(average_signal2, test)
        correlation_results2.append(corr2)
        # Perform additional correlations for shifted signals
        for shift in range(1, 251):
            # Compute and store the normalized cross-correlation for the shifted signal
            correlation_result_shifted1 = normalized_cross_correlation(average_signal1, np.roll(test, shift=-shift))
            correlation_results1.append(correlation_result_shifted1)
            correlation_result_shifted2 = normalized_cross_correlation(average_signal2, np.roll(test, shift=-shift))
            correlation_results2.append(correlation_result_shifted2)

        max1 = np.max(correlation_results1)
        max2 = np.max(correlation_results2)
        if max1 > max2:
            print("This Test Belongs to Class 1 Down")
        if max1 < max2:
            print("This Test Belongs to Class 2 UP")


    # Create the main window
    window = tk.Tk()
    window.geometry("400x500")
    window.title("Normalized Cross-Correlation Calculator")

    lable_sam = tk.Label(window, text="Enter Sampling Freq :")
    lable_sam.grid(row=1, column=0, padx=10, pady=10, sticky='e')

    entry_sam = tk.Entry(window)
    entry_sam.grid(row=1, column=1, padx=10, pady=10)
    # Button to import signals and compute correlation
    import_button = tk.Button(window, text="Correlation", padx=15, pady=5, fg="black", bg="lightblue", font=("Arial", 12), command=import_signals_and_compute_correlation)
    import_button.grid(row=0, column=1, pady=10, padx=10)

    import_button = tk.Button(window, text="Time Delay", padx=15, pady=5, fg="black", bg="lightblue", font=("Arial", 12), command=time_delay)
    import_button.grid(row=2, column=1, pady=10, padx=10)

    import_button = tk.Button(window, text="Template Match", padx=15, pady=5, fg="black", bg="lightblue", font=("Arial", 12), command=temp_match)
    import_button.grid(row=3, column=1, pady=10, padx=10)


    # Button to exit the application
    exit_button = tk.Button(window, text="Exit", padx=15, pady=5, fg="black", bg="red", font=("Arial", 12), command=window.destroy)
    exit_button.grid(row=4, column=1, pady=10, padx=10)

    window.mainloop()