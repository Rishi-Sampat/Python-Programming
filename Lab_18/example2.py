import numpy as np

x=[1,2,3,4]
h=[1,0,-1]
N=max(len(x),len(h))
x_padded=np.pad(x,(0,N - len(x)),mode='constant')
h_padded=np.pad(h,(0,N - len(h)),mode='constant')
X_fft=np.fft.fft(x_padded)
H_fft=np.fft.fft(h_padded)
circular_conv=np.fft.ifft(X_fft * H_fft)
circular_conv=np.real(circular_conv)
print("Circular Convolution: ",circular_conv)