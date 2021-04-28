import numpy as np
import matplotlib.pyplot as pyplot
from scipy import linalg


def ClampedCubicSpline(x, y, slope1, slope2):
    # the goal is to create a set of equations in the form [A][g'']=[b] where [A] is a tri-diagonal matrix, [g''] is a vector of
    # second derivatives at each x value, and [b] is a vector that is a function of x
    blen = len(x)
    A = np.zeros([blen, blen])
    b = np.zeros(blen)
    for i in range(blen):
        if i == 0:
            dX = x[i + 1] - x[i]  # deltaX for i
            A[i][i] = -dX / 3
            A[i][i + 1] = -dX / 6
            b[i] = slope1 + y[i] / dX - y[i + 1] / dX
        elif i == (blen - 1):
            dXl = x[i] - x[i - 1]  # deltaX for i-1
            A[i][i] = -dX / 3
            A[i][i - 1] = -dX / 6
            b[i] = slope2 + y[i - 1] / dXl - y[i] / dXl
        else:
            dX = x[i + 1] - x[i]  # deltaX for i
            dXl = x[i] - x[i - 1]  # deltaX for i-1
            dX2 = dX + dXl  # deltaX for i + deltaX for i-1
            mu = dXl / dX
            lam = dX2 / dX
            A[i][i - 1] = mu
            A[i][i] = 2 * lam
            A[i][i + 1] = 1
            b[i] = 6 * ((y[i + 1] - y[i]) / dX**2 + (y[i - 1] - y[i]) / (dXl * dX))
    ddg = linalg.solve(A, b)
    return ddg


def NaturalCubicSpline(x, y):
    # the goal is to create a set of equations in the form [A][g'']=[b] where [A] is a tri-diagonal matrix, [g''] is a vector of
    # second derivatives at each x value, and [b] is a vector that is a function of x
    blen = len(x)
    A = np.zeros([blen, blen])
    b = np.zeros(blen)
    for i in range(blen):
        if i == 0 or i == (blen - 1):
            A[i][i] = 1
            b[i] = 0
        else:
            dX = x[i + 1] - x[i]  # deltaX for i
            dXl = x[i] - x[i - 1]  # deltaX for i-1
            dX2 = dX + dXl  # deltaX for i + deltaX for i-1
            mu = dXl / dX
            lam = dX2 / dX
            A[i][i - 1] = mu
            A[i][i] = 2 * lam
            A[i][i + 1] = 1
            b[i] = 6 * ((y[i + 1] - y[i]) / dX**2 + (y[i - 1] - y[i]) / (dXl * dX))
    ddg = linalg.solve(A, b)
    return ddg


def interp(x, xvals, yvals, ddg):
    # given the vector of second derivatives find the value for F(x)
    nX = len(xvals)
    xi = 0
    for i in range(nX):
        if x < xvals[i]:
            i -= 1
            dXf = xvals[i + 1] - x  # width of interval to right of x
            dXb = x - xvals[i]  # width of interval to left of x
            dX = xvals[i + 1] - xvals[i]  # total with of interval
            fx = ddg[i] / 6 * ((dXf**3) / dX - dX * dXf)
            fx += ddg[i + 1] / 6 * ((dXb**3) / dX - dX * dXb)
            fx += yvals[i] * (dXf / dX) + yvals[i + 1] * (dXb / dX)
            return fx


def PlotCubicSpline(x, y, slope1, slope2, showpoints=True, npoints=500):

    # Find difference in  x and y
    dX = np.diff(x)
    dY = np.diff(y)
    dS = dY / dX  # x, y ratio
    coeffs = ClampedCubicSpline(x, y, slope1, slope2)  # Calculate the coefficients
    # coefficient arrays
    a = (3 * dS - coeffs[1:] - 2 * coeffs[: (len(x) - 1)]) / dX
    b = (coeffs[: (len(x) - 1)] + coeffs[1:] - 2 * dS) / (dX ** 2)
    xvals = np.linspace(min(x), max(x), npoints)  # Calculate x values
    yvals = []  # Calculate y values
    for i in xvals:  # Loop through x array
        for j in range(len(x) - 1):  # Loop through len x array
            if ((i >= x[j]) & (i <= x[j + 1])):  # Append y value
                yvals.append(y[j] + coeffs[j] * (i - x[j]) + a[j] * ((i - x[j]) ** 2) + b[j] * ((i - x[j]) ** 3))
    if showpoints:
        # Plot Showpoints
        pyplot.plot(x, y, linestyle='none', marker='o', markerfacecolor='white', markeredgecolor='black', markersize=10, label='Original Values')
    # Plot Cubic Spline
    pyplot.plot(xvals, yvals, linestyle='dashed', color='black', linewidth='2', label='Cubic Spline')
    pyplot.legend()
    pyplot.title('HW4 - C')  # Title
    pyplot.xlabel('X Values')  # X label
    pyplot.ylabel('Y Values')  # Y Label
    pyplot.show()


def main():
    x = np.array([1.5, 3, 4.5, 6, 7.5, 9])  # create an array for the x values of the data
    y = np.array([3.5, 1.5, -2, 6.9, 8.2, 1.5])  # create an array of the y values of the data
    slp1 = 2  # to be used for a clamped cubic spline
    slp2 = -4  # to be used for a clamped cubic spline
    # ans1=NaturalCubicSpline(x,y)
    PlotCubicSpline(x, y, slp1, slp2, showpoints=True)
    pass


main()
