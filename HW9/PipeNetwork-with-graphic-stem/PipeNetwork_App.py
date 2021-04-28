import sys
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PipeNetwork_GUI import Ui_Form
from PipeNetwork_classes import *


class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self):
        """
        Main window constructor.
        """
        super().__init__()
        self.setupUi(self)
        self.Model = PipeNetwork()  # start with an empty pipe network #$MODEL$#
        self.View = PipeNetworkView()  # view for Pipe Network #$VIEW$#
        self.Controller = PipeNetworkController()  # controller for modifying the Pipe Network #$CONTROLLER$#
        self.setupGraphicsView()
        self.buildScene()
        # Main UI code goes here
        self.setupSignalsSlotsEventFilter()
        # end Main UI code
        self.fitColumns()
        self.show()  # show the main widget

    def setupSignalsSlotsEventFilter(self):
        """
        This is called from the constructor to wire up the signals and slots and install event filter if needed.
        :return: nothing
        """
        # CONNECTING SIGNALS AND SLOTS
        # these available signals can be easily connected to a slot
        self.btn_AddPipe.clicked.connect(self.addPipeToPipeList)
        self.btn_DeletePipe.clicked.connect(self.deletePipe)
        self.btn_AddPipeToLoop.clicked.connect(self.addPipeToLoop)
        self.btn_CreateLoop.clicked.connect(self.createLoop)
        self.btn_Evaluate.clicked.connect(self.EvaluatePipeNetwork)
        self.tree_Pipes.itemChanged.connect(self.modifyPipe)
        self.tree_Nodes.itemChanged.connect(self.modifyNode)
        self.tree_Loops.itemChanged.connect(self.modifyLoop)
        self.btn_OpenPipeNetworkFile.clicked.connect(self.readPipeNetworkFile)
        self.btn_SavePipeNetworkFile.clicked.connect(self.savePipeNetworkFile)
        self.spnd_Zoom.valueChanged.connect(self.setZoom) #$NEW$ double spinner widget for setting zoom level

        # INSTALLING AN EVENT FILTER ON THE TREE WIDGETS
        # I do this if there is no easy signal to connect to do what I want.
        # The event filter allows the widget to analyze events from the windows event loop when
        # they occur on the widget.
        # if a signal is not available, I can use the event filter to take action
        self.tree_Pipes.installEventFilter(self)
        self.tree_LoopPipes.installEventFilter(self)
        self.tree_Loops.installEventFilter(self)

    def eventFilter(self, obj, event):
        """
        This overrides the default eventFilter of the widget.  It takes action on events and then passes the event
        along to the parent widget.
        :param obj: The object on which the event happened
        :param event: The event itself
        :return: boolean from the parent widget
        """
        #region $NEW$ 4/6/21 for mouse tracking on the drawing
        if obj == self.scene:
            et=event.type()
            if event.type() == qtc.QEvent.GraphicsSceneMouseMove:
                w=app.topLevelAt(event.screenPos())
                scenePos=event.scenePos()
                strScene="Mouse Position:  x = {}, y = {}".format(round(scenePos.x(),2), round(scenePos.y(),2))
                self.lbl_MousePosition.setText(strScene)
        #endregion
        # allow tree_pipes, tree_nodes, tree_LoopPipes, and tree_Loops to respond to delete key
        if event.type() == qtc.QEvent.KeyPress:
            if event.key() == qtc.Qt.Key_Delete:
                if obj == self.tree_Pipes:
                    self.deletePipe()
                elif obj == self.tree_Nodes:
                    self.deleteNode()
                elif obj == self.tree_LoopPipes:
                    self.deleteLoopPipe()
                elif obj == self.tree_Loops:
                    self.deleteLoop()

        # pass the event along to the parent widget if there is one.
        return super(MainWindow, self).eventFilter(obj, event)

    #region $NEW$ functions associated with the drawing
    def setupGraphicsView(self):
        #create a scene object
        self.scene = qtw.QGraphicsScene()
        self.scene.setObjectName("MyScene")
        self.scene.setSceneRect(-200, -200, 400, 400)  # xLeft, yTop, Width, Height
        self.scene.installEventFilter(self) #install the event filter for use in mouse tracking
        self.setMouseTracking(True)
        self.gb_GraphicView.setMouseTracking(True)
        self.gv_Main.setMouseTracking(True)

        #set the scene for the graphics view object
        self.gv_Main.setScene(self.scene)
        #make some pens and brushes for my drawing
        self.setupPensAndBrushes()

    def setupPensAndBrushes(self):
        #make the pens first
        #a thick darkGray pen
        self.penPipe = qtg.QPen(qtc.Qt.darkGray)
        self.penPipe.setStyle(qtc.Qt.SolidLine)
        self.penPipe.setWidth(4)
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

    def drawAGrid(self, DeltaX=10, DeltaY=10, Height=200, Width=200, CenterX=0, CenterY=0, Pen=None, Brush=None):
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

    def buildScene(self):
        #clear out the old scene first
        self.scene.clear()

        #draw a grid
        self.drawAGrid(DeltaX=10, DeltaY=10, Height=400, Width=400, Pen=self.penGridLines, Brush=self.brushGrid)

        #draw the pipe network
        self.View.drawPipes(PN=self.Model, scene=self.scene, penPipe=self.penPipe, brushPipe=self.brushFill)
        self.View.drawNodes(PN=self.Model, scene=self.scene, penNode=self.penNode, brushNode=self.brushNode)
        self.View.drawLoopLabels(PN=self.Model, pen=self.penNode, scene=self.scene)
        self.View.drawNodeExtFlows(PN=self.Model, pen=self.penNode, brush=self.brushNode, scene=self.scene)

    def setZoom(self):
        self.gv_Main.resetTransform()
        self.gv_Main.scale(self.spnd_Zoom.value(), self.spnd_Zoom.value())
    #endregion

    #region Functions that act as Slots
    def readPipeNetworkFile(self):
        """
        Read the information from a pipe network file.
        :return:
        """
        # open the file dialog box to search for the file I want
        filename = qtw.QFileDialog.getOpenFileName()[0]
        if len(filename) == 0:  # no file selected
            return
        self.le_FileName.setText(filename)  # echo the filename on the GUI
        file = open(filename, 'r')  # open the file
        data = file.readlines()  # read all the lines of the file into a list of strings
        self.Controller.importPipeNetwork(data, PN=self.Model)  # import the pipe network information
        self.updateView()  # update the view of the model
        pass

    def savePipeNetworkFile(self):
        """
        Read the information from a pipe network file.
        :return:
        """
        # open the file dialog box to search for the file I want
        dlg=qtw.QFileDialog(directory=self.le_FileName.text())
        filename = dlg.getSaveFileName()[0]
        if len(filename) == 0:  # no file selected
            return
        else:
            self.View.getPipeNetworkOutputForFileSortedUsingNodes(filename=filename, PN=self.Model, treeP=self.tree_Pipes, treeN=self.tree_Nodes, treeL=self.tree_Loops)

    def updateNodesTree(self):
        self.View.updateNodeTree(self.tree_Nodes,PN=self.Model)

    def addPipeToPipeList(self):
        """
        I use this as the slot for the clicked signal of the Add Pipe button.  It reads from the
        line edit boxes and creates a top level QTreeWidgetItem and places it in the tree_Pipes widget.
        :return: none
        """
        node1 = self.le_StartNode.text()  # read from GUI
        node2 = self.le_EndNodeName.text()  # read from GUI
        name = '{}-{}'.format(min(node1, node2), max(node1, node2))  # follow alphabetical naming convention
        length = self.le_PipeLength.text()  # read from GUI
        diam = str(float(self.le_Diam.text())/1000.0)  # read from GUI
        rough = self.le_Roughness.text()  # read from GUI
        itm = qtw.QTreeWidgetItem((name, length, diam, rough))
        self.Controller.addPipe(itm, PN=self.Model)  # part of the controller that updates the model with changes on the view
        self.View.updatePipeTree(self.tree_Pipes,self.Model)
        self.updateNodesTree()  #$NEW$ 4/6/21 added this and next line to update nodetree if a new pipe with a new node is added
        self.buildScene()

    def modifyPipe(self, item, col):
        self.Controller.modifyPipe(item, col, PN=self.Model)
        self.updateNodesTree()  #$NEW$ 4/6/21 catches changes to the model if nodes get changed
        self.buildScene()

    def modifyNode(self, item, col):
        self.Controller.modifyNode(item, col, PN=self.Model)
        self.buildScene()

    def modifyLoop(self, item, col):
        self.Controller.modifyLoop(item, col, PN=self.Model)


    def deletePipe(self):
        """
        This is the slot for the clicked signal of the Delete Pipe button as well as the response to the delete
        key being pressed when in the tree_Pipe widget.  This latter behavior is implemented with the eventFilter
        method that is installed on the tree_Pipe widget.
        :return: none
        """
        index = self.tree_Pipes.currentIndex().row()
        self.Controller.deletePipe(self.tree_Pipes.takeTopLevelItem(index), PN=self.Model)
        self.updateNodesTree()  #$NEW$ 4/6/21 removes any nodes that are no longer in use
        self.buildScene()

    def deleteNode(self):
        index = self.tree_Nodes.currentIndex().row()
        self.Controller.deleteNode(self.tree_Nodes.takeTopLevelItem(index), PN=self.Model)
        self.updateNodesTree()
        self.buildScene()

    def deleteLoopPipe(self):
        """
        This is the response to the delete
        key being pressed when in the tree_LoopPipes widget.  It implemented with the eventFilter
        method that is installed on the tree_LoopPipe widget.
        :return:
        """
        index = self.tree_LoopPipes.currentIndex().row()
        self.tree_LoopPipes.takeTopLevelItem(index)

    def deleteLoop(self):
        """
        This is the response to the delete
        key being pressed when in the tree_Loops widget.  It implemented with the eventFilter
        method that is installed on the tree_Loops widget.
        :return:
        """
        isParent = self.tree_Loops.currentItem().parent() is None
        itm = self.tree_Loops.currentItem()
        index = self.tree_Loops.currentIndex().row()
        if isParent:
            self.Controller.deleteLoop(self.tree_Loops.takeTopLevelItem(index), PN=self.Model)
        else:
            parent = self.tree_Loops.currentItem().parent()
            self.tree_Loops.currentItem().parent().removeChild(itm)
            self.PND.modifyLoop(parent, 0, PN=self.Model)

    def addPipeToLoop(self):
        """
        I use this as the slot for the clicked signal of the Add Pipe to loop button.  It reads from the
        tree_Pipes widget and creates a top level QTreeWidgetItem and places it in the tree_LoopPipes widget.
        :return: none
        """
        for p in self.tree_Pipes.selectedItems():
            name = p.text(0)
            rows = str(self.tree_LoopPipes.topLevelItemCount())
            itm = qtw.QTreeWidgetItem((rows, name))
            itm.setFlags(qtc.Qt.ItemIsSelectable | qtc.Qt.ItemIsEditable | qtc.Qt.ItemIsDragEnabled | qtc.Qt.ItemIsUserCheckable | qtc.Qt.ItemIsEnabled)
            self.tree_LoopPipes.addTopLevelItem(itm)
        rows = self.tree_LoopPipes.topLevelItemCount()

    def createLoop(self):
        """
        This is the slot for the clicked signal of btn_CreateLoop.  It reads from the tree_LoopPipes and builds
        the hierarchy of a loop object and adds it to the tree_Loops widget.
        :return:
        """
        loopName = [self.le_LoopName.text()]
        pipes = []
        while self.tree_LoopPipes.topLevelItemCount() > 0:
            pipe = self.tree_LoopPipes.takeTopLevelItem(0)
            pipes.append([pipe.text(1)])
        loop = qtw.QTreeWidgetItem(loopName)
        loop.setFlags(qtc.Qt.ItemIsSelectable | qtc.Qt.ItemIsEditable | qtc.Qt.ItemIsDragEnabled | qtc.Qt.ItemIsUserCheckable | qtc.Qt.ItemIsEnabled)
        for p in pipes:
            itm = qtw.QTreeWidgetItem(p)
            itm.setFlags(qtc.Qt.ItemIsSelectable | qtc.Qt.ItemIsEditable | qtc.Qt.ItemIsDragEnabled | qtc.Qt.ItemIsUserCheckable | qtc.Qt.ItemIsEnabled)
            loop.addChild(itm)
        self.tree_Loops.addTopLevelItem(loop)
        self.Controller.addLoop(loop, PN=self.Model)

    def EvaluatePipeNetwork(self):
        """
        Use the Pipe Network object to evaluate the pipe network and display output
        :return:
        """
        self.Model.findFlowRates()
        self.Model.setMinNodePressureHead(minPH=2, calcK=True)
        # show output
        #self.View.getPipeFlowRatesOutput(tabs='\t', PN=self.Model, lbl=self.lbl_FlowRates)
        self.View.getPipeFlowRatesOutputSorted(tabs='\t', PN=self.Model, lbl=self.lbl_FlowRates, tree=self.tree_Pipes)
        self.View.getPipeHeadLossesOutputSorted(tabs='\t', PN=self.Model, lbl=self.lbl_PipeHeadLosses, tree=self.tree_Pipes)
        self.View.getNodeHeadOutputSorted(tabs='\t', PN=self.Model, lbl=self.lbl_NodePressures, tree=self.tree_Nodes)
        self.View.getRealityCheckOutputSorted(tabs='\t', PN=self.Model, lbl=self.lbl_PressureAndFlowChecks, treeN=self.tree_Nodes, treeL=self.tree_Loops)
        return None
    #endregion

    def fitColumns(self):  # $NEW$ 4/6/21
        """
        this functions sizes the colums of the trees
        :return:
        """
        for i in range(self.tree_Pipes.columnCount()):
            self.tree_Pipes.resizeColumnToContents(i)
        for i in range(self.tree_Nodes.columnCount()):
            self.tree_Nodes.resizeColumnToContents(i)
        for i in range(self.tree_LoopPipes.columnCount()):
            self.tree_LoopPipes.resizeColumnToContents(i)
        for i in range(self.tree_Loops.columnCount()):
            self.tree_Loops.resizeColumnToContents(i)

    def updateView(self):
        """
        Update the representation of the model in the tree Widgets
        :return:
        """
        self.buildScene() #$NEW$ 4/6/21 call to draw the pipe network
        self.tree_LoopPipes.clear()
        # update the pipe tree
        self.View.updatePipeTree(self.tree_Pipes, PN=self.Model)
        #update the node tree
        self.View.updateNodeTree(self.tree_Nodes, PN=self.Model)
        #update the loop tree
        self.View.updateLoopTree(self.tree_Loops, PN=self.Model)
        self.fitColumns()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('Rankine Cycle Calculator')
    sys.exit(app.exec())
