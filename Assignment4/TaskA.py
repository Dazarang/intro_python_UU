import matplotlib.pyplot as plt
import numpy as np


def SIR(S0, I0, R0, a, b, T=100):

    t = np.linspace(0, T, T+1, dtype=int)
    
    S, I, R = np.zeros(T+1), np.zeros(T+1), np.zeros(T+1)
    S[0], I[0], R[0] = S0, I0, R0
    
    for i in range(1, T+1):
        S[i] = S[i-1] - a*S[i-1]*I[i-1]
        I[i] = I[i-1] + a*S[i-1]*I[i-1] - b*I[i-1]
        R[i] = R[i-1] + b*I[i-1]
        d = np.diff(R)

    plt.figure(figsize=(12,7))
    
    plt.subplot(2, 1, 1)
    plt.plot(S, "o-", color = "blue", label = "Susceptible")
    plt.plot(I, "o-", color = "darkorange", label = "Infected")
    plt.plot(R, "o-", color = "forestgreen", label = "Recovered")
    plt.legend(loc = "center left")
    plt.ylabel("Number of individuals")
    
    plt.subplot(2,1,2)
    plt.plot(d, "o-", color = "red", label = f"Death toll\nTotal death {int(round(d.cumsum()[-1]))}")
    plt.legend(loc = "upper right")
    plt.xlabel("Weeks")
    plt.ylabel("Number of individuals")
    plt.show()
    
    
    
    return S, I, R, t

SIR(995, 5, 0, 0.0005, 0.1, 40)

