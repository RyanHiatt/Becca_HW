from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from Truss import TrussController
from Truss_GUI import Ui_TrussStructuralDesign
import sys


class MainWindow(Ui_TrussStructuralDesign, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_Open.clicked.connect(self.OpenFile)
        self.spnd_Zoom.valueChanged.connect(self.setZoom)

        self.controller = TrussController()
        self.controller.setDisplayWidgets((self.te_DesignReport, self.le_LinkName, self.le_Node1Name,
                                           self.le_Node2Name, self.le_LinkLength, self.gv_Main))

        self.controller.view.scene.installEventFilter(self)
        self.gv_Main.setMouseTracking(True)

        self.show()

    def setZoom(self):
        self.gv_Main.resetTransform()
        self.gv_Main.scale(self.spnd_Zoom.value(), self.spnd_Zoom.value())

    def eventFilter(self, obj, event):
        if obj == self.controller.view.scene:
            et = event.type()
            if et == qtc.QEvent.GraphicsSceneMouseMove:
                scenePos = event.scenePos()
                strScene = f"Mouse Position: x = {round(scenePos.x(), 2)}, y = {round(-scenePos.y(), 2)}"
                self.lbl_MousePos.setText(strScene)
            if event.type() == qtc.QEvent.GraphicsSceneWheel:
                if event.delta() > 0:
                    self.spnd_Zoom.stepUp()
                else:
                    self.spnd_Zoom.stepDown()
                pass

        return super(MainWindow, self).eventFilter(obj, event)

    def OpenFile(self):
        filename = qtw.QFileDialog.getOpenFileName()[0]
        if len(filename) == 0:
            return
        self.te_Path.setText(filename)
        file = open(filename, 'r')
        data = file.readlines()
        self.controller.ImportFromFile(data)
        report = self.controller.displayReport()

        self.te_DesignReport.setText(report)
        self.le_LinkName.setText(self.controller.truss.longestlink.name)
        self.le_Node1Name.setText(self.controller.truss.longestlink.node1.name)
        self.le_Node2Name.setText(self.controller.truss.longestlink.node2.name)
        self.le_LinkLength.setText(str(self.controller.truss.longestlink.length))

        self.controller.drawTruss(self.gv_Main)


def Main():
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    Main()
