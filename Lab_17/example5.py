import sympy as sp
n,z=sp.symbols('n z')
x_n=[1, 2, 3]
X_z=sum(x_n[i]*z**(-i)for i in range(len(x_n)))
print("Z-transform of the finite sequence {1, 2, 3}:")
sp.pprint(X_z, use_unicode=True)