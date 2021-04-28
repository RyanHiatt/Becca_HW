from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def ode_system(X, t, m,c,k,fmag ):
    #define any numerical parameters (constants)
    # these params were stored in a list, and must be passed in the correct order!
    #define the forcing function equation
    f=fmag*np.sin(2*t)
    
    x=X[0]; xdot=X[1]  # copy from the state array to nicer names
    
    #write the non-trivial equation
    xddot= (1/m) * (f-c*xdot-k*x)
       
    return [xdot,xddot]

def main():
    t = np.linspace(0, 10, 200)    #time goes from 0 to 10 seconds
    ic=[1,0]

    #define the model parameters
    m=1  # the mass
    c=4  # damping (shock absorber)
    k=16 # the spring
    fmag = 5 # the magnitude of the forcing function

    x = odeint(ode_system, ic, t,args=(m,c,k,fmag))

    plt.plot(t, x[:,0], 'b-', label = 'Position')
    plt.plot(t, x[:,1], 'r-', label = 'Velocity')
    plt.legend(loc = 'lower right')
    plt.xlabel('Time, s')
    plt.ylabel('Position and Velocity')
    plt.title('Spring-Mass-Damper Dynamics - Forced Response')
    plt.show()

main()