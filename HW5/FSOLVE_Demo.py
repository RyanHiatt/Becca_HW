from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy


def twoQuadratics(vals):  # vals is a list of 2 numbers  ???
    x, y = vals  # ??? why 2 numbers  ???
    #  x^2  + y^2 = r^2  a circle of radius=4
    f1val = x**2 + y**2 - 16  # x^2  + y^2 - r^2  = 0
    # y = 0.5*x^2 + 1
    f2val = 0.5 * x**2 + 1 - y  # 0.5*x^2 + 1 - y = 0
    return (f1val, f2val)


def AnothertwoQuadratics(vals, args=[4, 0.5, 1]):
    radius, width, offset = args  # radius, witdh and offset can be changed
    x, y = vals
    f1val = x**2 + y**2 - radius**2
    f2val = width * x**2 + offset - y
    return (f1val, f2val)


def fromNotes(vals):  # vals is a list of 2 numbers  ???
    x, y = vals  # ??? why 2 numbers  ???
    f1val = np.sin(x) - 3 * y
    f2val = np.exp(y) + np.cos(x)
    return (f1val, f2val)


def main():
    # #first ... demo some numpy array tools ...
    # print("Linspace  :( ",np.linspace(0,5,10))
    # print("\nLinspace  :) ",np.linspace(0,5,11))

    # x=np.array([  [1,2,3,4,5,6,7],[7,6,5,4,3,2,1]  ]  )
    # y=np.ones_like(x)
    # print("ONES")
    # print("x = ",x)
    # print("x = ", y)
    #
    # x = np.array([[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4]])
    # y = np.zeros_like(x)
    #
    # print("ZEROS")
    # print("x = ", x)
    # print("y = ", y)
    #
    # x=np.zeros(5)
    # y=np.ones(5)
    # z=73.7*np.ones((5,3))
    # print("\n\nUsing np.zeros  :",x)
    # print("\nUsing np.ones  :",y)
    # print("\nUsing np.73.7  :",z)
    #
    #
    #
    # x=np.array([  [1,2,3,4,5,6,7],[1,2,3,4]  ]  )
    # y=deepcopy(x)
    #
    # print("\nDeep Copy :) ",x,"\n     --> ",y)

    # https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.fsolve.html
    # scipy.optimize.fsolve(func, x0, args=(), fprime=None, full_output=0, col_deriv=0, xtol=1.49012e-08, ...
    (x, y) = fsolve(twoQuadratics, (1.2, 0.4))   # (1.2,0.4)  ?????
    print("\n\nFirst function, No args possible: ", x, y)
    # let's plot it
    xvals = np.linspace(0, 5, 100)
    y_fn1 = np.array([np.sqrt(-x**2 + 16) for x in xvals])
    y_fn2 = np.array([0.5 * x**2 + 1 for x in xvals])
    plt.plot(xvals, y_fn1)
    plt.plot(xvals, y_fn2)
    plt.plot(x, y, marker='o', markerfacecolor='none', markeredgecolor='red', markersize=14)
    plt.ylim(0, 4)
    plt.xlim(0, 4)
    plt.show()

    (x, y) = fsolve(AnothertwoQuadratics, (1, 1))
    print("Second function, no Args sent: ", x, y)
    # let's plot it
    radius, width, offset = [4, 0.5, 1]
    f1val = x**2 + y**2 - radius**2
    f2val = width * x**2 + offset - y
    xvals = np.linspace(0, 5, 100)
    y_fn1 = np.array([np.sqrt(-x ** 2 + radius**2) for x in xvals])
    y_fn2 = np.array([width * x ** 2 + offset for x in xvals])
    plt.plot(xvals, y_fn1)
    plt.plot(xvals, y_fn2)
    plt.plot(x, y, marker='o', markerfacecolor='none', markeredgecolor='red', markersize=14)
    plt.ylim(0, 4)
    plt.xlim(0, 4)
    plt.show()

    (x, y) = fsolve(fromNotes, (-3, 0))
    print("fromNotes: ", x, y)
    # let's plot it
    xvals = np.linspace(-3.5, -2, 100)
    y_fn1 = np.array([1 / 3 * np.sin(x) for x in xvals])
    y_fn2 = np.array([np.log(-np.cos(x)) for x in xvals])
    plt.plot(xvals, y_fn1)
    plt.plot(xvals, y_fn2)
    plt.plot(x, y, marker='o', markerfacecolor='none', markeredgecolor='red', markersize=14)
    plt.show()

    # find the other root
    (x, y) = fsolve(fromNotes, (-2, 0))
    print("fromNotes: ", x, y)
    # let's plot it
    xvals = np.linspace(-3.5, -2, 100)
    y_fn1 = np.array([1 / 3 * np.sin(x) for x in xvals])
    y_fn2 = np.array([np.log(-np.cos(x)) for x in xvals])
    plt.plot(xvals, y_fn1)
    plt.plot(xvals, y_fn2)
    plt.plot(x, y, marker='o', markerfacecolor='none', markeredgecolor='blue', markersize=14)
    plt.show()


main()
