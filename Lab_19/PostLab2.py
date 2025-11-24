import numpy as np
from scipy.signal import dlti

def stability(num,den):
    system=dlti(num,den)
    zeros=system.zeros
    poles=system.poles
    print("Zeros:", zeros)
    print("Poles:", poles)

    stable=all(np.abs(p)<1 for p in poles)
    print("Stability:", "Stable" if stable else "Unstable")

num=[0.5,-0.7,-0.9,-0.6,-0.4]
den=[1]
stability(num, den)