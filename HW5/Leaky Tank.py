from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np


def ode_system(x, t):
    #define any numerical parameters (constants)
    qvi=24  # input flow rate
    cdA2g=6 # cd * Area* sqrt(2g)
    A=1     # Tank cross-sectional area
    
    h=x[0]
    hdot=(1/A)*(qvi-cdA2g*np.sqrt(h))
    return [hdot]

def main():
    t = np.linspace(0, 10, 200)    #time goes from 0 to 10 seconds
    h0 = np.zeros(1)               # and array to hold the initial conditions
    h0[0]=0

    h = odeint(ode_system, h0, t)

    plt.plot(t, h, 'b-', label = 'Fluid Height')
    plt.legend(loc = 'upper right')
    plt.xlabel('Time, s')
    plt.ylabel('Fluid Height, m')
    plt.title('Filling a Leaky Tank')
    plt.show()

main()