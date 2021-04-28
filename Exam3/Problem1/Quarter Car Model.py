from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import sys
from QuarterModelCarUI import Ui_Form

import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar



class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = self.verticalLayout
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        # self.setLayout(layout)

        self.setup_signals()
        self.show()

    def setup_signals(self):
        self.Calculate.clicked.connect(lambda: self.create_plot())

    def create_plot(self):
        t = np.linspace(0, 20, 200)  # time goes from 0 to 10 seconds
        ic = [0, 0, 0, 0]
        m1 = float(self.BodyMassInput.text())
        m2 = float(self.WheelMassInput.text())
        c1 = float(self.DampingCoefficientInput.text())
        k1 = float(self.k1Input.text())
        k2 = float(self.k2Input.text())
        ymag = 1  # the magnitude of the forcing function
        carparams = [m1, m2, c1, k1, k2]  # put the car parameters into a list
        roadparams = [ymag]  # put the road parameters into a list
        x = odeint(self.ode_system, ic, t, args=(carparams, roadparams))

        # create an axis
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(t, x[:, 0], 'b-', label='Body Position')
        ax.plot(t, x[:, 1], 'r-', label='Body Velocity')
        ax.legend(loc='lower right')
        ax.set(title='Car Body Dynamics', xlabel='Time, s', ylabel='Position and Velocity')

        self.canvas.draw()

    def ode_system(self, X, t, carparams, roadparams):
        # define any numerical parameters (constants)
        # these params were stored in two lists, and must be passed in the correct order!
        m1 = carparams[0]
        m2 = carparams[1]
        c1 = carparams[2]
        k1 = carparams[3]
        k2 = carparams[4]

        ymag = roadparams[0]

        # define the forcing function equation
        if t < np.pi / 2:
            y = ymag * np.sin(2 * t)
        else:
            y = 0

        x1 = X[0]
        x1dot = X[1]
        x2 = X[2]
        x2dot = X[3]  # copy from the state array to nicer names

        # write the non-trivial equations
        x1ddot = (1 / m1) * (c1 * (x2dot - x1dot) + k1 * (x2 - x1))
        x2ddot = (1 / m2) * (-c1 * (x2dot - x1dot) - k1 * (x2 - x1) + k2 * (y - x2))

        # return the derivitaves of the input state vector
        return [x1dot, x1ddot, x2dot, x2ddot]


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('Quarter Car Model')
    sys.exit(app.exec())
