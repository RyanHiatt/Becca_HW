# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pump_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1131, 880)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        Form.setMouseTracking(True)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.label.setObjectName("label")
        self.input_FileName = QtWidgets.QLineEdit(self.groupBox)
        self.input_FileName.setGeometry(QtCore.QRect(120, 40, 951, 41))
        self.input_FileName.setObjectName("input_FileName")
        self.btn_Calculate = QtWidgets.QPushButton(self.groupBox)
        self.btn_Calculate.setGeometry(QtCore.QRect(120, 100, 221, 23))
        self.btn_Calculate.setObjectName("btn_Calculate")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(580, 60, 91, 16))
        self.label_6.setObjectName("label_6")
        self.output_PumpName = QtWidgets.QLineEdit(self.groupBox_2)
        self.output_PumpName.setGeometry(QtCore.QRect(180, 30, 911, 20))
        self.output_PumpName.setObjectName("output_PumpName")
        self.output_FlowUnits = QtWidgets.QLineEdit(self.groupBox_2)
        self.output_FlowUnits.setGeometry(QtCore.QRect(180, 60, 381, 20))
        self.output_FlowUnits.setObjectName("output_FlowUnits")
        self.output_HeadCoefficients = QtWidgets.QLineEdit(self.groupBox_2)
        self.output_HeadCoefficients.setGeometry(QtCore.QRect(180, 90, 911, 20))
        self.output_HeadCoefficients.setObjectName("output_HeadCoefficients")
        self.output_EfficiencyConstraints = QtWidgets.QLineEdit(self.groupBox_2)
        self.output_EfficiencyConstraints.setGeometry(QtCore.QRect(180, 120, 911, 20))
        self.output_EfficiencyConstraints.setObjectName("output_EfficiencyConstraints")
        self.output_HeadUnits = QtWidgets.QLineEdit(self.groupBox_2)
        self.output_HeadUnits.setGeometry(QtCore.QRect(670, 60, 421, 20))
        self.output_HeadUnits.setObjectName("output_HeadUnits")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(19, 149, 1071, 551))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.graph_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.graph_layout.setObjectName("graph_layout")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.label.setText(_translate("Form", "Filename"))
        self.btn_Calculate.setText(_translate("Form", "Read File and Calculate"))
        self.groupBox_2.setTitle(_translate("Form", "GroupBox"))
        self.label_2.setText(_translate("Form", "Efficiency Constraints"))
        self.label_3.setText(_translate("Form", "Pump Name"))
        self.label_4.setText(_translate("Form", "Flow Units"))
        self.label_5.setText(_translate("Form", "Head Coefficients"))
        self.label_6.setText(_translate("Form", "Head Units"))

