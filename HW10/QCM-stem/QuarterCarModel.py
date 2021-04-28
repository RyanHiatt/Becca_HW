from scipy.integrate import odeint
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np
import math
from PyQt5 import QtWidgets as qtw
import statistics


class CarModel():
    """
    I re-wrote the quarter car model as an object oriented program
    and used the MVC pattern.  This is the quarter car model.  It just
    stores information about the car and results of the ode calculation.
    """

    def __init__(self):
        """
        self.results to hold results of odeint solution
        self.t time vector for odeint and for plotting
        self.tramp is time required to climb the ramp
        self.angrad is the ramp angle in radians
        self.ymag is the ramp height in m
        """
        self.results = []
        self.tmax = 3.0  # limit of timespan for simulation in seconds
        self.t = np.linspace(0, self.tmax, 200)
        self.tramp = 1.0  # time to traverse the ramp in seconds
        self.angrad = 0.1
        self.ymag = 6.0 / (12 * 3.3)  # ramp height in meters.  default is 0.1515 m
        self.yangdeg = 45.0  # ramp angle in degrees.  default is 45
        self.results = None
        self.m1 = 450  # mass of car body in kg
        self.m2 = 20  # mass of wheel in kg
        self.c1 = 4500.00  # damping coefficient in N*s/m
        self.k1 = 15000  # spring constant of suspension in N/m
        self.k2 = 90000  # spring constant of tire in N/m
        self.v = 120.0  # velocity of car in kph
        # the min and max spring constants based on static compression limits
        self.mink1 = self.m1 / 0.0762  # k1 min spring constant of suspension in N/m
        self.maxk1 = self.m1 / 0.1524  # k1 max spring constant of suspension in N/m
        self.mink2 = self.m2 / 0.01905  # k2 min spring constant of suspension in N/m
        self.maxk2 = self.m1 / 0.0381  # k2 max spring constant of suspension in N/m


class CarController():
    def __init__(self, ax=None):
        """
        This is the controller I am using for the quarter car model.
        """
        self.model = CarModel()
        self.view = CarView()
        self.view.ax = ax  # axes for the plotting using view

    def ode_system(self, X, t):
        # define the forcing function equation for the linear ramp
        # It takes self.tramp time to climb the ramp, so y position is
        # a linear function of time.
        if t < self.model.tramp:
            y = self.model.ymag * (t / self.model.tramp)
        else:
            y = self.model.ymag

        x1 = X[0]  # car position in vertical direction
        x1dot = X[1]  # car velocity  in vertical direction
        x2 = X[2]  # wheel position in vertical direction
        x2dot = X[3]  # wheel velocity in vertical direction

        # write the non-trivial equations in vertical direction
        x1ddot = (1 / self.model.m1) * (self.model.c1 * (x2dot - x1dot) + self.model.k1 * (x2 - x1))
        x2ddot = (1 / self.model.m2) * (
                -self.model.c1 * (x2dot - x1dot) - self.model.k1 * (x2 - x1) + self.model.k2 * (y - x2))

        # return the derivatives of the input state vector
        return [x1dot, x1ddot, x2dot, x2ddot]

    def set(self):
        """
        I will first set the basic properties of the car model and then calculate the result
        in another function doCalc.
        """
        self.model.m1 = float(self.view.le_m1.text())
        self.model.m2 = float(self.view.le_m2.text())
        self.model.c1 = float(self.view.le_c1.text())
        self.model.k1 = float(self.view.le_k1.text())
        self.model.k2 = float(self.view.le_k2.text())
        self.model.v = float(self.view.le_v.text())
        ymag = 6.0 / (12.0 * 3.3)  # I set this as a fixed ramp height of 6"
        if ymag is not None:
            self.model.ymag = ymag
        self.model.yangdeg = float(self.view.le_ang.text())
        self.model.tmax = float(self.view.le_tmax.text())

        self.doCalc()

    def setWidgets(self, w):
        self.view.setWidgets(w)

    def doCalc(self, doPlot=True):
        v = 1000 * self.model.v / 3600  # convert speed to m/s from kph
        self.model.angrad = self.model.yangdeg * math.pi / 180.0  # convert angle to radians
        self.model.tramp = self.model.ymag / (math.sin(self.model.angrad) * v)  # calculate time to traverse ramp
        self.model.t = np.linspace(0, self.model.tmax, 200)
        ic = [0, 0, 0, 0]
        # run odeint solver
        self.model.results = odeint(self.ode_system, ic, self.model.t)
        if doPlot:
            self.doPlot()

    # def OptimizeSuspension(self):
    #     x0 = [self.model.mink1, self.model.c1, self.model.mink2]
    #     answer = minimize(self.SSE, x0, method='Nelder-Mead')
    #     self.view.updateView(self.model)

    def OptimizeSuspension(self):
        x0 = [self.model.mink1, self.model.c1, self.model.mink2]
        answer = minimize(self.SSE, x0, method='Nelder-Mead')
        self.view.updateView(self.model)

    def SSE(self, vals):
        k1, c1, k2 = vals
        self.model.k1 = k1
        self.model.c1 = c1
        self.model.k2 = k2
        self.doCalc(doPlot=False)
        SSE = 0
        for i in range(len(self.model.results[:, 0])):
            t = self.model.t[i]
            y = self.model.results[i]
            if t < self.model.tramp:
                ytarget = self.model.ymag * t / self.model.tramp
            else:
                ytarget = self.model.ymag
            SSE += (y[0] - ytarget)**2
        # some penalty functions if the constants are too small
        if k1 < self.model.mink1 or k1 > self.model.maxk1:
            SSE += max(0, SSE - ytarget) ** 2
        if c1 < 1000:
            SSE += max(0, SSE - ytarget) ** 2
        if k2 < self.model.mink2 or k2 > self.model.maxk2:
            SSE += max(0, SSE - ytarget) ** 2

        return SSE

    def doPlot(self):
        self.view.doPlot(self.model)


class CarView():
    def __init__(self):
        self.ax = None
        self.le_k1 = qtw.QLineEdit()
        self.le_c1 = qtw.QLineEdit()
        self.le_k2 = qtw.QLineEdit()
        self.le_m1 = qtw.QLineEdit()
        self.le_m2 = qtw.QLineEdit()
        self.le_v = qtw.QLineEdit()
        self.le_ang = qtw.QLineEdit()
        self.le_tmax = qtw.QLineEdit()

    def setWidgets(self, w):
        self.le_m1 = w[0]
        self.le_v = w[1]
        self.le_k1 = w[2]
        self.le_c1 = w[3]
        self.le_m2 = w[4]
        self.le_k2 = w[5]
        self.le_ang = w[6]
        self.le_tmax = w[7]

    def updateView(self, model=None):
        self.le_m1.setText("{:0.2f}".format(model.m1))
        self.le_k1.setText("{:0.2f}".format(model.k1))
        self.le_c1.setText("{:0.2f}".format(model.c1))
        self.le_m2.setText("{:0.2f}".format(model.m2))
        self.le_k2.setText("{:0.2f}".format(model.k2))
        self.le_ang.setText("{:0.2f}".format(model.yangdeg))
        self.le_tmax.setText("{:0.2f}".format(model.tmax))
        self.doPlot(model)

    def doPlot(self, model=None):
        ax = self.ax
        t = model.t
        results = model.results
        # plot result of odeint solver
        QTPlotting = True  # assumes we are plotting onto a QT GUI form
        if ax == None:
            ax = plt.subplot()
            QTPlotting = False  # actually, we are just using CLI and showing the plot
        ax.clear()
        x = results
        ax.plot(t, x[:, 0], 'b-', label='Body Position')
        ax.plot(t, x[:, 2], 'r-', label='Wheel Position')

        # add axis labels
        ax.set_ylabel("Vertical Position (m)", fontsize='large' if QTPlotting else 'medium')
        ax.set_xlabel("time (s)", fontsize='large' if QTPlotting else 'medium')
        ax.legend()

        ax.axvline(x=model.tramp)  # vertical line at tramp
        ax.axhline(y=model.ymag)  # horizontal line at ymag
        # modify the tick marks
        ax.tick_params(axis='both', which='both', direction='in', top=True, right=True,
                       labelsize='large' if QTPlotting else 'medium')  # format tick marks
        # show the plot
        if QTPlotting == False:
            plt.show()


def main():
    QCM = CarController()
    QCM.doCalc()


if __name__ == '__main__':
    main()
