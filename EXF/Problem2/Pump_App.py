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
        self.ax = self.figure.add_subplot()
        self.main_VerticalLayout.addWidget(self.canvas)

        # Signals and Slots

        # show the form
        self.show()

    def read_pump_file(self):
        # open the file dialog box to search for the file I want
        filename = qtw.QFileDialog.getOpenFileName()[0]
        if len(filename) == 0:  # no file selected
            return
        self.input_filename.setText(filename)  # echo the filename on the GUI
        self.model.read_file(filename)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('Otto Cycle Calculator')
    sys.exit(app.exec())
