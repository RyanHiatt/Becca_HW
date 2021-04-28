from scipy.integrate import odeint
import matplotlib.pyplot as plt
'''
h - varying height of bucket. A,H,R,D - Area, Height, Radius, Diameter of Bucket respectively
a,r,d - area, radius, diameter of hole respectively.

Qstored = Qin - Qout.
Qstored = A * dh/dt where A = pi*R^2*H = pi*(D/2)^2*H, Qstored = pi* (D/2)^2* H* dh/dt
Qout = 0.5959* a*(rhow*g*h)^(1/2) where a = pi*r^2 = pi*(d/2)^2, Qout = 0.5959 pi(d/2)^2*(rhow*g*h)^(1/2)
Qstored = Qin - Qout gives pi (D/2)^2 *H dH/dt = Qin - (0.5959 *pi(d/2)^2*(rhow*g*h)^(1/2))
dh/dt = ( Qin - (0.5959 pi(d/2)^2*(rhow*g*h)^(1/2)) ) / (pi *(D/2)^2 * H)
'''
Qin = 20 # gpm
Qin = Qin * 0.000063 # m^3/s
d = 0.25 # in.
d = d * 0.0254 # meters
D = 1.3 # ft
D = D * 0.3048 # meters
H = 2.3 #ft
H = H * 0.3048 # meters
rhow = 1000 # kg/m^3
g = 9.81 # m/s^2
pi = 3.141592653589793
dhdt = lambda h,t: ( Qin - (0.5959 * pi * (d/2)*2*(rhow*g*h)*(1/2)) ) / (pi * (D/2) ** 2 * H)

# applying odeint to find the solution to dhdt
t = [i for i in range(401)] # tspan [0,400], any range that gives a satisfactory plot
h0 = 0 # assume initial condition h(0) = 0
h = odeint(dhdt,h0,t) # solving ode using odeint

# plot solution
plt.plot(t,h), plt.xlabel('t [s]'), plt.ylabel('h(t) [m]'), plt.grid(), plt.show()