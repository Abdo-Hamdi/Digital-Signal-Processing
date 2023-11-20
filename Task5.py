import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog


import signalcompare
sampling_frequency = None
file_path = None

def Task5_fun():

    def dft(signal):
        N = len(signal)
        dft_result = np.zeros(N, dtype=np.complex128)

        for k in range(N):
            for n in range(N):
                angle = 2 * np.pi * k * n / N
                dft_result[k] += signal[n] * np.exp(-1j * angle)

        return dft_result

    def idft(signal):
        N = len(signal)
        idft_result = np.zeros(N, dtype=np.complex128)

        for n in range(N):
            for k in range(N):
                angle = 2 * np.pi * k * n / N
                idft_result[n] += signal[k] * np.exp(1j * angle)

        return idft_result / N


    def process_signal(sampling_frequency):
        global amplitude
        global phase
        if sampling_frequency is None:
            return  # User canceled input

        file_path = filedialog.askopenfilename(title="Select a signal file")
        if file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()[3:]
                signal = np.array([float(line.split()[1]) for line in lines])

            N = len(signal)
            freq = np.fft.fftfreq(N, 1 / sampling_frequency)  # Adjust for the sampling frequency

            # Compute the DFT of the signal
            signal_dft = dft(signal)

            # Calculate amplitude and phase
            amplitude = np.abs(signal_dft).astype(float)
            amplitude = np.round(amplitude, 12)
            phase = np.angle(signal_dft).astype(float)

            # Create a single figure with two subplots
            fig, axes = plt.subplots(2, 2, figsize=(12, 6))

            # Plot the signal and its Fourier transform (Frequency vs. Amplitude)
            axes[0, 0].plot(np.arange(N) / sampling_frequency, signal)  # Adjust x-axis for time in seconds
            axes[0, 0].set_title('Original Signal')

            # Create custom x-values starting from zero for bar plots
            x_values = np.arange(len(freq)) * (sampling_frequency / N)

            # Adjust the width to make the bars smaller
            bar_width = 0.1  # You can change this value as needed

            # Plot the Fourier Transform (Frequency vs. Amplitude) with smaller bars
            axes[1, 0].bar(x_values, amplitude, width=bar_width, align='center')
            axes[1, 0].set_title('Fourier Transform (Frequency vs. Amplitude)')
            axes[1, 0].set_xlabel('Frequency (Hz)')
            axes[1, 0].set_ylabel('Amplitude')

            # Plot the frequency versus phase relations with smaller bars
            axes[0, 1].bar(x_values, phase, width=bar_width, align='center')
            axes[0, 1].set_title('Fourier Transform (Frequency vs. Phase)')
            axes[0, 1].set_xlabel('Frequency (Hz)')
            axes[0, 1].set_ylabel('Phase (radians)')

            # Remove the unused subplot
            fig.delaxes(axes[1, 1])
            plt.tight_layout()

            # Save the Fourier transform data to text files
            data = np.column_stack((amplitude, phase))
            header = f"0\n1\n{N}"
            file_name = "DFT.txt"
            np.savetxt(file_name, data, header=header, comments='', fmt='%s', delimiter='\t', encoding='utf-8')
            plt.show()


    def get_sampling_frequency():
        sampling_frequency = simpledialog.askfloat("Sampling Frequency", "Enter the sampling frequency in Hz:")
        return sampling_frequency

    def modify_amplitude_phase(sampling_frequency):
        # Ask the user for amplitude and phase input
        amplitude = simpledialog.askfloat("Amplitude", "Enter the amplitude:")
        phase = simpledialog.askfloat("Phase", "Enter the phase (radians):")

        if sampling_frequency is None:
            return  # User canceled input

        file_path = filedialog.askopenfilename(title="Select a signal file")
        if file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()[3:]
                signal = np.array([float(line.split()[1]) for line in lines])

            N = len(signal)

            if amplitude is None or phase is None:
                return  # User canceled input

            freq = np.fft.fftfreq(N, 1 / sampling_frequency)  # Adjust for the sampling frequency

            # Modify the signal components
            modified_signal = amplitude * np.sin(2 * np.pi * phase + signal)

            # Compute the DFT of the modified signal using your custom dft function
            signal_dft = dft(modified_signal)

            # Calculate amplitude and phase
            amplitude = np.abs(signal_dft).astype(float)
            phase = np.angle(signal_dft).astype(float)

            # Create a single figure with two subplots
            fig, axes = plt.subplots(2, 2, figsize=(12, 6))

            # Plot the signal and its Fourier transform (Frequency vs. Amplitude)
            axes[0, 0].plot(np.arange(N) / sampling_frequency, signal)  # Adjust x-axis for time in seconds
            axes[0, 0].set_title('Modified Signal')

            # Create custom x-values starting from zero for bar plots
            x_values = np.arange(len(freq)) * (sampling_frequency / N)

            # Adjust the width to make the bars smaller
            bar_width = 0.1  # You can change this value as needed

            # Plot the Fourier Transform (Frequency vs. Amplitude) with smaller bars
            axes[1, 0].bar(x_values, amplitude, width=bar_width, align='center')
            axes[1, 0].set_title('Fourier Transform (Frequency vs. Amplitude)')
            axes[1, 0].set_xlabel('Frequency (Hz)')
            axes[1, 0].set_ylabel('Amplitude')

            # Plot the frequency versus phase relations with smaller bars
            axes[0, 1].bar(x_values, phase, width=bar_width, align='center')
            axes[0, 1].set_title('Fourier Transform (Frequency vs. Phase)')
            axes[0, 1].set_xlabel('Frequency (Hz)')
            axes[0, 1].set_ylabel('Phase (radians)')

            # Remove the unused subplot
            fig.delaxes(axes[1, 1])

            plt.tight_layout()
            plt.show()


    def reconstruct_signal_idft(sampling_frequency):
        global amplitude
        global phase
        if sampling_frequency is None:
            return  # User canceled input

        file_path = filedialog.askopenfilename(title="Select a signal file")
        if file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()[3:]
                data = []
                amplitude_idft = []
                phase_idft = []
                # Split each row into amplitude and phase
                for row in lines:
                    try:
                        # Remove non-numeric characters ('f' in this case) from amplitude and phase
                        amp, ph = map(float,
                                      [''.join(char for char in val if char.isdigit() or char == '.' or char == '-')
                                       for val in row.split(',')])
                        amp = np.round(amp, 12)
                        amplitude_idft.append(float(amp))
                        phase_idft.append(float(ph))
                        data.append((amp, ph))
                    except ValueError:
                        print(f"Skipping row: {row.strip()} - Unable to convert to float")
                # Calculate the length of each row
            N = len(data)

            if not data:
                return  # No valid data found

            # Generate the complex DFT components from amplitude and phase
            signal_dft = np.array([amp * np.exp(1j * ph) for amp, ph in data])
            # Perform IDFT to reconstruct the signal
            reconstructed_signal = idft(signal_dft)
            # Adjust the time axis (x-axis) using the provided sampling frequency
            time_axis = np.arange(N) / sampling_frequency

            # Plot the reconstructed signal
            plt.figure()
            plt.plot(time_axis, reconstructed_signal.real)
            plt.title('Reconstructed Signal')
            plt.xlabel('Time (s)')
            plt.ylabel('Amplitude')
            plt.show()

        if (signalcompare.SignalComapreAmplitude(amplitude, amplitude_idft)):
            print("amp Done")
        if (signalcompare.SignalComaprePhaseShift(phase, phase_idft)):
            print("ph Done")


    # Create a simple GUI window
    root = tk.Tk()
    root.title("Signal Processing")

    # Set the window size (width x height)
    root.geometry("400x250")  # Adjust the size as needed

    # Add a label and an entry field for the user to enter sampling_frequency
    sampling_frequency_label = tk.Label(root, text="Enter Sampling Frequency (Hz):")
    sampling_frequency_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

    sampling_frequency_entry = tk.Entry(root)
    sampling_frequency_entry.grid(row=0, column=1, padx=10, pady=10)

    # Create a button to trigger the signal processing
    process_button = tk.Button(root, text="Process Signal", command=lambda: process_signal(float(sampling_frequency_entry.get())))
    process_button.grid(row=1, column=0, padx=10, pady=10)

    # Add a button to modify the amplitude and phase
    modify_button = tk.Button(root, text="Modify Amplitude and Phase", command=lambda: modify_amplitude_phase(float(sampling_frequency_entry.get())))
    modify_button.grid(row=1, column=1, padx=10, pady=10)

    # Create a button for signal reconstruction
    reconstruct_button = tk.Button(root, text="Reconstruct Signal", command=lambda: reconstruct_signal_idft(float(sampling_frequency_entry.get())))
    reconstruct_button.grid(row=2, column=0, padx=10, pady=10)


    # Create an exit button to close the window
    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.grid(row=2, column=1, padx=10, pady=10)

    root.mainloop()