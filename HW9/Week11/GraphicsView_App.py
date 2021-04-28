from GraphicsView_GUI import Ui_Form
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import sys

class MainWindow(Ui_Form, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #region UserInterface stuff here
        self.scene = qtw.QGraphicsScene()
        self.scene.setObjectName("My Drawing Scene")
        self.brushFill=qtg.QBrush(qtc.Qt.red)

        self.penThick=qtg.QPen(qtc.Qt.green)
        self.penThick.setStyle(qtc.Qt.DashLine)
        self.penThick.setWidth(3)
        self.penThick.setCapStyle(qtc.Qt.RoundCap)

        self.penMed=qtg.QPen(qtc.Qt.darkBlue)
        self.penMed.setStyle(qtc.Qt.SolidLine)

        self.size=self.scene.setSceneRect(-200,-200,400,400)

        self.scene.installEventFilter(self)
        self.gv_Main.setScene(self.scene)
        self.gv_Main.scale(2,2)
        self.gv_Main.setMouseTracking(True)
        self.pushButton.setMouseTracking(True)
        self.setMouseTracking(True)
        #self.scene.setSceneRect(-100,-100,200,200)
        name=self.scene.objectName()
        self.drawAGrid()
        self.drawACircle(-50,-50,20, pen=self.penThick, brush=self.brushFill)
        #self.drawATriangle(-50,50,20,pen=self.penThick)
        self.drawASquare(-50,50,20, pen=self.penMed, brush=self.brushFill)
        self.drawATriangle(50,-50,30, pen=self.penMed, brush=self.brushFill)
        self.spnd_Zoom.valueChanged.connect(self.setZoom)
        self.show()

    def mouseMoveEvent(self, a0: qtg.QMouseEvent) :
        w=app.widgetAt(a0.globalPos())
        if w is None:
            name='none'
        else:
            name=w.objectName()
        self.setWindowTitle(str(a0.x())+','+ str(a0.y())+name)

    def eventFilter(self, obj, event):

        if obj == self.scene:
            et=event.type()
            if event.type() == qtc.QEvent.GraphicsSceneMouseMove:
                w=app.topLevelAt(event.screenPos())
                screenPos=event.screenPos()
                scenePos=event.scenePos()
                strScreen="screen x = {}, screen y = {}".format(screenPos.x(), screenPos.y())
                strScene=":  scene x = {}, scene y = {}".format(scenePos.x(), scenePos.y())
                self.setWindowTitle(strScreen+strScene)

        # pass the event along to the parent widget if there is one.
        return super(MainWindow, self).eventFilter(obj, event)

    def drawAGrid(self):
        height=self.scene.sceneRect().height()
        width=self.scene.sceneRect().width()
        left=self.scene.sceneRect().left()
        right=self.scene.sceneRect().right()
        top=self.scene.sceneRect().top()
        bottom=self.scene.sceneRect().bottom()
        Dx=10
        Dy=10
        self.gridlines=[]
        x=left
        while x <= right:
            self.gridlines.append(qtw.QGraphicsLineItem(x,top,x,bottom))
            self.scene.addItem(self.gridlines[len(self.gridlines)-1])
            x += Dx
        y=top
        while y<=bottom:
            self.scene.addItem(qtw.QGraphicsLineItem(left, y, right,y))
            y+= Dy

    def drawACircle(self, centerX, centerY, Radius, brush=None, pen=None):
        ellipse=qtw.QGraphicsEllipseItem(centerX-Radius, centerY-Radius,2*Radius, 2*Radius)
        if pen is not None:
            ellipse.setPen(pen)
        if brush is not None:
            ellipse.setBrush(brush)
        self.scene.addItem(ellipse)

    def drawASquare(self, centerX, centerY, Size, brush=None, pen=None):
        sqr=qtw.QGraphicsRectItem(centerX-Size/2.0, centerY-Size/2.0, Size, Size)
        if pen is not None:
            sqr.setPen(pen)
        if brush is not None:
            sqr.setBrush(brush)
        self.scene.addItem(sqr)

    def drawATriangle(self, centerX, centerY, Radius, brush=None, pen=None):
        pts=[]
        pts.append(qtc.QPointF(centerX-Radius,centerY+Radius))
        pts.append(qtc.QPointF(centerX+Radius,centerY))
        pts.append(qtc.QPointF(centerX-Radius,centerY-Radius))
        pts.append(qtc.QPointF(centerX-Radius,centerY+Radius))

        pg=qtg.QPolygonF(pts)
        PG=qtw.QGraphicsPolygonItem(pg)
        if pen is not None:
            PG.setPen(pen)
        if brush is not None:
            PG.setBrush(brush)
        self.scene.addItem(PG)


    def setZoom(self):
        self.gv_Main.resetTransform()
        self.gv_Main.scale(self.spnd_Zoom.value(), self.spnd_Zoom.value())

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('GraphicsView')
    sys.exit(app.exec())
