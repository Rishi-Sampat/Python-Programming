import sympy as sp
n,z,alpha=sp.symbols('n z alpha')
x_n=sp.exp(alpha*n)
X_z=sp.summation(x_n*z**(-n),(n,0,sp.oo))
print("Z-transform of x[n] = exp(alpha * n) u[n]:")
sp.pprint(X_z, use_unicode=True)