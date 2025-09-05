import numpy as np
arr1=np.array([10,20,30])
print("My 1D array:\n",arr1)

arr2 = np.array([[10,20,30],[40,50,60]])
print("My 2D numpy array:\n", arr2)
print("Type:", type(arr2))

arr= np.arange(0, 20, 3)
print ("A sequential array with steps of 3:\n", arr)

arr= np.linspace(0, 3, 5)
print ("A sequential array with 5 values between 0 and 5:\n", arr)

arr = np.ones((2,3))
print("numpy array:\n", arr)
print("Type:", type(arr))