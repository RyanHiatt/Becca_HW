import math


from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class Link:
    def __init__(self, node1='1', node2='2', length=None, angleRad=None):
        self.name = None
        self.node1 = node1
        self.node2 = node2
        self.length = length
        self.angleRad = angleRad

    def __eq__(self, other):
        if self.node1 != other.node1:
            return False
        if self.node2 != other.node2:
            return False
        if self.length != other.length:
            return False
        if self.angleRad != other.angleRad:
            return False
        return True

    def set(self, node1=None, node2=None, length=None, angleRad=None):
        self.node1 = node1
        self.node2 = node2
        self.length = length
        self.angleRad = angleRad


class Material:
    def __init__(self, uts=None, ys=None, modulus=None, staticFactor=None):
        self.uts = uts
        self.ys = ys
        self.E = modulus
        self.staticFactor = staticFactor


class Position:
    def __init__(self):
        pass


class Node:
    def __init__(self, name=None, position=None):
        self.name = name
        self.position = position if position is not None else Position()

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.position != other.position:
            return False
        return True


class Truss:
    def __init__(self):
        self.title = None
        self.links = []
        self.nodes = []
        self.material = Material()
        self.longestlink = None

    def getNode(self, name):
        for n in self.nodes:
            if n.name == name:
                return n

    def getLink(self, name):
        for l in self.links:
            if l.name == name:
                return l


class TrussController():
    def __init__(self):
        self.truss = Truss()
        self.view = TrussView()

    def ImportFromFile(self, data):
        self.truss.nodes.clear()
        self.truss.links.clear()

        i = 0
        while i < len(data):
            L = data[i]
            L.lower().strip()

            if L.find('#') == 0:
                pass

            elif L.find('Title') >= 0:
                cells = data[i].split(',')
                self.truss.title = cells[1].split("'")[1]

            elif L.find('Material') >= 0:
                cells = data[i].split(',')
                self.truss.material.uts = cells[1].strip()
                self.truss.material.ys = cells[2].strip()
                self.truss.material.E = cells[3].strip()

            elif L.find('Static_factor') >= 0:
                self.truss.material.staticFactor = data[i].split(',')[1].strip()

            elif L.find('node') >= 0:
                n = Node()
                cells = data[i].split(',')
                n.name = cells[1].lower().strip()
                n.position = (float(cells[2].strip()), float(cells[3].strip()))
                self.truss.nodes.append(n)

            elif L.find('link') >= 0:
                l = Link()
                cells = data[i].split(',')
                l.name = cells[1].lower().strip()
                # l.node1 = cells[2].lower().strip()
                l.node1 = self.truss.getNode(cells[2].lower().strip())
                # l.node2 = cells[3].lower().strip()
                l.node2 = self.truss.getNode(cells[3].lower().strip())
                length, angle = self.calcLinkVals(l)
                l.length = length
                l.angleRad = angle
                self.truss.links.append(l)
            i += 1

        rand_dict = {}
        for l in self.truss.links:
            rand_dict[l.name] = l.length

        self.truss.longestlink = self.truss.getLink(max(rand_dict))

    def calcLinkVals(self, link):
        x1 = link.node1.position[0]
        y1 = link.node1.position[1]
        x2 = link.node2.position[0]
        y2 = link.node2.position[1]

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        angle = 1

        return distance, angle

    def setDisplayWidgets(self, args):
        pass

    def displayReport(self):
        report = self.view.displayReport(truss=self.truss)
        return report

    def drawTruss(self):
        self.view.buildScene()


class TrussView():
    def __init__(self):
        self.scene = qtw.QGraphicsScene()
        self.le_LongLinkName = qtw.QLineEdit()
        self.le_LongLinkNode1 = qtw.QLineEdit()
        self.le_LongLinkNode2 = qtw.QLineEdit()
        self.le_LongLinkLength = qtw.QLineEdit()
        self.te_Report = qtw.QTextEdit()
        self.gv = qtw.QGraphicsView()

    def setDisplayWidgets(self, args):
        pass

    def displayReport(self, truss=None):

        report = '\t\tTruss Design Report\n'
        report += f'Title: {truss.title}\n'
        report += f'Static Factor of Safety: {truss.material.staticFactor}\n'
        report += f'Ultimate Strength: {truss.material.uts}\n'
        report += f'Yield Strength: {truss.material.ys}\n'
        report += f'Modulus of Elasticity: {truss.material.E}\n'
        report += '---------- Link Summary ----------\n'
        report += 'Link\tNode1\tNode2\tLength\tAngle\n'
        for l in truss.links:
            report += f'{l.name}\t{l.node1.name}\t{l.node2.name}\t{l.length:.1f}\t{l.angleRad:.1f}\n'

        return report

    def buildScene(self, truss=None):
        # clear out the old scene first
        self.scene.clear()

        self.setupPensAndBrushes()

        # draw a grid
        self.drawAGrid(DeltaX=10, DeltaY=10, Height=400, Width=400, Pen=self.penGridLines, Brush=self.brushGrid)

        # # draw the pipe network
        # self.View.drawPipes(PN=self.Model, scene=self.scene, penPipe=self.penPipe, brushPipe=self.brushFill)
        # self.View.drawNodes(PN=self.Model, scene=self.scene, penNode=self.penNode, brushNode=self.brushNode)
        # self.View.drawLoopLabels(PN=self.Model, pen=self.penNode, scene=self.scene)
        # self.View.drawNodeExtFlows(PN=self.Model, pen=self.penNode, brush=self.brushNode, scene=self.scene)

    def setZoom(self):
        self.gv_Main.resetTransform()
        self.gv_Main.scale(self.spnd_Zoom.value(), self.spnd_Zoom.value())

    def setupPensAndBrushes(self):
        #make the pens first
        #a thick darkGray pen
        self.penTruss = qtg.QPen(qtc.Qt.darkGray)
        self.penTruss.setStyle(qtc.Qt.SolidLine)
        self.penTruss.setWidth(4)
        #a medium darkBlue pen
        self.penNode = qtg.QPen(qtc.Qt.darkBlue)
        self.penNode.setStyle(qtc.Qt.SolidLine)
        self.penNode.setWidth(1)
        #a pen for the grid lines
        self.penGridLines = qtg.QPen()
        self.penGridLines.setWidth(1)
        self.penGridLines.setColor(qtg.QColor.fromHsv(197, 144, 228, 255))

        #now make some brushes
        #build a brush for filling with solid red
        self.brushFill = qtg.QBrush(qtc.Qt.darkRed)
        #a brush that makes a hatch pattern
        self.brushNode = qtg.QBrush(qtc.Qt.yellow)
        #a brush for the background of my grid
        self.brushGrid = qtg.QBrush(qtg.QColor.fromHsv(87, 98, 245, 255))

    def drawAGrid(self, DeltaX=10, DeltaY=10, Height=320, Width=180, CenterX=120, CenterY=60, Pen=None, Brush=None):
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

    def drawLinks(self, truss=None):
        pass

    def drawNodes(self, truss=None, scene=None):
        nodePen = qtg.QPen() if penNode is None else penNode
        nodeBrush = qtg.QBrush() if brushNode is None else brushNode
        for n in truss.nodes:
            x = n.position[0]
            y = n.position[1]
            self.drawACircle(x, y, 5, penNode, brushNode, scene=scene)  # draw a circle for the node
            self.drawALabel(x, y, f'{n.Name}', penNode, scene=scene)  # draw a label for the node

    def drawALabel(self, x, y, str='', pen=None, brush=None, tip=None):
        pass

    def drawACircle(self, centerX, centerY, Radius, angle=0, brush=None, pen=None, name=None, tooltip=None):
        ellipse = qtw.QGraphicsEllipseItem(centerX - Radius, centerY - Radius, 2 * Radius, 2 * Radius)
        if pen is not None:
            ellipse.setPen(pen)
        if brush is not None:
            ellipse.setBrush(brush)
        self.scene.addItem(ellipse)
