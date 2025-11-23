import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs=500
f=5
t=np.linspace(0,1,fs,endpoint=False)
sine_wave=np.sin(2*np.pi*f*t)
square_wave=signal.square(2*np.pi*f*t)
plt.figure(figsize=(10,5))
plt.subplot(2,1,1,)
plt.plot(t,sine_wave)
plt.title('Sine Wave')
plt.xlabel('Time[s]')
plt.ylabel('Aplitude')
plt.subplot(2,1,2)
plt.plot(t,square_wave)
plt.xlabel('Time[s]')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()