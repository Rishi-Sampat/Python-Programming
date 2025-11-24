import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Use raw strings for Windows paths
audio_fs, audio = wavfile.read(r"E:\College\Python Programming\Lab_18\audio.wav")
ir_fs, ir = wavfile.read(r"E:\College\Python Programming\Lab_18\impulse.wav")

if audio.ndim == 2:
    audio = np.mean(audio, axis=1)

if ir.ndim == 2:
    ir = np.mean(ir, axis=1)

audio = audio.astype(float)
ir = ir.astype(float)

if audio_fs != ir_fs:
    raise ValueError("Sampling rates of audio & IR must match!")

# Linear convolution
linear_conv = np.convolve(audio, ir, mode="full")

# Circular convolution via FFT
N = len(audio)
M = len(ir)
L = max(N, M)

audio_pad = np.pad(audio, (0, L - N), mode="constant")
ir_pad = np.pad(ir, (0, L - M), mode="constant")

audio_fft = np.fft.fft(audio_pad)
ir_fft = np.fft.fft(ir_pad)

circular_conv = np.fft.ifft(audio_fft * ir_fft)
circular_conv = np.real(circular_conv)

plt.figure()
plt.subplot(3, 1, 1)
plt.title("Original Audio Signal")
plt.plot(audio)

plt.subplot(3, 1, 2)
plt.title("Linear Convolution Output")
plt.plot(linear_conv)

plt.subplot(3, 1, 3)
plt.title("Circular Convolution Output")
plt.plot(circular_conv)

plt.tight_layout()
plt.show()
