import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

audio,sample_rate=sf.read(r'E:\College\Python Programming\Lab_20\file_example_WAV_1MG.wav')
print(audio)
print(sample_rate)
time=np.arange(0,len(audio))/sample_rate
plt.plot(time, audio)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
