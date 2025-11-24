import numpy as np
x=[1,2,3,4]
h=[1,0,-1]
linear_conv=np.convolve(x,h)
print("Linear Convolution: ",linear_conv) 