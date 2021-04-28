from Car_GUI import Ui_Form
import sys
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from QuarterCarModel import CarController

#these imports are necessary for drawing a matplot lib graph on my GUI
#no simple widget for this exists in QT Designer, so I have to add the widget in code.
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self):
        """
        Main window constructor.
        """
        super().__init__()
        self.setupUi(self)

        # connect clicked signal of calculate button
        self.btn_calculate.clicked.connect(self.doCalculate)
        self.pb_Optimize.clicked.connect(self.doOptimize)

        # creating a canvas to draw a figure for the car model
        self.figure = Figure(figsize=(3,8),tight_layout=True, frameon=True, facecolor='none')
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.layout_MainVertical.addWidget(self.canvas)

        # setup car controller
        self.controller=CarController(self.figure.add_subplot())  # instantiate controller with axes argument
        w=[self.le_mcar, self.le_CarSpeed, self.le_k1, self.le_c1, self.le_m2, self.le_k2, self.le_AngDeg, self.le_tMax]
        # pass this list of widgets to the controller so they can be used in calculations and for view
        self.controller.setWidgets(w)
        # show the main window/widget
        self.show()

    def doCalculate(self):
        # this reads the values from the widgets I passed, calculates odeint solution and plots the graph
        self.controller.set()
        self.canvas.draw()

    def doOptimize(self):
        # calls the OptimizeSuspension function of the controller then displays k1,c1,k2 on the widgets and plots
        self.controller.OptimizeSuspension()
        self.canvas.draw()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('Quarter Car Model')
    sys.exit(app.exec())
