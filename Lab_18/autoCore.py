import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
auto_corr=np.correlate(x,x,mode='full')
plt.stem(auto_corr)
plt.title('Autocorrelation')
plt.show()