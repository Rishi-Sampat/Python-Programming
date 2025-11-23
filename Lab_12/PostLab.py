import numpy as np
import matplotlib.pyplot as plt

#a
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

x1 = np.sin(2*np.pi*5*t)
x2 = np.sin(2*np.pi*10*t)
sum=x1+x2

plt.figure()
plt.plot(t,sum)
plt.title("Sum of 5 Hz and 10 Hz Sine Waves")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

#b
fs = 500
t = np.linspace(0, 2, 2*fs, endpoint=False)

x1 = np.sin(2*np.pi*5*t)
x2 = np.cos(2*np.pi*10*t)
mul=x1*x2

plt.figure()
plt.plot(t,mul)
plt.title("Multiplication: 5 Hz Sine × 10 Hz Cosine")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

#c
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
x = np.sin(2*np.pi*5*t)
timeShift = 0.1
#Convert the time shift into number of samples.
#Shifting should be in samples because array indices work in discrete steps,
#multiply the shift time by the sampling frequency to get
#how many samples the signal needs to be shifted.
shift_samples = int(timeShift * fs)
#length of x
x_shift= np.zeros_like(x)
x_shift[shift_samples:] = x[:-shift_samples]

plt.figure()
plt.plot(t, x, label="Original")
plt.plot(t, x_shift, label="Shifted (0.1s)")
plt.title("Time Shift of 5 Hz Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()

#d
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

x = np.sin(2*np.pi*10*t)
scale= 3 * x
plt.figure()
plt.plot(t, x, label="Original")
plt.plot(t, scale, label="Scaled ×3")
plt.title("Amplitude Scaling of 10 Hz Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()

#e
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

x = np.sin(2*np.pi*5*t)
x_rev = x[::-1]

plt.figure()
plt.plot(t, x, label="Original")
plt.plot(t, x_rev, label="Reversed")
plt.title("Time Reversal of 5 Hz Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()