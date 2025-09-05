import numpy as np
intArray=np.array([-3,-1,0,1])
floatArray=np.array([0.1,0.2,0.3])
complexArray=np.array([1+2j,2+3j,3+4j])
print(intArray.dtype)
print(floatArray.dtype)
print(complexArray.dtype)

array1=np.array([1,3,7],dtype='int8')
array2=np.array([2,4,6],dtype='uint16')
array3 = np.array([1.2, 2.3, 3.4], dtype='float32')
array4 = np.array([1+2j, 2+3j, 3+4j], dtype='complex64')
print(array1, array1.dtype)
print(array2, array2.dtype)
print(array3, array3.dtype)
print(array4, array4.dtype)


int_array = np.array([1, 3, 5, 7])
float_array=int_array.astype('float')
print(int_array, int_array.dtype)
print(float_array, float_array.dtype)