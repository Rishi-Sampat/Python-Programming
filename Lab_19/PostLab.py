import sympy as sp

def z_transform_unit_step():
    n,z=sp.symbols('n z')
    u = 1 

    U=sp.summation(u*z**(-n),(n,0,sp.oo))
    return sp.simplify(U)

U_z=z_transform_unit_step()
print("Z-transform of unit step u[n]:")
sp.pprint(U_z)

roc = "|z| > 1"
print("\nRegion of Convergence (ROC):", roc)

if roc=="|z| > 1":
    print("Stability: Unstable (unit circle not included in ROC)")
else:
    print("Stability: Stable")