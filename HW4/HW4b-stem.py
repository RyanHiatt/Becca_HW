import numpy as np
import matplotlib.pyplot as pyplot
from scipy import linalg
from math import *


def RSquared(x, y, a):
    '''
    To calculate the R**2 value for a set of x,y data and a LeastSquares fit with polynomial having coefficients a
    :param x:
    :param y:
    :param a:
    :return:
    '''
    AvgY = np.mean(y)  # calculates the average value of y
    SSTot = 0
    SSRes = 0
    for i in range(len(y)):
        SSTot += (y[i] - AvgY)**2
        SSRes += (y[i] - Poly(x[i], a))**2
    RSq = 1 - SSRes / SSTot
    return RSq


def Poly(x, a):
    '''
    calculates the value for a polynomial given a value for x and the coefficients of the polynomial.
    f(x)=y=a[0]+a[1]x+a[2]x**2+a[3]x**3+...
    :param x: the x value for calculating the function
    :param a: the coefficients of the polynomial
    :return:
    '''
    y = 0
    for i in range(len(a)):
        y += a[i] * x**i
    return y


def LeastSquares(x, y, power):
    '''
    Calculates the coefficients for a polynomial of degree power to best
    fit a data set (x,y) using the least squares approach.
    :param x: the independent variable of the data set
    :param y: the value of the function evaluated at each value of x
    :param power: the degree of the polynomial
    :return: the array of coefficients (i.e., f(x)=a[0]+a[1]x+a[2]x**2+...)
    '''
    return np.polyfit(x, y, power)


def PlotLeastSquares(x, y, power, showpoints=True, npoints=500):
    Xmin = min(x)
    Xmax = max(x)
    Ymin = min(y)
    Ymax = max(y)
    dX = 1.0 * (Xmax - Xmin) / npoints
    a = LeastSquares(x, y, power)  # calculate the coefficients of the fitting polynomial
    xvals = np.linspace(Xmin, Xmax, len(x))  # &MISSING CODE HERE&#) #build the numpy array of xvals
    yvals = np.polyval(a, xvals)

    RSq = RSquared(x, y, a)  # calculate an R^2 value
    pyplot.plot(xvals, yvals, linestyle='dashed', color='black', linewidth='2')
    pyplot.title(r'$R^2={:0.3f}$'.format(RSq))
    pyplot.xlim(floor(Xmin * 10) / 10, ceil(Xmax * 10) / 10)
    pyplot.ylim(floor(Ymin), ceil(Ymax * 10) / 10)
    if showpoints:
        pyplot.plot(x, y, linestyle='none', marker='o', markerfacecolor='white', markeredgecolor='black', markersize=10)
    pyplot.xlabel('X values')
    pyplot.ylabel('Y values')
    pyplot.show()
    return xvals, yvals


def main():
    x = np.array([0.05, 0.11, 0.15, 0.31, 0.46, 0.52, 0.70, 0.74, 0.82, 0.98, 1.17])
    y = np.array([0.956, 1.09, 1.332, 0.717, 0.771, 0.539, 0.378, 0.370, 0.306, 0.242, 0.104])

    # 1. Call LeastSquares for a linear fit
    ans1 = LeastSquares(x, y, 1)
    print(ans1)

    # 2. Call PlotLeastSquares for a linear fit
    linx, liny = PlotLeastSquares(x, y, 1, showpoints=True, npoints=500)
    RSqLin = RSquared(x, y, ans1)  # calculate RSqured for linear fit

    # 3. Call LeastSquares for a Cubic fit
    ans2 = LeastSquares(x, y, 3)
    RSqCub = RSquared(x, y, ans2)  # calculate RSquared for cubic fit
    print(ans2)

    # 4. Call PlotLeastSquares for a Cubic fit
    cubx, cuby = PlotLeastSquares(x, y, 3, showpoints=True, npoints=500)

    # 5. Use results form 1 and 3 to plot the data points, the Linear fit and the Cubic fit all on one graph
    pyplot.plot(linx, liny, linewidth=2, linestyle='dashed', color='black', label=r'Linear fit ($R^2={:0.3f}$)'.format(RSqLin)) #for the linear fit
    pyplot.plot(cubx, cuby, linewidth=2, linestyle='dotted', color='black', label='Cubic fit ($R^2={:0.3f}$)'.format(RSqCub)) #for the cubic fit
    pyplot.plot(x, y, linestyle='none', marker='o', markersize=10, markerfacecolor='white', markeredgecolor='black', label='Data')  # the data points
    pyplot.xlabel('X values')
    pyplot.ylabel('Y values')
    pyplot.legend()

    pyplot.grid(axis='both')
    pyplot.tick_params(axis='both', direction='in', grid_linewidth=1, grid_linestyle='dashed', grid_alpha=0.5)
    pyplot.show()
    x=np.array([[10, 20, 30], [40, 50, 60]])
    y=np.array([[100], [200]])
    print(np.append(x, y, axis=1))
    # Use proper titles, labels and legends


main()
