import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWindow(QtWidgets.QWidget) :
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        tabs = QtWidgets.QTabWidget()
        tab1 = QtWidgets.QWidget()
        tab2 = QtWidgets.QWidget()
        tabs.addTab(tab1, "Tab 1")
        tabs.addTab(tab2, "Tab 2")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(tabs)
        self.setLayout(layout)
        self.setMouseTracking(True)

    def setMouseTracking(self, flag):
        def recursive_set(parent):
            for child in parent.findChildren(QtCore.QObject):
                try:
                    child.setMouseTracking(flag)
                except:
                    pass
                recursive_set(child)
        QtWidgets.QWidget.setMouseTracking(self, flag)
        recursive_set(self)

    def mouseMoveEvent(self, event):
        print('mouseMoveEvent: x=%d, y=%d' % (event.x(), event.y()))


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setFixedSize(640, 480)
window.show()
sys.exit(app.exec_())