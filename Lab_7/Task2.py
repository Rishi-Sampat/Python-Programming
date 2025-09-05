import numpy as np

p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("Original matrices:")
print(p)
print(q)
res1=np.dot(p,q)
print("Matrix Multiplication:")
print(res1)

a=np.array([[1,0],[1,2]])
print("Original 2-d array")
print(a)
print("Determinant:")
print(np.linalg.det(a))