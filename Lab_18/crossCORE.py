import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([2,3,4,5,6])
cross_corr=np.correlate(x,y,mode='full')
plt.stem(cross_corr)
plt.title('Cross-Correlation')
plt.show()