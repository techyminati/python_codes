import numpy as np
import matplotlib.pyplot as plt

def generate_signal(frequencies, amplitudes, duration, sample_rate):
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
    signal = sum(amplitude * np.sin(2 * np.pi * frequency * t) for frequency, amplitude in zip(frequencies, amplitudes))
    return signal

def apply_filter(signal, filter_kernel):
    signal_length = len(signal)
    kernel_length = len(filter_kernel)
    filtered_signal = np.zeros_like(signal)

    for i in range(signal_length):
        for j in range(kernel_length):
            if i - j >= 0:
                filtered_signal[i] += signal[i - j] * filter_kernel[j]

    return filtered_signal



def add_noise(signal, noise_level):
    noise = np.random.normal(0, noise_level, len(signal))
    noisy_signal = signal + noise
    return noisy_signal

def remove_random_samples(signal, percentage):
    num_samples_to_remove = int(len(signal) * percentage)
    indices_to_remove = np.random.choice(len(signal), num_samples_to_remove, replace=False)
    signal_with_samples_removed = signal.copy()
    signal_with_samples_removed[indices_to_remove] = np.nan
    return signal_with_samples_removed


frequencies = [1.0, 2.0, 3.0, 4.0, 5.0]
amplitudes = [1.0, 0.8, 0.6, 0.4, 0.2] 
duration = 5.0 
sample_rate = 500 
noise_level = 0.1 
missing_samples_fraction = 0.10  
window_size = 20 
sigma = 2  


original_signal = generate_signal(frequencies, amplitudes, duration, sample_rate)


noisy_signal = add_noise(original_signal, noise_level)

kernel=[1/window_size]*window_size
filter_kernel = np.array(kernel)
filtered_data=apply_filter(noisy_signal,filter_kernel)


signal_with_missing_samples = remove_random_samples(filtered_data, missing_samples_fraction)
plt.figure(figsize=(12, 6))
plt.subplot(311)
plt.plot(original_signal)
plt.title("Original Signal")

plt.subplot(312)
plt.plot(noisy_signal)
plt.title("Noisy Signal")

plt.subplot(313)
plt.plot(filtered_data)
plt.title("Filtered Signal")

plt.show()

def fill_missing_samples_mean(signal, window_size):
    filled_signal = signal.copy()
    for i in range(len(signal)):
        if np.isnan(signal[i]):
            start = max(0, i - window_size)
            end = min(len(signal), i + window_size + 1)
            filled_signal[i] = np.nanmean(signal[start:end])
    return filled_signal

def fill_missing_samples_weighted_mean(signal, window_size, sigma):
    filled_signal = signal.copy()
    for i in range(len(signal)):
        if np.isnan(signal[i]):
            start = max(0, i - window_size)
            end = min(len(signal), i + window_size + 1)
            weights = np.exp(-((np.arange(start, end) - i) ** 2) / (2 * sigma**2))
            filled_signal[i] = np.nansum(signal[start:end] * weights) / np.nansum(weights)
    return filled_signal

def fill_missing_samples_line_fit(signal):
    filled_signal = signal.copy()
    nan_indices = np.isnan(signal) 
    valid_indices = ~nan_indices 

    for i in range(len(signal)):
        if nan_indices[i]: 
            left_index, right_index = i - 1, i + 1
            while left_index >= 0 and not valid_indices[left_index]:
                left_index -= 1
            while right_index < len(signal) and not valid_indices[right_index]:
                right_index += 1

            if left_index >= 0 and right_index < len(signal):
                y_left, y_right = signal[left_index], signal[right_index]
                slope = (y_right - y_left) / (right_index - left_index)
                intercept = y_left - slope * left_index
                filled_signal[i] = slope * i + intercept

    return filled_signal

filled_signal_mean = fill_missing_samples_mean(signal_with_missing_samples, window_size)
filled_signal_weighted_mean = fill_missing_samples_weighted_mean(signal_with_missing_samples, window_size, sigma)
filled_signal_line_fit = fill_missing_samples_line_fit(signal_with_missing_samples)


plt.figure(figsize=(12, 10))

plt.subplot(511)
plt.plot(original_signal)
plt.title("Original Signal")

plt.subplot(512)
plt.plot(noisy_signal)
plt.title("Noisy Signal")

plt.subplot(513)
plt.plot(signal_with_missing_samples)
plt.title("Signal with Missing Samples")

plt.subplot(514)
plt.plot(filled_signal_mean)
plt.title("Filled with Mean")

plt.subplot(515)
plt.plot(filled_signal_weighted_mean, label="Weighted Mean (Gaussian Window)")
plt.plot(filled_signal_line_fit, label="Line Fit")
plt.legend()
plt.title("Filled with Weighted Mean and Line Fit")

plt.tight_layout()
plt.show()
