from OttoCycle_GUI import Ui_Form
import sys
from PyQt5 import QtWidgets as qtw

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from OttoCycle import OttoCycle, Controller, View


class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.setupUi(self)
        # Main UI code goes here
        self.model = OttoCycle()
        self.controller = Controller()
        self.view = View()

        # creating a canvas to draw a figure for the rankine cycle
        self.figure = Figure(figsize=(3, 8), tight_layout=True, frameon=True, facecolor='none')
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.ax = self.figure.add_subplot()
        self.main_VerticalLayout.addWidget(self.canvas)

        # Signals and Slots
        self.btn_Calculate.clicked.connect(self.run_backend)
        self.rdo_Metric.toggled.connect(self.set_output)

        # show the form
        self.show()

    def run_backend(self):
        self.initialize_values()
        self.controller.run_cycle()
        self.set_output()
        self.doPlot()

    def initialize_values(self):
        values = [float(self.input_CylinderVolume.text()),
                  float(self.input_InitialPressure.text()),
                  float(self.input_CompressionRatio.text()),
                  float(self.input_InitialTemperature.text()),
                  float(self.input_MaximumTemperature.text())]
        self.controller.init_values(values)

    def set_output(self):
        TF = self.rdo_Metric.isChecked()
        if TF:  # Set Metric Units
            self.output_T1.setText(f'{self.controller.view.kelvin_to_celsius(self.controller.model.T[0]):.2f}')
            self.output_T2.setText(f'{self.controller.view.kelvin_to_celsius(self.controller.model.T[1]):.2f}')
            self.output_T3.setText(f'{self.controller.view.kelvin_to_celsius(self.controller.model.T[2]):.2f}')
            self.output_T4.setText(f'{self.controller.view.kelvin_to_celsius(self.controller.model.T[3]):.2f}')
            self.label_t1.setText('Celsius')
            self.label_t2.setText('Celsius')
            self.label_t3.setText('Celsius')
            self.label_t4.setText('Celsius')
        else:  # Set English Units
            self.output_T1.setText(f'{self.controller.view.kelvin_to_fahrenheit(self.controller.model.T[0]):.2f}')
            self.output_T2.setText(f'{self.controller.view.kelvin_to_fahrenheit(self.controller.model.T[1]):.2f}')
            self.output_T3.setText(f'{self.controller.view.kelvin_to_fahrenheit(self.controller.model.T[2]):.2f}')
            self.output_T4.setText(f'{self.controller.view.kelvin_to_fahrenheit(self.controller.model.T[3]):.2f}')
            self.label_t1.setText('Fahrenheit')
            self.label_t2.setText('Fahrenheit')
            self.label_t3.setText('Fahrenheit')
            self.label_t4.setText('Fahrenheit')

        self.output_CycleEfficiency.setText(f'{self.controller.model.eff * 100:.2f}')

    def doPlot(self):
        self.ax.clear()
        X = self.cmb_Abcissa.currentText()
        Y = self.cmb_Ordinate.currentText()
        self.controller.plot_cycle_XY(x=X, y=Y, ax=self.ax)
        self.canvas.draw()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('Otto Cycle Calculator')
    sys.exit(app.exec())
