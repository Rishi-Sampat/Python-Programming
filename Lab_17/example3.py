import sympy as sp
n,z=sp.symbols('n z')
u_n=1
U_z=sp.summation(u_n * z**(-n),(n,0,sp.oo))
print("Z-transform of the unit step signal u[n]:")
sp.pprint(U_z, use_unicode=True)