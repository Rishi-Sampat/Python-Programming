import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs1,clean=wavfile.read(r"E:\College\Python Programming\Lab_18\clean_audio.wav")
fs2,noisy=wavfile.read(r"E:\College\Python Programming\Lab_18\noisy_audio.wav")
fs3,periodic=wavfile.read(r"E:\College\Python Programming\Lab_18\periodic_audio.wav")

clean=clean.astype(float)
noisy=noisy.astype(float)
periodic=periodic.astype(float)

if clean.ndim == 2:
    clean=np.mean(clean,axis=1)

if noisy.ndim == 2:
    noisy=np.mean(noisy,axis=1)

if periodic.ndim == 2:
    periodic=np.mean(periodic,axis=1)

def autocorr(x):
    return np.correlate(x,x,mode="full")

clean_auto=autocorr(clean)
noisy_auto=autocorr(noisy)
periodic_auto=autocorr(periodic)

def crosscorr(x, y):
    return np.correlate(x,y,mode="full")

cross_clean_noisy=crosscorr(clean, noisy)
cross_clean_periodic=crosscorr(clean, periodic)

plt.figure()

plt.subplot(3, 2, 1)
plt.title("Autocorrelation: Clean Audio")
plt.plot(clean_auto)
plt.subplot(3, 2, 3)
plt.title("Autocorrelation: Noisy Audio")
plt.plot(noisy_auto)
plt.subplot(3, 2, 5)
plt.title("Autocorrelation: Periodic Audio")
plt.plot(periodic_auto)
plt.subplot(3, 2, 2)
plt.title("Cross-Correlation: Clean vs Noisy")
plt.plot(cross_clean_noisy)
plt.subplot(3, 2, 4)
plt.title("Cross-Correlation: Clean vs Periodic")
plt.plot(cross_clean_periodic)
plt.tight_layout()
plt.show()