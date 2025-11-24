import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import dlti, freqz

def analyze_z_transfer_function(num,den):
    system=dlti(num,den)
    zeros=system.zeros
    poles=system.poles
    print("Zeros:", zeros)
    print("Poles:", poles)

    stable=all(np.abs(p)<1 for p in poles)
    print("Stability:", "Stable" if stable else "Unstable")

    causal=all(num[i]==0 for i in range(len(num)-1) if num[i+1]==0)
    print("Causality:","Causal" if causal else "Non-Causal")
    
    time_invariant=True
    print("Time Invariance:","Time Invariant" if time_invariant else "Time Variant")

    w, h = freqz(num,den)
    plt.figure()
    plt.subplot(2,1,1)
    plt.semilogx(w,20*np.log10(abs(h)))
    plt.title('Magnitude Plot')
    plt.xlabel('Frequency [rad/s]')
    plt.ylabel('Magnitude [dB]')
    plt.grid()

    plt.subplot(2,1,2)
    plt.semilogx(w,np.angle(h, deg=True))
    plt.title('Phase Plot')
    plt.xlabel('Frequency [rad/s]')
    plt.ylabel('Phase [degrees]')
    plt.grid()
    plt.tight_layout()
    plt.show()
# Example: Analyzing a specific system H(z) = (z^2 + 0.5)/(z^2 - 1.5z + 0.5)
num = [1, 0.5]
den = [1, -1.5, 0.5]
analyze_z_transfer_function(num, den)