from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

def myfunc(x):
    # an exponentially decaying sinusoid
    return 3*np.exp(-np.abs(x/10)) * np.sin(x)

def myfuncinv(x):
    return -1.0*myfunc(x)

def plotfunc(f,x0,x1):
    x=np.linspace(x0,x1,1000)  # create the x values
    y=np.zeros_like(x)  # create the f(x) values
    for i in range(1000):
        y[i]=f(x[i])
    plt.plot(x,y)  # do the plot


def myfuncconstrained(x):
    # the exponentially decaying sinusoid with penalty function
    f=myfunc(x)
    penalties = 0
    if x > 6:
        penalties += (x-6)*10**6
    if x < -1:
        penalties += (-1 - x)*10**6
    return f + penalties

def myfunc2D(vals, maxR, maxThetaDeg):
    x,y=vals
    f= y**2 - y + x**2 - 3*x
    Rsquared = x**2 + y**2
    thetaDeg=np.abs(np.arctan2(y,x)*180/np.pi)
    penalty = 0
    if Rsquared > maxR**2:
        penalty += (np.sqrt(Rsquared) - maxR) * 10e6
    if thetaDeg > maxThetaDeg:
        penalty += (thetaDeg - maxThetaDeg) * 10e6
    return f + penalty

def main():

    # 1d minimization
    guess = 0
    # unconstrained
    answer = minimize(myfunc, guess, method='Nelder-Mead')
    #print(answer)
    plotfunc(myfunc, -5, 10)
    plt.plot(answer.x, myfunc(answer.x), marker='o')
    plt.ylim(-3.0, 3.0)
    plt.show()
    print(answer.x, answer.fun)

    # 1d maximization
    guess = 0
    # unconstrained
    answer = minimize(myfuncinv, guess, method='Nelder-Mead')
    #print(answer)
    plotfunc(myfunc, -5, 10)
    plt.plot(answer.x, myfunc(answer.x), marker='o')
    plt.ylim(-3.0, 3.0)
    plt.show()
    print(answer.x, answer.fun)

    # constrained
    answer = minimize(myfuncconstrained, guess, method='Nelder-Mead')
    plotfunc(myfuncconstrained, -5, 10)
    plt.plot(answer.x, answer.fun, marker='o')
    plt.ylim(-3.0, 3.0)
    plt.show()
    print(answer.x,answer.fun)

    guess = 3
    # unconstrained
    answer = minimize(myfunc, guess, method='Nelder-Mead')
    plotfunc(myfunc, -5, 10)
    plt.plot(answer.x, answer.fun, marker='o')
    plt.ylim(-3.0, 3.0)
    plt.show()
    #print(answer)
    print(answer.x, answer.fun)

    # constrained
    answer = minimize(myfuncconstrained, guess, method='Nelder-Mead')
    plotfunc(myfuncconstrained, -5, 10)
    plt.plot(answer.x, answer.fun, marker='o')
    plt.ylim(-3.0, 3.0)
    plt.show()
    print(answer.x,answer.fun,'\n\n')

    # 2D optimization - constrained
    answer = minimize(myfunc2D, [1,1], args = (6,45), method='Nelder-Mead')
    #print('\n',answer)
    xvals=np.linspace(-2.0,2.0,20)
    yvals=np.linspace(-2.0,2.0,20)
    z=np.zeros(shape=(len(xvals),len(yvals)))
    for r in range(len(xvals)):
        for c in range(len(yvals)):
            zval=myfunc2D((xvals[r],yvals[c]),6,45)
            z[r][c]=min(zval,1)
    MGX,MGY=np.meshgrid(xvals,yvals)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(MGX, MGY, z, rstride=1, cstride=1, cmap='coolwarm', alpha=1.0, linewidth=0.2)
    ax.scatter(answer.x[1], answer.x[0], answer.fun, marker='o', color='orange')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    #ax.set_zlim(0,1.0)
    ax.contour(MGX, MGY, z, levels=50, zdir='z', offset=np.min(z), cmap='coolwarm')
    plt.show()

    print(answer.x,answer.fun)

    answer = minimize(myfunc2D, [1,1], args = (1,45), method='Nelder-Mead')
    #print('\n',answer)
    print(answer.x,answer.fun)

    answer = minimize(myfunc2D, [1, 1], args=(1, 15), method='Nelder-Mead')
    #print('\n', answer)
    print(answer.x, answer.fun)
    x=answer.x[0]
    y=answer.x[1]

    print(x,y)

    print('\n',answer)

main()