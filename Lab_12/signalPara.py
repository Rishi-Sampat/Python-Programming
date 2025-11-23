import numpy as np
import matplotlib.pyplot as plt

fs=20
t_continuous=np.linspace(0,1,1000)
t_discrete=np.arange(0,1,1/fs)

f=5
continuous=np.sin(2*np.pi*f*t_continuous)
discrete=np.sin(2*np.pi*f*t_discrete)

#quantisation
level=4
dis_amp_signal=np.round(continuous*(level/2))/(level/2)
dis_time_ampl_signal=np.round(discrete*(level/2))/(level/2)

plt.figure()
plt.subplot(3, 1, 1)
plt.plot(t_continuous, continuous)
plt.title('Continuous-Time Signal (Sine Wave)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.stem(t_discrete, discrete)
plt.title('Discrete-Time Signal (Sampled Sine Wave)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t_continuous, dis_amp_signal, drawstyle='steps-pre')
plt.title('Discrete-Amplitude Signal (Quantized Sine Wave)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()