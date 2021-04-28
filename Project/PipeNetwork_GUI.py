# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PipeNetwork_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2378, 791)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        Form.setMouseTracking(True)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.grp_PipeNetworkBuilder = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_PipeNetworkBuilder.sizePolicy().hasHeightForWidth())
        self.grp_PipeNetworkBuilder.setSizePolicy(sizePolicy)
        self.grp_PipeNetworkBuilder.setMouseTracking(True)
        self.grp_PipeNetworkBuilder.setObjectName("grp_PipeNetworkBuilder")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.grp_PipeNetworkBuilder)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.grp_PipeAndNodeCreation = QtWidgets.QGroupBox(self.grp_PipeNetworkBuilder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_PipeAndNodeCreation.sizePolicy().hasHeightForWidth())
        self.grp_PipeAndNodeCreation.setSizePolicy(sizePolicy)
        self.grp_PipeAndNodeCreation.setMouseTracking(True)
        self.grp_PipeAndNodeCreation.setObjectName("grp_PipeAndNodeCreation")
        self.gridLayout = QtWidgets.QGridLayout(self.grp_PipeAndNodeCreation)
        self.gridLayout.setObjectName("gridLayout")
        self.le_PipeLength = QtWidgets.QLineEdit(self.grp_PipeAndNodeCreation)
        self.le_PipeLength.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_PipeLength.sizePolicy().hasHeightForWidth())
        self.le_PipeLength.setSizePolicy(sizePolicy)
        self.le_PipeLength.setMinimumSize(QtCore.QSize(80, 0))
        self.le_PipeLength.setMaximumSize(QtCore.QSize(150, 16777215))
        self.le_PipeLength.setObjectName("le_PipeLength")
        self.gridLayout.addWidget(self.le_PipeLength, 5, 1, 1, 1)
        self.le_Diam = QtWidgets.QLineEdit(self.grp_PipeAndNodeCreation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_Diam.sizePolicy().hasHeightForWidth())
        self.le_Diam.setSizePolicy(sizePolicy)
        self.le_Diam.setMinimumSize(QtCore.QSize(80, 0))
        self.le_Diam.setMaximumSize(QtCore.QSize(150, 16777215))
        self.le_Diam.setObjectName("le_Diam")
        self.gridLayout.addWidget(self.le_Diam, 6, 1, 1, 1)
        self.metric_rbtn = QtWidgets.QRadioButton(self.grp_PipeAndNodeCreation)
        self.metric_rbtn.setObjectName("metric_rbtn")
        self.gridLayout.addWidget(self.metric_rbtn, 10, 0, 1, 1)
        self.lbl_EndNodeName_4 = QtWidgets.QLabel(self.grp_PipeAndNodeCreation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_EndNodeName_4.sizePolicy().hasHeightForWidth())
        self.lbl_EndNodeName_4.setSizePolicy(sizePolicy)
        self.lbl_EndNodeName_4.setMinimumSize(QtCore.QSize(170, 0))
        self.lbl_EndNodeName_4.setMaximumSize(QtCore.QSize(185, 16777215))
        self.lbl_EndNodeName_4.setObjectName("lbl_EndNodeName_4")
        self.gridLayout.addWidget(self.lbl_EndNodeName_4, 7, 0, 1, 1)
        self.lbl_StartNode = QtWidgets.QLabel(self.grp_PipeAndNodeCreation)
        self.lbl_StartNode.setMinimumSize(QtCore.QSize(170, 0))
        self.lbl_StartNode.setMaximumSize(QtCore.QSize(185, 16777215))
        self.lbl_StartNode.setObjectName("lbl_StartNode")
        self.gridLayout.addWidget(self.lbl_StartNode, 3, 0, 1, 1)
        self.le_Roughness = QtWidgets.QLineEdit(self.grp_PipeAndNodeCreation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_Roughness.sizePolicy().hasHeightForWidth())
        self.le_Roughness.setSizePolicy(sizePolicy)
        self.le_Roughness.setMinimumSize(QtCore.QSize(80, 0))
        self.le_Roughness.setMaximumSize(QtCore.QSize(150, 16777215))
        self.le_Roughness.setObjectName("le_Roughness")
        self.gridLayout.addWidget(self.le_Roughness, 7, 1, 1, 1)
        self.btn_OpenPipeNetworkFile = QtWidgets.QPushButton(self.grp_PipeAndNodeCreation)
        self.btn_OpenPipeNetworkFile.setMinimumSize(QtCore.QSize(285, 0))
        self.btn_OpenPipeNetworkFile.setMaximumSize(QtCore.QSize(285, 16777215))
        self.btn_OpenPipeNetworkFile.setObjectName("btn_OpenPipeNetworkFile")
        self.gridLayout.addWidget(self.btn_OpenPipeNetworkFile, 0, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tree_Pipes = QtWidgets.QTreeWidget(self.grp_PipeAndNodeCreation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_Pipes.sizePolicy().hasHeightForWidth())
        self.tree_Pipes.setSizePolicy(sizePolicy)
        self.tree_Pipes.setMinimumSize(QtCore.QSize(650, 0))
        self.tree_Pipes.setMaximumSize(QtCore.QSize(800, 50000))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_Pipes.setFont(font)
        self.tree_Pipes.setMouseTracking(False)
        self.tree_Pipes.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tree_Pipes.setProperty("showDropIndicator", False)
        self.tree_Pipes.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tree_Pipes.setAllColumnsShowFocus(True)
        self.tree_Pipes.setWordWrap(False)
        self.tree_Pipes.setHeaderHidden(False)
        self.tree_Pipes.setObjectName("tree_Pipes")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_Pipes.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_Pipes.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_Pipes.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_Pipes.headerItem().setFont(3, font)
        self.tree_Pipes.header().setDefaultSectionSize(100)
        self.tree_Pipes.header().setMinimumSectionSize(35)
        self.verticalLayout_2.addWidget(self.tree_Pipes)
        self.tree_Nodes = QtWidgets.QTreeWidget(self.grp_PipeAndNodeCreation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_Nodes.sizePolicy().hasHeightForWidth())
        self.tree_Nodes.setSizePolicy(sizePolicy)
        self.tree_Nodes.setMinimumSize(QtCore.QSize(800, 0))
        self.tree_Nodes.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_Nodes.setFont(font)
        self.tree_Nodes.setMouseTracking(True)
        self.tree_Nodes.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tree_Nodes.setObjectName("tree_Nodes")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_Nodes.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_Nodes.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_Nodes.headerItem().setFont(5, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_Nodes.headerItem().setFont(6, font)
        self.tree_Nodes.header().setDefaultSectionSize(55)
        self.tree_Nodes.header().setMinimumSectionSize(25)
        self.verticalLayout_2.addWidget(self.tree_Nodes)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 2, 9, 1)
        self.lbl_EndNodeName = QtWidgets.QLabel(self.grp_PipeAndNodeCreation)
        self.lbl_EndNodeName.setMinimumSize(QtCore.QSize(170, 0))
        self.lbl_EndNodeName.setMaximumSize(QtCore.QSize(185, 16777215))
        self.lbl_EndNodeName.setObjectName("lbl_EndNodeName")
        self.gridLayout.addWidget(self.lbl_EndNodeName, 4, 0, 1, 1)
        self.btn_SavePipeNetworkFile = QtWidgets.QPushButton(self.grp_PipeAndNodeCreation)
        self.btn_SavePipeNetworkFile.setMaximumSize(QtCore.QSize(285, 16777215))
        self.btn_SavePipeNetworkFile.setObjectName("btn_SavePipeNetworkFile")
        self.gridLayout.addWidget(self.btn_SavePipeNetworkFile, 2, 0, 1, 2)
        self.lbl_EndNodeName_3 = QtWidgets.QLabel(self.grp_PipeAndNodeCreation)
        self.lbl_EndNodeName_3.setMinimumSize(QtCore.QSize(170, 0))
        self.lbl_EndNodeName_3.setMaximumSize(QtCore.QSize(185, 16777215))
        self.lbl_EndNodeName_3.setObjectName("lbl_EndNodeName_3")
        self.gridLayout.addWidget(self.lbl_EndNodeName_3, 6, 0, 1, 1)
        self.le_StartNode = QtWidgets.QLineEdit(self.grp_PipeAndNodeCreation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_StartNode.sizePolicy().hasHeightForWidth())
        self.le_StartNode.setSizePolicy(sizePolicy)
        self.le_StartNode.setMinimumSize(QtCore.QSize(80, 0))
        self.le_StartNode.setMaximumSize(QtCore.QSize(150, 16777215))
        self.le_StartNode.setObjectName("le_StartNode")
        self.gridLayout.addWidget(self.le_StartNode, 3, 1, 1, 1)
        self.english_rbtn = QtWidgets.QRadioButton(self.grp_PipeAndNodeCreation)
        self.english_rbtn.setObjectName("english_rbtn")
        self.gridLayout.addWidget(self.english_rbtn, 10, 1, 1, 1)
        self.lbl_EndNodeName_2 = QtWidgets.QLabel(self.grp_PipeAndNodeCreation)
        self.lbl_EndNodeName_2.setEnabled(False)
        self.lbl_EndNodeName_2.setMinimumSize(QtCore.QSize(170, 0))
        self.lbl_EndNodeName_2.setMaximumSize(QtCore.QSize(185, 16777215))
        self.lbl_EndNodeName_2.setObjectName("lbl_EndNodeName_2")
        self.gridLayout.addWidget(self.lbl_EndNodeName_2, 5, 0, 1, 1)
        self.le_FileName = QtWidgets.QLineEdit(self.grp_PipeAndNodeCreation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_FileName.sizePolicy().hasHeightForWidth())
        self.le_FileName.setSizePolicy(sizePolicy)
        self.le_FileName.setMaximumSize(QtCore.QSize(800, 16777215))
        self.le_FileName.setObjectName("le_FileName")
        self.gridLayout.addWidget(self.le_FileName, 0, 2, 1, 1)
        self.btn_AddPipe = QtWidgets.QPushButton(self.grp_PipeAndNodeCreation)
        self.btn_AddPipe.setMaximumSize(QtCore.QSize(185, 16777215))
        self.btn_AddPipe.setObjectName("btn_AddPipe")
        self.gridLayout.addWidget(self.btn_AddPipe, 8, 1, 1, 1)
        self.btn_DeletePipe = QtWidgets.QPushButton(self.grp_PipeAndNodeCreation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_DeletePipe.sizePolicy().hasHeightForWidth())
        self.btn_DeletePipe.setSizePolicy(sizePolicy)
        self.btn_DeletePipe.setMinimumSize(QtCore.QSize(170, 0))
        self.btn_DeletePipe.setMaximumSize(QtCore.QSize(185, 16777215))
        self.btn_DeletePipe.setObjectName("btn_DeletePipe")
        self.gridLayout.addWidget(self.btn_DeletePipe, 8, 0, 1, 1)
        self.le_EndNodeName = QtWidgets.QLineEdit(self.grp_PipeAndNodeCreation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_EndNodeName.sizePolicy().hasHeightForWidth())
        self.le_EndNodeName.setSizePolicy(sizePolicy)
        self.le_EndNodeName.setMinimumSize(QtCore.QSize(80, 0))
        self.le_EndNodeName.setMaximumSize(QtCore.QSize(150, 16777215))
        self.le_EndNodeName.setObjectName("le_EndNodeName")
        self.gridLayout.addWidget(self.le_EndNodeName, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.grp_PipeAndNodeCreation)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 9, 0, 1, 1)
        self.horizontalLayout.addWidget(self.grp_PipeAndNodeCreation)
        self.groupBox_4 = QtWidgets.QGroupBox(self.grp_PipeNetworkBuilder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_CreateLoop = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_CreateLoop.sizePolicy().hasHeightForWidth())
        self.btn_CreateLoop.setSizePolicy(sizePolicy)
        self.btn_CreateLoop.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_CreateLoop.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_CreateLoop.setObjectName("btn_CreateLoop")
        self.gridLayout_2.addWidget(self.btn_CreateLoop, 2, 1, 1, 1)
        self.le_LoopName = QtWidgets.QLineEdit(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_LoopName.sizePolicy().hasHeightForWidth())
        self.le_LoopName.setSizePolicy(sizePolicy)
        self.le_LoopName.setMinimumSize(QtCore.QSize(120, 0))
        self.le_LoopName.setMaximumSize(QtCore.QSize(130, 16777215))
        self.le_LoopName.setBaseSize(QtCore.QSize(0, 0))
        self.le_LoopName.setObjectName("le_LoopName")
        self.gridLayout_2.addWidget(self.le_LoopName, 0, 1, 1, 1)
        self.lbl_LoopName = QtWidgets.QLabel(self.groupBox_4)
        self.lbl_LoopName.setMinimumSize(QtCore.QSize(120, 0))
        self.lbl_LoopName.setMaximumSize(QtCore.QSize(125, 16777215))
        self.lbl_LoopName.setObjectName("lbl_LoopName")
        self.gridLayout_2.addWidget(self.lbl_LoopName, 0, 0, 1, 1)
        self.btn_AddPipeToLoop = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_AddPipeToLoop.sizePolicy().hasHeightForWidth())
        self.btn_AddPipeToLoop.setSizePolicy(sizePolicy)
        self.btn_AddPipeToLoop.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_AddPipeToLoop.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_AddPipeToLoop.setObjectName("btn_AddPipeToLoop")
        self.gridLayout_2.addWidget(self.btn_AddPipeToLoop, 1, 1, 1, 1)
        self.tree_Loops = QtWidgets.QTreeWidget(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_Loops.sizePolicy().hasHeightForWidth())
        self.tree_Loops.setSizePolicy(sizePolicy)
        self.tree_Loops.setMinimumSize(QtCore.QSize(100, 0))
        self.tree_Loops.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_Loops.setFont(font)
        self.tree_Loops.setToolTipDuration(0)
        self.tree_Loops.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tree_Loops.setLineWidth(3)
        self.tree_Loops.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tree_Loops.setObjectName("tree_Loops")
        self.tree_Loops.headerItem().setText(0, "Loops")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_Loops.headerItem().setFont(0, font)
        self.tree_Loops.header().setDefaultSectionSize(75)
        self.gridLayout_2.addWidget(self.tree_Loops, 0, 2, 5, 1)
        self.tree_LoopPipes = QtWidgets.QTreeWidget(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_LoopPipes.sizePolicy().hasHeightForWidth())
        self.tree_LoopPipes.setSizePolicy(sizePolicy)
        self.tree_LoopPipes.setMinimumSize(QtCore.QSize(200, 0))
        self.tree_LoopPipes.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_LoopPipes.setFont(font)
        self.tree_LoopPipes.setToolTipDuration(0)
        self.tree_LoopPipes.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tree_LoopPipes.setObjectName("tree_LoopPipes")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_LoopPipes.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tree_LoopPipes.headerItem().setFont(1, font)
        self.tree_LoopPipes.header().setDefaultSectionSize(70)
        self.tree_LoopPipes.header().setMinimumSectionSize(25)
        self.gridLayout_2.addWidget(self.tree_LoopPipes, 3, 0, 2, 2)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.verticalLayout.addWidget(self.grp_PipeNetworkBuilder)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.grid_Feedback = QtWidgets.QGridLayout()
        self.grid_Feedback.setObjectName("grid_Feedback")
        self.lbl_FlowRates = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_FlowRates.sizePolicy().hasHeightForWidth())
        self.lbl_FlowRates.setSizePolicy(sizePolicy)
        self.lbl_FlowRates.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_FlowRates.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbl_FlowRates.setLineWidth(3)
        self.lbl_FlowRates.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_FlowRates.setObjectName("lbl_FlowRates")
        self.grid_Feedback.addWidget(self.lbl_FlowRates, 0, 1, 1, 1)
        self.lbl_PressureAndFlowChecks = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_PressureAndFlowChecks.sizePolicy().hasHeightForWidth())
        self.lbl_PressureAndFlowChecks.setSizePolicy(sizePolicy)
        self.lbl_PressureAndFlowChecks.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_PressureAndFlowChecks.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbl_PressureAndFlowChecks.setLineWidth(3)
        self.lbl_PressureAndFlowChecks.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_PressureAndFlowChecks.setObjectName("lbl_PressureAndFlowChecks")
        self.grid_Feedback.addWidget(self.lbl_PressureAndFlowChecks, 0, 4, 1, 1)
        self.lbl_NodePressures = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_NodePressures.sizePolicy().hasHeightForWidth())
        self.lbl_NodePressures.setSizePolicy(sizePolicy)
        self.lbl_NodePressures.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_NodePressures.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbl_NodePressures.setLineWidth(3)
        self.lbl_NodePressures.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_NodePressures.setObjectName("lbl_NodePressures")
        self.grid_Feedback.addWidget(self.lbl_NodePressures, 0, 3, 1, 1)
        self.lbl_PipeHeadLosses = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_PipeHeadLosses.sizePolicy().hasHeightForWidth())
        self.lbl_PipeHeadLosses.setSizePolicy(sizePolicy)
        self.lbl_PipeHeadLosses.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_PipeHeadLosses.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbl_PipeHeadLosses.setLineWidth(3)
        self.lbl_PipeHeadLosses.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_PipeHeadLosses.setObjectName("lbl_PipeHeadLosses")
        self.grid_Feedback.addWidget(self.lbl_PipeHeadLosses, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_Feedback.addItem(spacerItem, 0, 5, 1, 1)
        self.gridLayout_3.addLayout(self.grid_Feedback, 1, 0, 1, 1)
        self.btn_Evaluate = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Evaluate.sizePolicy().hasHeightForWidth())
        self.btn_Evaluate.setSizePolicy(sizePolicy)
        self.btn_Evaluate.setObjectName("btn_Evaluate")
        self.gridLayout_3.addWidget(self.btn_Evaluate, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gb_GraphicView = QtWidgets.QGroupBox(Form)
        self.gb_GraphicView.setMouseTracking(True)
        self.gb_GraphicView.setObjectName("gb_GraphicView")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gb_GraphicView)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lbl_MousePosition = QtWidgets.QLabel(self.gb_GraphicView)
        self.lbl_MousePosition.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_MousePosition.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbl_MousePosition.setLineWidth(1)
        self.lbl_MousePosition.setObjectName("lbl_MousePosition")
        self.gridLayout_4.addWidget(self.lbl_MousePosition, 1, 0, 1, 1)
        self.gv_Main = QtWidgets.QGraphicsView(self.gb_GraphicView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gv_Main.sizePolicy().hasHeightForWidth())
        self.gv_Main.setSizePolicy(sizePolicy)
        self.gv_Main.setMinimumSize(QtCore.QSize(700, 700))
        self.gv_Main.setMouseTracking(True)
        self.gv_Main.setObjectName("gv_Main")
        self.gridLayout_4.addWidget(self.gv_Main, 0, 0, 1, 3)
        self.spnd_Zoom = QtWidgets.QDoubleSpinBox(self.gb_GraphicView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnd_Zoom.sizePolicy().hasHeightForWidth())
        self.spnd_Zoom.setSizePolicy(sizePolicy)
        self.spnd_Zoom.setSingleStep(0.5)
        self.spnd_Zoom.setProperty("value", 1.0)
        self.spnd_Zoom.setObjectName("spnd_Zoom")
        self.gridLayout_4.addWidget(self.spnd_Zoom, 1, 2, 1, 1)
        self.lbl_Zoom = QtWidgets.QLabel(self.gb_GraphicView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Zoom.sizePolicy().hasHeightForWidth())
        self.lbl_Zoom.setSizePolicy(sizePolicy)
        self.lbl_Zoom.setObjectName("lbl_Zoom")
        self.gridLayout_4.addWidget(self.lbl_Zoom, 1, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.gb_GraphicView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.le_StartNode, self.le_EndNodeName)
        Form.setTabOrder(self.le_EndNodeName, self.le_PipeLength)
        Form.setTabOrder(self.le_PipeLength, self.le_Diam)
        Form.setTabOrder(self.le_Diam, self.le_Roughness)
        Form.setTabOrder(self.le_Roughness, self.btn_AddPipe)
        Form.setTabOrder(self.btn_AddPipe, self.le_LoopName)
        Form.setTabOrder(self.le_LoopName, self.btn_AddPipeToLoop)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.grp_PipeNetworkBuilder.setTitle(_translate("Form", "Pipe Network Builder"))
        self.grp_PipeAndNodeCreation.setTitle(_translate("Form", "Pipe and Node Creation"))
        self.le_PipeLength.setText(_translate("Form", "125"))
        self.le_Diam.setText(_translate("Form", "300"))
        self.metric_rbtn.setText(_translate("Form", "Metric"))
        self.lbl_EndNodeName_4.setText(_translate("Form", "Roughness (m)"))
        self.lbl_StartNode.setText(_translate("Form", "Node 1"))
        self.le_Roughness.setText(_translate("Form", "0.00025"))
        self.btn_OpenPipeNetworkFile.setText(_translate("Form", "Open Pipe Network File"))
        self.tree_Pipes.setSortingEnabled(True)
        self.tree_Pipes.headerItem().setText(0, _translate("Form", "Name"))
        self.tree_Pipes.headerItem().setText(1, _translate("Form", "Length (m)"))
        self.tree_Pipes.headerItem().setText(2, _translate("Form", "Diam (m)"))
        self.tree_Pipes.headerItem().setText(3, _translate("Form", "Rough (m)"))
        self.tree_Nodes.setSortingEnabled(True)
        self.tree_Nodes.headerItem().setText(0, _translate("Form", "Name"))
        self.tree_Nodes.headerItem().setText(1, _translate("Form", "x"))
        self.tree_Nodes.headerItem().setText(2, _translate("Form", "y"))
        self.tree_Nodes.headerItem().setText(3, _translate("Form", "z"))
        self.tree_Nodes.headerItem().setText(4, _translate("Form", "External Flow"))
        self.tree_Nodes.headerItem().setText(5, _translate("Form", "Sprinkler?"))
        self.tree_Nodes.headerItem().setText(6, _translate("Form", "Specified P/Min P"))
        self.lbl_EndNodeName.setText(_translate("Form", "Node 2"))
        self.btn_SavePipeNetworkFile.setText(_translate("Form", "Save Pipe Network File"))
        self.lbl_EndNodeName_3.setText(_translate("Form", "Diam (mm)"))
        self.le_StartNode.setText(_translate("Form", "a"))
        self.english_rbtn.setText(_translate("Form", "English"))
        self.lbl_EndNodeName_2.setText(_translate("Form", "Length (m)"))
        self.btn_AddPipe.setText(_translate("Form", "Add Pipe"))
        self.btn_DeletePipe.setText(_translate("Form", "Delete Pipe"))
        self.le_EndNodeName.setText(_translate("Form", "b"))
        self.label.setText(_translate("Form", "Units:"))
        self.groupBox_4.setTitle(_translate("Form", "Loop Creation"))
        self.btn_CreateLoop.setText(_translate("Form", "Create Loop"))
        self.lbl_LoopName.setText(_translate("Form", "Loop Name"))
        self.btn_AddPipeToLoop.setText(_translate("Form", "Add Pipe(s)"))
        self.tree_LoopPipes.headerItem().setText(0, _translate("Form", "Item"))
        self.tree_LoopPipes.headerItem().setText(1, _translate("Form", "Pipe Name"))
        self.groupBox_2.setTitle(_translate("Form", "Output"))
        self.lbl_FlowRates.setText(_translate("Form", "Flow Rates"))
        self.lbl_PressureAndFlowChecks.setText(_translate("Form", "Pressure and Flow Checks"))
        self.lbl_NodePressures.setText(_translate("Form", "Node Pressures"))
        self.lbl_PipeHeadLosses.setText(_translate("Form", "Pipe Head Losses"))
        self.btn_Evaluate.setText(_translate("Form", "Evaluate Pipe Network"))
        self.gb_GraphicView.setTitle(_translate("Form", "Graphic View of Pipe Network"))
        self.lbl_MousePosition.setText(_translate("Form", "Mouse Position:"))
        self.lbl_Zoom.setText(_translate("Form", "Scale"))
