from Pump import Pump
from Pump_GUI import Ui_Form
import sys
from PyQt5 import QtWidgets as qtw

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.setupUi(self)
        # Main UI code goes here
        self.model = Pump()

        # creating a canvas to draw a figure for the rankine cycle
        self.figure = Figure(figsize=(3, 8), tight_layout=True, frameon=True, facecolor='none')
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.ax1 = self.figure.add_subplot()
        self.graph_layout.addWidget(self.canvas)

        # Signals and Slots
        self.btn_Calculate.clicked.connect(self.calculate)

        # show the form
        self.show()

    def calculate(self):
        self.read_pump_file()
        self.set_outputs()
        self.doPlot()

    def read_pump_file(self):
        # open the file dialog box to search for the file I want
        filename = qtw.QFileDialog.getOpenFileName()[0]
        if len(filename) == 0:  # no file selected
            return
        self.input_FileName.setText(filename)  # echo the filename on the GUI
        self.model.read_file(filename)

    def set_outputs(self):
        self.output_PumpName.setText(self.model.pump_name)
        self.output_FlowUnits.setText(self.model.flow_units)
        self.output_HeadUnits.setText(self.model.head_units)
        self.output_HeadCoefficients.setText(self.model.list_to_string(self.model.head))
        self.output_EfficiencyConstraints.setText(self.model.list_to_string(self.model.efficiency))

    def doPlot(self):
        self.model.plot_data(ax1=self.ax, ax2=self.ax2)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('Otto Cycle Calculator')
    sys.exit(app.exec())
