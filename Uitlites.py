import numpy as np
import CompareSignalFIR
from tkinter import filedialog
import matplotlib.pyplot as plt
def Convolution(x , x_ind ,h ,h_ind):
    total_length = len(x) + len(h) - 1
    x_pad = np.pad(x, (0, total_length - len(x)), 'constant')
    h_pad = np.pad(h, (0, total_length - len(h)), 'constant')
    result_ind = list(range(int(min(x_ind) + min(h_ind)), int(max(x_ind) + max(h_ind) + 1)))

    signal1dft = dft(x_pad)
    signal2dft = dft(h_pad)

    fre_conv = signal1dft * signal2dft

    res_signal = idft(fre_conv)

    res_signal = res_signal.real

    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    axes[0].plot(x_ind, x)
    axes[0].set_title('X Signal')
    axes[1].plot(h_ind, h)
    axes[1].set_title('H Filter')
    axes[2].plot(result_ind, res_signal)
    axes[2].set_title('Result')
    plt.tight_layout()
    plt.show()
    return result_ind, res_signal

def Convo(x , h):
    res_signal = [0] * (len(x) + len(h) - 1)
    for i in range(len(x)):
        for j in range(len(h)):
            res_signal[i + j] += x[i] * h[j]
    return res_signal
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
def generate_window(TS , StopBandAttenuation):
    if 0 < StopBandAttenuation <= 21:
        N = 0.9 / TS
        N = np.round(N).astype(int)
        if N % 2 == 0:
            N += 1
        for i in range(N):
            window = np.ones(N)
    elif 21 < StopBandAttenuation <= 44:
        N = 3.1 / TS
        N = np.round(N).astype(int)
        if N % 2 == 0:
            N += 1
        window = np.zeros(N)
        for i in range(N):
            window[i] = 0.5 + 0.5 * np.cos((2 * np.pi * i ) / N)
    elif 44 < StopBandAttenuation <= 53:
        N = 3.3 / TS
        N = np.round(N).astype(int)
        if N % 2 == 0:
            N += 1
        window = np.zeros(N)
        for i in range(N):
            window[i] = 0.54 + 0.46 * np.cos((2 * np.pi * i ) / N)
    else:
        N = 5.5 / TS
        N = np.round(N).astype(int)
        if N % 2 == 0:
            N += 1
        window = np.zeros(N)
        for i in range(N):
            window[i] = 0.42 + 0.5 * np.cos((2 * np.pi * i) / (N - 1)) + 0.08 * np.cos((4 * np.pi * i) / (N - 1))
    return N, window

def Low_pass(FS, StopBandAttenuation, FC, TransitionBand):
    TS = TransitionBand / FS
    N, window = generate_window(TS, StopBandAttenuation)
    cutoff_freq = FC + (TransitionBand / 2)
    cutoff_freq /= FS
    st = (N // 2)
    taps = np.zeros(st + 1)
    coff1 = np.zeros(st + 1)
    for i in range(0, st + 1):
        if i == 0:
            taps[i] = 2 * cutoff_freq
        else:
            taps[i] = (np.sin(2 * np.pi * cutoff_freq * i) / (2 * np.pi * i * cutoff_freq)) * (2 * cutoff_freq)
        coff1[i] = taps[i] * window[i]
    coff2 = coff1[1:][::-1]
    coff = np.concatenate((coff2, coff1))
    indices = list(range(-st, st + 1))
    CompareSignalFIR.Compare_Signals("LPFCoefficients.txt", indices, coff)
    file_path = filedialog.askopenfilename(title="Select Signal File", filetypes=[("Text files", "*.txt")])
    if file_path:
        signal = np.loadtxt(file_path, skiprows=3)
        x_ind = signal[:, 0]
        x = signal[:, 1].astype(int)
        result_ind, res_signal = Convolution(x, x_ind, coff, indices)
        return result_ind, res_signal

def High_pass(FS, StopBandAttenuation, FC, TransitionBand):
    TS = TransitionBand / FS
    N, window = generate_window(TS, StopBandAttenuation)
    cutoff_freq = FC - (TransitionBand / 2)
    cutoff_freq /= FS
    st = (N // 2)
    taps = np.zeros(st + 1)
    coff1 = np.zeros(st + 1)
    for i in range(0, st + 1):
        if i == 0:
            taps[i] = 1 - (2 * cutoff_freq)
        else:
            taps[i] = (np.sin(2 * np.pi * cutoff_freq * i) / (2 * np.pi * i * cutoff_freq)) * (-2 * cutoff_freq)
        coff1[i] = taps[i] * window[i]

    coff2 = coff1[1:][::-1]
    coff = np.concatenate((coff2, coff1))
    indices = list(range(-st, st + 1))
    CompareSignalFIR.Compare_Signals("HPFCoefficients.txt", indices, coff)
    file_path = filedialog.askopenfilename(title="Select Signal File", filetypes=[("Text files", "*.txt")])
    if file_path:
        signal = np.loadtxt(file_path, skiprows=3)
        x_ind = signal[:, 0]
        x = signal[:, 1].astype(int)
        result_ind, res_signal = Convolution(x , x_ind ,coff , indices)
        return result_ind, res_signal

def Band_pass(FS, StopBandAttenuation, F1, F2, TransitionBand):
    TS = TransitionBand / FS
    N, window = generate_window(TS, StopBandAttenuation)
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
            taps[i] = (np.sin(2 * np.pi * cutoff_freq2 * i) / (np.pi * i)) - (np.sin(2 * np.pi * cutoff_freq1 * i) / (np.pi * i))
        coff1[i] = taps[i] * window[i]

    coff2 = coff1[1:][::-1]
    coff = np.concatenate((coff2, coff1))
    indices = list(range(-st, st + 1))
    CompareSignalFIR.Compare_Signals("BPFCoefficients.txt", indices, coff)

    file_path = filedialog.askopenfilename(title="Select Signal File", filetypes=[("Text files", "*.txt")])
    if file_path:
        signal = np.loadtxt(file_path, skiprows=3)
        x_ind = signal[:, 0]
        x = signal[:, 1].astype(int)
        result_ind, res_signal = Convolution(x, x_ind, coff, indices)
        return result_ind, res_signal

def Band_pass2(FS, StopBandAttenuation, F1, F2, TransitionBand):
    TS = TransitionBand / FS
    N, window = generate_window(TS, StopBandAttenuation)
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
            taps[i] = (np.sin(2 * np.pi * cutoff_freq2 * i) / (np.pi * i)) - (np.sin(2 * np.pi * cutoff_freq1 * i) / (np.pi * i))
        coff1[i] = taps[i] * window[i]

    coff2 = coff1[1:][::-1]
    coff = np.concatenate((coff2, coff1))
    indices = list(range(-st, st + 1))
    CompareSignalFIR.Compare_Signals("BPFCoefficients.txt", indices, coff)

    file_path = filedialog.askopenfilename(title="Select Signal File", filetypes=[("Text files", "*.txt")])
    if file_path:
        signal = np.loadtxt(file_path, skiprows=3)
        x = signal[:, 0]
        result_ind, res_signal = Convo(x, coff)
        return res_signal
def Band_stop(FS, StopBandAttenuation, F1, F2, TransitionBand):
    TS = TransitionBand / FS
    N, window = generate_window(TS, StopBandAttenuation)
    cutoff_freq1 = F1 + (TransitionBand / 2)
    cutoff_freq2 = F2 - (TransitionBand / 2)
    cutoff_freq1 /= FS
    cutoff_freq2 /= FS
    st = N // 2
    taps = np.zeros(st + 1)
    coff1 = np.zeros(st + 1)

    for i in range(st + 1):
        if i == 0:
            taps[i] = 1 - 2 * (cutoff_freq2 - cutoff_freq1)
        else:
            taps[i] = -(np.sin(2 * np.pi * cutoff_freq2 * i) / (np.pi * i)) + (
                        np.sin(2 * np.pi * cutoff_freq1 * i) / (np.pi * i))
        coff1[i] = taps[i] * window[i]

    coff2 = coff1[1:][::-1]
    coff = np.concatenate((coff2, coff1))
    indices = list(range(-st, st + 1))
    CompareSignalFIR.Compare_Signals("BSFCoefficients.txt", indices, coff)
    file_path = filedialog.askopenfilename(title="Select Signal File", filetypes=[("Text files", "*.txt")])
    if file_path:
        signal = np.loadtxt(file_path, skiprows=3)
        x_ind = signal[:, 0]
        x = signal[:, 1].astype(int)
        result_ind, res_signal = Convolution(x, x_ind, coff, indices)
        return result_ind, res_signal

def CALC_DC (signal):
    N = len(signal)
    Sum = 0.0
    Avarge = 0.0
    result = []
    for i in range(N):
        Sum += signal[i]
        Avarge = Sum / N
    for z in range(N):
        result.append(signal[z] - Avarge)
    return result

def Fast_Correlation(signal1,signal2):
    if len(signal1) != len(signal1):
        total_length = len(signal1) + len(signal2) - 1
        signal1 = np.pad(signal1, (0, total_length - len(signal1)), 'constant')
        signal2 = np.pad(signal2, (0, total_length - len(signal2)), 'constant')
    signal1dft = dft(signal1)
    signal2dft = dft(signal2)
    fre_corr = np.conjugate(signal1dft) * signal2dft
    res_signal = idft(fre_corr)
    res_signal = np.round(res_signal.real)
    fig, axes = plt.subplots(3, 1, figsize=(10, 9))
    axes[0].plot(signal1)
    axes[0].set_title('Signal 1')
    axes[1].plot(signal2)
    axes[1].set_title('Signal 2')
    axes[2].plot(res_signal)
    axes[2].set_title('Result')
    plt.tight_layout()
    plt.show()
    return res_signal

def cross_correlation(signal1, signal2):
    return np.sum(signal1 * signal2)

def Correlation(signal1,signal2):
    correlation_results = []
    correlation_result_original = cross_correlation(signal1, signal2)
    correlation_results.append(correlation_result_original)
    for shift in range(1, len(signal1)):
        correlation_result_shifted = cross_correlation(signal1, np.roll(signal2, shift=-shift))
        correlation_results.append(correlation_result_shifted)
    fig, axes = plt.subplots(3, 1, figsize=(3, 4))
    axes[0].plot(signal1)
    axes[0].set_title('Signal 1')
    axes[1].plot(signal2)
    axes[1].set_title('Signal 2')
    axes[2].plot(correlation_results)
    axes[2].set_title('Result')
    plt.tight_layout()
    plt.show()
    return correlation_results
def CALC_DCT(signal):
    N = len(signal)
    result = []
    for K in range(N):
        Sum = 0.0
        for n in range(N):
            ang =float((np.pi / (4 * N)) * (2*n - 1) * (2*K - 1))
            Sum +=float(signal[n]) * np.cos(ang)
        r = np.sqrt(2 / N) * Sum
        result.append(float(r))
    return result
def temp_match(A ,B):
    A = np.mean(A)
    B = np.mean(B)
    file_path = filedialog.askopenfilename(title="Select Signal File Test", filetypes=[("Text files", "*.txt")])
    test = []
    if file_path:
        test = np.loadtxt(file_path)

    correlation_results1 = []
    correlation_results2 = []
    # Compute and store the normalized cross-correlation for the original signals
    corr1 = cross_correlation(A, test)
    correlation_results1.append(corr1)

    corr2 = cross_correlation(B, test)
    correlation_results2.append(corr2)
    # Perform additional correlations for shifted signals
    for shift in range(1, len(A)):
        # Compute and store the normalized cross-correlation for the shifted signal
        correlation_result_shifted1 = cross_correlation(A, np.roll(test, shift=-shift))
        correlation_results1.append(correlation_result_shifted1)
        correlation_result_shifted2 = cross_correlation(B, np.roll(test, shift=-shift))
        correlation_results2.append(correlation_result_shifted2)

    max1 = np.max(correlation_results1)
    max2 = np.max(correlation_results2)
    if max1 > max2:
        print("This Test Belongs to Class A")
    if max1 < max2:
        print("This Test Belongs to Class B")