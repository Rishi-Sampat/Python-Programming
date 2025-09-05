import numpy as np

ar=np.array([[2,4,6],[1,3,5],])
print(ar.ndim)
print(ar.size)
print(ar.shape)
print(ar.dtype)

a1=np.array([6,7,8,10,13])
a2=np.array([6,7,8,10,13],dtype=np.int32)
print(a1.itemsize)
print(a2.itemsize)

array1 = np.array([6, 7, 8])
array2 = np.array([[1, 2, 3],[6, 7, 8]])
print("\nData of array1 is: ",array1.data)
print("Data of array2 is: ",array2.data)