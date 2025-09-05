#Create a 3x3 matrix with values ranging from 2 to 10
import numpy as np
a=np.arange(2,11).reshape(3,3)
print("3x3 matrix\n",a)

#b.reverse an array
arr=np.array([1,2,3,4,5])
print("Reversed array:",arr[::-1])

#c.Find common values between two arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])
print("Common values:",np.intersect1d(arr1,arr2))

#d. Repeat array elements
arr=np.array([1,2,3])
print("Repeated:",np.repeat(arr,2))

#e.Find the memory size of a NumPy array
arr=np.array([1,2,3,4,5])
print("Memory size(bytes):",arr.nbytes)

#f. Create an array of ones and zeros
print("Arrays of ones:\n",np.ones((2,3)))
print("Arrays of zeros:\n",np.zeros((2,3)))

#g. Find the 4th element of a specified array
arr = np.array([10, 20, 30, 40, 50])
print("4th element:", arr[3])
