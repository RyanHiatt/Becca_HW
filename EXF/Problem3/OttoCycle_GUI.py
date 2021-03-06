# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OttoCycle_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1081, 1041)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.main_VerticalLayout = QtWidgets.QVBoxLayout(Form)
        self.main_VerticalLayout.setObjectName("main_VerticalLayout")
        self.gb_Input = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_Input.sizePolicy().hasHeightForWidth())
        self.gb_Input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gb_Input.setFont(font)
        self.gb_Input.setObjectName("gb_Input")
        self.gridLayout = QtWidgets.QGridLayout(self.gb_Input)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_PHigh = QtWidgets.QLabel(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_PHigh.sizePolicy().hasHeightForWidth())
        self.lbl_PHigh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_PHigh.setFont(font)
        self.lbl_PHigh.setObjectName("lbl_PHigh")
        self.gridLayout.addWidget(self.lbl_PHigh, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.input_InitialTemperature = QtWidgets.QLineEdit(self.gb_Input)
        self.input_InitialTemperature.setMinimumSize(QtCore.QSize(167, 0))
        self.input_InitialTemperature.setObjectName("input_InitialTemperature")
        self.gridLayout.addWidget(self.input_InitialTemperature, 3, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.rdo_Metric = QtWidgets.QRadioButton(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdo_Metric.sizePolicy().hasHeightForWidth())
        self.rdo_Metric.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdo_Metric.setFont(font)
        self.rdo_Metric.setChecked(True)
        self.rdo_Metric.setObjectName("rdo_Metric")
        self.gridLayout.addWidget(self.rdo_Metric, 2, 3, 1, 1)
        self.input_CylinderVolume = QtWidgets.QLineEdit(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_CylinderVolume.sizePolicy().hasHeightForWidth())
        self.input_CylinderVolume.setSizePolicy(sizePolicy)
        self.input_CylinderVolume.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_CylinderVolume.setFont(font)
        self.input_CylinderVolume.setClearButtonEnabled(True)
        self.input_CylinderVolume.setObjectName("input_CylinderVolume")
        self.gridLayout.addWidget(self.input_CylinderVolume, 0, 1, 1, 1)
        self.btn_Calculate = QtWidgets.QPushButton(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Calculate.sizePolicy().hasHeightForWidth())
        self.btn_Calculate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Calculate.setFont(font)
        self.btn_Calculate.setObjectName("btn_Calculate")
        self.gridLayout.addWidget(self.btn_Calculate, 0, 3, 2, 2)
        self.lbl_TurbineInletCondition = QtWidgets.QLabel(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_TurbineInletCondition.sizePolicy().hasHeightForWidth())
        self.lbl_TurbineInletCondition.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_TurbineInletCondition.setFont(font)
        self.lbl_TurbineInletCondition.setObjectName("lbl_TurbineInletCondition")
        self.gridLayout.addWidget(self.lbl_TurbineInletCondition, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.input_CompressionRatio = QtWidgets.QLineEdit(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_CompressionRatio.sizePolicy().hasHeightForWidth())
        self.input_CompressionRatio.setSizePolicy(sizePolicy)
        self.input_CompressionRatio.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_CompressionRatio.setFont(font)
        self.input_CompressionRatio.setClearButtonEnabled(True)
        self.input_CompressionRatio.setObjectName("input_CompressionRatio")
        self.gridLayout.addWidget(self.input_CompressionRatio, 2, 1, 1, 1)
        self.lbl_PLow = QtWidgets.QLabel(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_PLow.sizePolicy().hasHeightForWidth())
        self.lbl_PLow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_PLow.setFont(font)
        self.lbl_PLow.setObjectName("lbl_PLow")
        self.gridLayout.addWidget(self.lbl_PLow, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label = QtWidgets.QLabel(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.input_MaximumTemperature = QtWidgets.QLineEdit(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_MaximumTemperature.sizePolicy().hasHeightForWidth())
        self.input_MaximumTemperature.setSizePolicy(sizePolicy)
        self.input_MaximumTemperature.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_MaximumTemperature.setFont(font)
        self.input_MaximumTemperature.setClearButtonEnabled(True)
        self.input_MaximumTemperature.setObjectName("input_MaximumTemperature")
        self.gridLayout.addWidget(self.input_MaximumTemperature, 5, 1, 1, 1)
        self.units_initial_pressure = QtWidgets.QLabel(self.gb_Input)
        self.units_initial_pressure.setObjectName("units_initial_pressure")
        self.gridLayout.addWidget(self.units_initial_pressure, 1, 2, 1, 1)
        self.units_cylinder_volume = QtWidgets.QLabel(self.gb_Input)
        self.units_cylinder_volume.setObjectName("units_cylinder_volume")
        self.gridLayout.addWidget(self.units_cylinder_volume, 0, 2, 1, 1)
        self.units_initial_temp = QtWidgets.QLabel(self.gb_Input)
        self.units_initial_temp.setObjectName("units_initial_temp")
        self.gridLayout.addWidget(self.units_initial_temp, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 5, 1, 1)
        self.rdo_English = QtWidgets.QRadioButton(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdo_English.sizePolicy().hasHeightForWidth())
        self.rdo_English.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdo_English.setFont(font)
        self.rdo_English.setObjectName("rdo_English")
        self.gridLayout.addWidget(self.rdo_English, 2, 4, 1, 1)
        self.units_max_temp = QtWidgets.QLabel(self.gb_Input)
        self.units_max_temp.setObjectName("units_max_temp")
        self.gridLayout.addWidget(self.units_max_temp, 5, 2, 1, 1)
        self.input_InitialPressure = QtWidgets.QLineEdit(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_InitialPressure.sizePolicy().hasHeightForWidth())
        self.input_InitialPressure.setSizePolicy(sizePolicy)
        self.input_InitialPressure.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_InitialPressure.setFont(font)
        self.input_InitialPressure.setClearButtonEnabled(True)
        self.input_InitialPressure.setObjectName("input_InitialPressure")
        self.gridLayout.addWidget(self.input_InitialPressure, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gb_Input)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1)
        self.main_VerticalLayout.addWidget(self.gb_Input)
        self.gb_Output = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_Output.sizePolicy().hasHeightForWidth())
        self.gb_Output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gb_Output.setFont(font)
        self.gb_Output.setObjectName("gb_Output")
        self.grid_Output = QtWidgets.QGridLayout(self.gb_Output)
        self.grid_Output.setObjectName("grid_Output")
        self.label_t3 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_t3.sizePolicy().hasHeightForWidth())
        self.label_t3.setSizePolicy(sizePolicy)
        self.label_t3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_t3.setFont(font)
        self.label_t3.setObjectName("label_t3")
        self.grid_Output.addWidget(self.label_t3, 0, 6, 1, 1)
        self.label_t4 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_t4.sizePolicy().hasHeightForWidth())
        self.label_t4.setSizePolicy(sizePolicy)
        self.label_t4.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_t4.setFont(font)
        self.label_t4.setObjectName("label_t4")
        self.grid_Output.addWidget(self.label_t4, 1, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_Output.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_Output.addItem(spacerItem2, 0, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.grid_Output.addWidget(self.label_12, 0, 10, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.grid_Output.addWidget(self.label_5, 1, 0, 1, 1)
        self.output_CycleEfficiency = QtWidgets.QLineEdit(self.gb_Output)
        self.output_CycleEfficiency.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_CycleEfficiency.sizePolicy().hasHeightForWidth())
        self.output_CycleEfficiency.setSizePolicy(sizePolicy)
        self.output_CycleEfficiency.setMinimumSize(QtCore.QSize(0, 0))
        self.output_CycleEfficiency.setMaximumSize(QtCore.QSize(200, 16777215))
        self.output_CycleEfficiency.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output_CycleEfficiency.setFont(font)
        self.output_CycleEfficiency.setObjectName("output_CycleEfficiency")
        self.grid_Output.addWidget(self.output_CycleEfficiency, 0, 9, 1, 1)
        self.output_T2 = QtWidgets.QLineEdit(self.gb_Output)
        self.output_T2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_T2.sizePolicy().hasHeightForWidth())
        self.output_T2.setSizePolicy(sizePolicy)
        self.output_T2.setMinimumSize(QtCore.QSize(0, 0))
        self.output_T2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.output_T2.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output_T2.setFont(font)
        self.output_T2.setObjectName("output_T2")
        self.grid_Output.addWidget(self.output_T2, 1, 1, 1, 1)
        self.output_T4 = QtWidgets.QLineEdit(self.gb_Output)
        self.output_T4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_T4.sizePolicy().hasHeightForWidth())
        self.output_T4.setSizePolicy(sizePolicy)
        self.output_T4.setMinimumSize(QtCore.QSize(0, 0))
        self.output_T4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.output_T4.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output_T4.setFont(font)
        self.output_T4.setObjectName("output_T4")
        self.grid_Output.addWidget(self.output_T4, 1, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.grid_Output.addWidget(self.label_9, 0, 4, 1, 1)
        self.label_t1 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_t1.sizePolicy().hasHeightForWidth())
        self.label_t1.setSizePolicy(sizePolicy)
        self.label_t1.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_t1.setFont(font)
        self.label_t1.setObjectName("label_t1")
        self.grid_Output.addWidget(self.label_t1, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.grid_Output.addWidget(self.label_10, 0, 7, 1, 1)
        self.output_T1 = QtWidgets.QLineEdit(self.gb_Output)
        self.output_T1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_T1.sizePolicy().hasHeightForWidth())
        self.output_T1.setSizePolicy(sizePolicy)
        self.output_T1.setMinimumSize(QtCore.QSize(0, 0))
        self.output_T1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.output_T1.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output_T1.setFont(font)
        self.output_T1.setObjectName("output_T1")
        self.grid_Output.addWidget(self.output_T1, 0, 1, 1, 1)
        self.output_T3 = QtWidgets.QLineEdit(self.gb_Output)
        self.output_T3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_T3.sizePolicy().hasHeightForWidth())
        self.output_T3.setSizePolicy(sizePolicy)
        self.output_T3.setMinimumSize(QtCore.QSize(0, 0))
        self.output_T3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.output_T3.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output_T3.setFont(font)
        self.output_T3.setObjectName("output_T3")
        self.grid_Output.addWidget(self.output_T3, 0, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.grid_Output.addWidget(self.label_7, 1, 4, 1, 1)
        self.label_t2 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_t2.sizePolicy().hasHeightForWidth())
        self.label_t2.setSizePolicy(sizePolicy)
        self.label_t2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_t2.setFont(font)
        self.label_t2.setObjectName("label_t2")
        self.grid_Output.addWidget(self.label_t2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_Output.addItem(spacerItem3, 4, 11, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.grid_Output.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_Output.addItem(spacerItem4, 1, 7, 1, 1)
        self.main_VerticalLayout.addWidget(self.gb_Output)
        self.gb_Plot = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_Plot.sizePolicy().hasHeightForWidth())
        self.gb_Plot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gb_Plot.setFont(font)
        self.gb_Plot.setObjectName("gb_Plot")
        self.grid_Plot = QtWidgets.QGridLayout(self.gb_Plot)
        self.grid_Plot.setObjectName("grid_Plot")
        self.lbl_Abcissa = QtWidgets.QLabel(self.gb_Plot)
        self.lbl_Abcissa.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lbl_Abcissa.setObjectName("lbl_Abcissa")
        self.grid_Plot.addWidget(self.lbl_Abcissa, 0, 0, 1, 1)
        self.cmb_graph = QtWidgets.QComboBox(self.gb_Plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_graph.sizePolicy().hasHeightForWidth())
        self.cmb_graph.setSizePolicy(sizePolicy)
        self.cmb_graph.setMaximumSize(QtCore.QSize(50, 16777215))
        self.cmb_graph.setObjectName("cmb_graph")
        self.cmb_graph.addItem("")
        self.cmb_graph.addItem("")
        self.grid_Plot.addWidget(self.cmb_graph, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_Plot.addItem(spacerItem5, 0, 2, 1, 1)
        self.main_VerticalLayout.addWidget(self.gb_Plot)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.main_VerticalLayout.addItem(spacerItem6)

        self.retranslateUi(Form)
        self.cmb_graph.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gb_Input.setTitle(_translate("Form", "Input"))
        self.lbl_PHigh.setText(_translate("Form", "Cylinder Volume"))
        self.input_InitialTemperature.setText(_translate("Form", "35"))
        self.rdo_Metric.setText(_translate("Form", "Metric"))
        self.input_CylinderVolume.setText(_translate("Form", ".0006"))
        self.input_CylinderVolume.setPlaceholderText(_translate("Form", "enter a value for the high pressure isobar"))
        self.btn_Calculate.setText(_translate("Form", "Calculate"))
        self.lbl_TurbineInletCondition.setText(_translate("Form", "Compression Ratio"))
        self.input_CompressionRatio.setText(_translate("Form", "9.5"))
        self.lbl_PLow.setText(_translate("Form", "Initial Pressure"))
        self.label.setText(_translate("Form", "Maximum Temperature"))
        self.input_MaximumTemperature.setText(_translate("Form", "1696"))
        self.input_MaximumTemperature.setPlaceholderText(_translate("Form", "turbine isentropic efficiency 0.0<eta<=1.0"))
        self.units_initial_pressure.setText(_translate("Form", "kPa"))
        self.units_cylinder_volume.setText(_translate("Form", "m^3"))
        self.units_initial_temp.setText(_translate("Form", "Celsius"))
        self.rdo_English.setText(_translate("Form", "English"))
        self.units_max_temp.setText(_translate("Form", "Celsius"))
        self.input_InitialPressure.setText(_translate("Form", "100"))
        self.input_InitialPressure.setPlaceholderText(_translate("Form", "enter a value for the low pressure isobar"))
        self.label_16.setText(_translate("Form", "Initial Temperature"))
        self.gb_Output.setTitle(_translate("Form", "Output"))
        self.label_t3.setText(_translate("Form", "Celsius"))
        self.label_t4.setText(_translate("Form", "Celsius"))
        self.label_12.setText(_translate("Form", "%"))
        self.label_5.setText(_translate("Form", "T2"))
        self.label_9.setText(_translate("Form", "T3"))
        self.label_t1.setText(_translate("Form", "Celsius"))
        self.label_10.setText(_translate("Form", "Cycle Efficiency"))
        self.label_7.setText(_translate("Form", "T4"))
        self.label_t2.setText(_translate("Form", "Celsius"))
        self.label_2.setText(_translate("Form", "T1"))
        self.gb_Plot.setTitle(_translate("Form", "Plot"))
        self.lbl_Abcissa.setText(_translate("Form", "Graph"))
        self.cmb_graph.setItemText(0, _translate("Form", "P-V"))
        self.cmb_graph.setItemText(1, _translate("Form", "T-S"))

