import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 20)
signal = np.sin(0.2 * np.pi * n)

delay = 3
delayed_signal = np.zeros_like(signal)
delayed_signal[delay:] = signal[:-delay]

advance = 3
advanced_signal = np.zeros_like(signal)
advanced_signal[:-advance] = signal[advance:]

plt.figure()
plt.subplot(3, 1, 1)
plt.stem(n, signal)
plt.title('Original Signal')
plt.xlabel('n (Discrete Time)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.stem(n, delayed_signal)
plt.title(f'Delayed Signal (by {delay} samples)')
plt.xlabel('n (Discrete Time)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.stem(n, advanced_signal)
plt.title(f'Advanced Signal (by {advance} samples)')
plt.xlabel('n (Discrete Time)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()