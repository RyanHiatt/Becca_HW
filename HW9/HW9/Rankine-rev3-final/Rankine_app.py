from Rankine_GUI import Ui_Form
from PyQt5 import uic
import sys
from PyQt5 import QtWidgets as qtw
from Rankine import rankine
from Steam import *

# these imports are necessary for drawing a matplot lib graph on my GUI
# no simple widget for this exists in QT Designer, so I have to add the widget in code.
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.setupUi(self)
        # Main UI code goes here
        self.le_TurbineInletCondition.setEnabled(False)
        self.calculated = False
        # creating a canvas to draw a figure for the rankine cycle
        self.figure = Figure(figsize=(3, 8), tight_layout=True, frameon=True, facecolor='none')
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.ax = self.figure.add_subplot()
        self.main_VerticalLayout.addWidget(self.canvas)

        # setting up some signals and slots
        self.le_PHigh.editingFinished.connect(self.setPHigh)  # triggered by hitting enter or leaving the line edit
        self.le_PLow.editingFinished.connect(self.setPLow)  # triggered by hitting enter or leaving the line edit
        self.le_TurbineEff.editingFinished.connect(self.checkTurbineEffRange)
        self.rdo_Quality.toggled.connect(self.setQualityOrTHigh)  # triggered when the state of the radio button changes
        self.btn_Calculate.clicked.connect(self.calcRankine)
        self.cmb_Abcissa.currentIndexChanged.connect(self.doPlot)
        self.cmb_Ordinate.currentIndexChanged.connect(self.doPlot)
        self.chk_LogAbcissa.stateChanged.connect(self.doPlot)
        self.chk_LogOrdinate.stateChanged.connect(self.doPlot)
        # End main ui code

        # create a rankine object to work with later
        self.RC = rankine(8, 8000, name='Default Rankine Cycle')
        # create a steam object to help with retrieving saturated properties
        self.WorkingFluid = steam(8000, x=1.0)

        self.satPHigh = satProps()
        self.satPLow = satProps()
        # call the functions to set the saturation properties during construction of this class
        self.setPHigh()
        self.setPLow()

        # show the form
        self.show()

    def clamp(self, val, low, high):
        if self.isfloat(val):
            val = float(val)
            if val > high:
                return float(high)
            if val < low:
                return float(low)
            return val
        return float(low)

    def isfloat(self, value):
        '''
        This function is a check to verify that a string can be converted to a float
        :return:
        '''
        if value == 'NaN': return False
        try:
            float(value)
            return True
        except ValueError:
            return False

    def setPHigh(self):
        # make sure it is a number
        ph = self.le_PHigh.text()
        if not self.isfloat(ph):
            ph = '80'
            self.le_PHigh.setText(ph)

        PHigh = float(ph)  # convert text to number
        self.satPHigh = self.WorkingFluid.getSatProp(P_Bar=PHigh)
        self.TSatHigh = self.satPHigh.Tsat
        st_high = 'PSat = {:0.2f} bar, TSat = {:0.2f} C'.format(PHigh, self.satPHigh.Psat)
        st_high += '\nhf = {:0.2f} kJ/kg, hg = {:0.2f} kJ/kg'.format(self.satPHigh.hf, self.satPHigh.hg)
        st_high += '\nsf = {:0.2f} kJ/kg*K, sg = {:0.2f} kJ/kg*k'.format(self.satPHigh.sf, self.satPHigh.sg)
        st_high += '\nvf = {:0.4f} m^3/kg, vg = {:0.2f} m^3/kg'.format(self.satPHigh.vf, self.satPHigh.vg)
        self.lbl_SatPropHigh.setText(st_high)

    def setPLow(self):
        # make sure it is a number
        pl = self.le_PLow.text()
        if not self.isfloat(pl):
            pl = '0.08'
            self.le_PLow.setText(pl)

        PLow = float(self.le_PLow.text())  # convert text to number
        self.satPLow = self.WorkingFluid.getSatProp(P_Bar=PLow)
        # (Tsat, hf, hg, sf, sg, vf, vg)
        st_low = 'PSat = {:0.2f} bar, TSat = {:0.2f} C'.format(PLow, self.satPLow.Tsat)
        st_low += '\nhf = {:0.2f} kJ/kg, hg = {:0.2f} kJ/kg'.format(self.satPLow.hf, self.satPLow.hg)
        st_low += '\nsf = {:0.2f} kJ/kg*K, sg = {:0.2f} kJ/kg*k'.format(self.satPLow.sf, self.satPLow.sg)
        st_low += '\nvf = {:0.4f} m^3/kg, vg = {:0.2f} m^3/kg'.format(self.satPLow.vf, self.satPLow.vg)
        self.lbl_SatPropLow.setText(st_low)

    def checkTurbineEffRange(self):
        '''
        Makes sure turbine efficiency is in the range from 0 to 1
        :return:
        '''
        e = self.clamp(self.le_TurbineEff.text(), 0.0, 1.0)
        self.le_TurbineEff.setText(str(e))

    def setQualityOrTHigh(self):
        TF = self.rdo_Quality.isChecked()
        if TF:
            self.lbl_TurbineInletCondition.setText('Turbine Inlet: x=')
            self.le_TurbineInletCondition.setText(str(1.0))
            self.le_TurbineInletCondition.setEnabled(False)
        else:
            self.lbl_TurbineInletCondition.setText('Turbine Inlet: T High =')
            self.le_TurbineInletCondition.setText('{:0.2f}'.format(self.TSatHigh + 1))
            self.le_TurbineInletCondition.setEnabled(True)

    def doPlot(self):
        self.ax.clear()
        X = self.cmb_Abcissa.currentText()
        Y = self.cmb_Ordinate.currentText()
        logx = self.chk_LogAbcissa.isChecked()
        logy = self.chk_LogOrdinate.isChecked()
        self.RC.plot_cycle_XY(X=X, Y=Y, ax=self.ax, logx=logx, logy=logy)
        self.canvas.draw()

    def calcRankine(self):
        '''
        This is called when the calculate button is clicked
        :return: nothing
        '''
        # read the high and low pressure isobar values.  no range checking.
        PHigh = float(self.le_PHigh.text())
        PLow = float(self.le_PLow.text())

        # create a new rankine object with values depending on which radio buttton checked
        if (self.rdo_Quality.isChecked()):
            self.RC.set(p_low=PLow * 100, p_high=PHigh * 100, eff_turbine=float(self.le_TurbineEff.text()))
        else:
            self.RC.set(p_low=PLow * 100, p_high=PHigh * 100, eff_turbine=float(self.le_TurbineEff.text()),
                        t_high=float(self.le_TurbineInletCondition.text()))
        # calculate the cycle efficiency (and states 1,2,3,4)
        self.RC.calc_efficiency()

        # fill out the enthalpy values
        self.le_H1.setText('{:0.2f}'.format(self.RC.state1.h))
        self.le_H2.setText('{:0.2f}'.format(self.RC.state2.h))
        self.le_H3.setText('{:0.2f}'.format(self.RC.state3.h))
        self.le_H4.setText('{:0.2f}'.format(self.RC.state4.h))

        # fill out the other properties for the rankine cycle
        self.le_Efficiency.setText('{:0.2f}'.format(self.RC.efficiency))
        self.le_TurbineWork.setText('{:0.2f}'.format(self.RC.turbine_work))
        self.le_PumpWork.setText('{:0.2f}'.format(self.RC.pump_work))
        self.le_HeatAdded.setText('{:0.2f}'.format(self.RC.heat_added))

        self.doPlot()
        self.cmb_Abcissa.setEnabled(True)
        self.cmb_Ordinate.setEnabled(True)
        # self.ax.clear()
        # self.RC.plot_cycle_XY(X='s', Y='T', ax=self.ax)
        # self.canvas.draw()

        # self.ax.clear()
        # self.RC.plot_cycle_XY(X='h', Y='T', ax=self.ax)
        # self.canvas.draw()

        # self.ax.clear()
        # self.RC.plot_cycle_XY(X='s', Y='h', ax=self.ax)
        # self.canvas.draw()


# if this module is being imported, this won't run. If it is the main module, it will run.
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('Rankine Cycle Calculator')
    sys.exit(app.exec())
