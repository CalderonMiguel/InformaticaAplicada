import numpy as np
import matplotlib.pyplot as plt

# Define the analog signal
fs = 1000
t = np.linspace(0, 1, fs)
analog_signal = np.sin(2 * np.pi * 300 * t)

# Define the Nyquist rate
fs_nyquist = 2 * 300

# Sample the analog signal
digital_signal = analog_signal[::int(fs / (1.5 * fs_nyquist))]
# Plot the signals
fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t, analog_signal)
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Amplitude')
axs[1].stem(np.arange(len(digital_signal)) * t[-1] / (len(digital_signal) - 1), digital_signal)
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Amplitude')
plt.show()