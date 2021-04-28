from GraphicsView_GUI import Ui_Form
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import math
import sys

class MainWindow(Ui_Form, qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #region UserInterface stuff here

        #set up graphics view, scene and build pens and brushes
        self.setupGraphics()

        #turning on mouse tracking
        self.gv_Main.setMouseTracking(True)
        self.pushButton.setMouseTracking(True)
        self.setMouseTracking(True)

        #draws a scene
        self.buildScene()

        #signals/slots
        self.spnd_Zoom.valueChanged.connect(self.setZoom)
        self.pushButton.clicked.connect(self.pickAColor)
        self.scene.installEventFilter(self)

        self.show()

    def setupGraphics(self):
        #create a scene object
        self.scene = qtw.QGraphicsScene()
        self.scene.setObjectName("MyScene")
        self.scene.setSceneRect(-200, -200, 400, 400)  # xLeft, yTop, Width, Height

        #set the scene for the graphics view object
        self.gv_Main.setScene(self.scene)
        #make some pens and brushes for my drawing
        self.setupPensAndBrushes()

    def setupPensAndBrushes(self):
        #make the pens first
        #a thick green pen
        self.penThick = qtg.QPen(qtc.Qt.GlobalColor.darkGreen)
        self.penThick.setWidth(10)
        #a medium blue pen
        self.penMed = qtg.QPen(qtc.Qt.GlobalColor.darkBlue)
        self.penMed.setStyle(qtc.Qt.PenStyle.SolidLine)
        self.penMed.setWidth(2)
        #a pen for the grid lines
        self.penGridLines = qtg.QPen()
        self.penGridLines.setWidth(1)
        self.penGridLines.setColor(qtg.QColor.fromHsv(197, 144, 228, 255))

        #now make some brushes
        #build a brush for filling with solid red
        self.brushFill = qtg.QBrush(qtc.Qt.GlobalColor.darkRed)
        #a brush that makes a hatch pattern
        self.brushHatch = qtg.QBrush()
        self.brushHatch.setStyle(qtc.Qt.BrushStyle.DiagCrossPattern)
        #a brush for the background of my grid
        self.brushGrid = qtg.QBrush(qtg.QColor.fromHsv(87, 98, 245, 255))

    def mouseMoveEvent(self, a0: qtg.QMouseEvent):
        w=app.widgetAt(a0.globalPos())
        if w is None:
            name='none'
        else:
            name=w.objectName()
        self.setWindowTitle(str(a0.x())+','+ str(a0.y())+name)

    def eventFilter(self, obj, event):
        # I set up an event filter to track mouse position and illustrate difference between scene and screen coords.
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

    def buildScene(self):
        #clear out the old scene first
        self.scene.clear()

        #draw a grid
        self.drawAGrid(DeltaX=10, DeltaY=10, Pen=self.penGridLines, Brush=self.brushGrid)

        #draw some lines
        self.line1 = qtw.QGraphicsLineItem(-50, -50, -50, 50)
        self.line1.setPen(self.penThick)
        self.scene.addItem(self.line1)
        self.line2 = qtw.QGraphicsLineItem(-50, -50, 50, -50)
        self.line2.setPen(self.penThick)
        self.scene.addItem(self.line2)

        self.drawACircle(-50,-50,5, pen=self.penMed, brush=self.brushFill)
        self.drawASquare(-50,50,10, pen=self.penMed, brush=self.brushFill)
        self.drawATriangle(50,-50,10, pen=self.penMed, brush=self.brushHatch)
        self.drawAnArrow(0,0,10,-20,pen=self.penMed, brush=self.brushFill)

    def drawAGrid(self, DeltaX=10, DeltaY=10, Height=200, Width=200, CenterX=0, CenterY=0, Pen=None, Brush=None,
                  SubGrid=None):
        """
        This makes a grid for reference.  No snapping to grid enabled.
        :param DeltaX: grid spacing in x direction
        :param DeltaY: grid spacing in y direction
        :param Height: height of grid (y)
        :param Width: width of grid (x)
        :param CenterX: center of grid (x, in scene coords)
        :param CenterY: center of grid (y, in scene coords)
        :param Pen: pen for grid lines
        :param Brush: brush for background
        :param SubGrid: subdivide the grid (not currently working)
        :return: nothing
        """
        height = self.scene.sceneRect().height() if Height is None else Height
        width = self.scene.sceneRect().width() if Width is None else Width
        left = self.scene.sceneRect().left() if CenterX is None else (CenterX - width / 2.0)
        right = self.scene.sceneRect().right() if CenterX is None else (CenterX + width / 2.0)
        top = self.scene.sceneRect().top() if CenterY is None else (CenterY - height / 2.0)
        bottom = self.scene.sceneRect().bottom() if CenterY is None else (CenterY + height / 2.0)
        Dx = DeltaX
        Dy = DeltaY
        pen = qtg.QPen() if Pen is None else Pen

        # make the background rectangle first
        if Brush is not None:
            rect = qtw.QGraphicsRectItem(left, top, width, height)
            rect.setBrush(Brush)
            rect.setPen(pen)
            self.scene.addItem(rect)
        # draw the vertical grid lines
        x = left
        while x <= right:
            lVert = qtw.QGraphicsLineItem(x, top, x, bottom)
            lVert.setPen(pen)
            self.scene.addItem(lVert)
            x += Dx
        # draw the horizontal grid lines
        y = top
        while y <= bottom:
            lHor = qtw.QGraphicsLineItem(left, y, right, y)
            lHor.setPen(pen)
            self.scene.addItem(lHor)
            y += Dy

    def polarToRect(self, centerX, centerY, radius, angleDeg=0):
        angleRad=angleDeg*2.0*math.pi/360.0
        return centerX+radius*math.cos(angleRad), centerY+radius*math.sin(angleRad)

    def drawACircle(self, centerX, centerY, Radius, angle=0, brush=None, pen=None):
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

    def drawATriangle(self, centerX, centerY, Radius, angleDeg=0,brush=None, pen=None):
        pts=[]

        x,y=self.polarToRect(centerX,centerY,Radius, 0+angleDeg)
        pts.append(qtc.QPointF(x,y))
        x,y=self.polarToRect(centerX,centerY,Radius,120+angleDeg)
        pts.append(qtc.QPointF(x,y))
        x,y=self.polarToRect(centerX, centerY,Radius,240+angleDeg)
        pts.append(qtc.QPointF(x,y))
        x,y=self.polarToRect(centerX,centerY,Radius,0+angleDeg)
        pts.append(qtc.QPointF(x,y))

        pg=qtg.QPolygonF(pts)
        PG=qtw.QGraphicsPolygonItem(pg)
        if pen is not None:
            PG.setPen(pen)
        if brush is not None:
            PG.setBrush(brush)
        self.scene.addItem(PG)

    def drawAnArrow(self, startX, startY, endX, endY, pen=None, brush=None):
        line=qtw.QGraphicsLineItem(startX, startY, endX, endY)
        p=qtg.QPen() if pen is None else pen
        line.setPen(pen)
        angleDeg=180.0/math.pi*math.atan((endY-startY)/(endX-startX))
        self.scene.addItem(line)
        self.drawATriangle(endX, endY, 5, angleDeg=angleDeg,pen=pen, brush=brush)

    def pickAColor(self):
        cdb=qtw.QColorDialog(self)
        c=cdb.getColor()
        hsv=c.getHsv()
        self.pushButton.setText(str(hsv))
        self.penGridLines.setColor(qtg.QColor.fromHsv(hsv[0],hsv[1],hsv[2],hsv[3]))
        self.buildScene()
        pass

    def setZoom(self):
        self.gv_Main.resetTransform()
        self.gv_Main.scale(self.spnd_Zoom.value(), self.spnd_Zoom.value())

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('GraphicsView')
    sys.exit(app.exec())
