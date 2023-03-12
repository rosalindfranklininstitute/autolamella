# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 945)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 630, 441, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.log_txt = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.log_txt.setObjectName("log_txt")
        self.verticalLayout_2.addWidget(self.log_txt)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 441, 621))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 321, 125))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 4, 0, 1, 1)
        self.microscope_status = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.microscope_status.setFont(font)
        self.microscope_status.setText("")
        self.microscope_status.setAlignment(QtCore.Qt.AlignCenter)
        self.microscope_status.setObjectName("microscope_status")
        self.gridLayout_2.addWidget(self.microscope_status, 0, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.RefImage = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.RefImage.setObjectName("RefImage")
        self.gridLayout_2.addWidget(self.RefImage, 5, 0, 1, 3)
        self.hfw_box = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.hfw_box.setMinimum(50)
        self.hfw_box.setMaximum(5000)
        self.hfw_box.setObjectName("hfw_box")
        self.gridLayout_2.addWidget(self.hfw_box, 4, 1, 1, 1)
        self.protocol_txt = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.protocol_txt.setText("")
        self.protocol_txt.setObjectName("protocol_txt")
        self.gridLayout_2.addWidget(self.protocol_txt, 1, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 140, 417, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 14, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.move_fiducial_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.move_fiducial_button.setObjectName("move_fiducial_button")
        self.gridLayout.addWidget(self.move_fiducial_button, 13, 2, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 8, 0, 1, 1)
        self.tilt_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.tilt_button.setObjectName("tilt_button")
        self.gridLayout.addWidget(self.tilt_button, 3, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.mill_position_txt = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.mill_position_txt.setFont(font)
        self.mill_position_txt.setText("")
        self.mill_position_txt.setObjectName("mill_position_txt")
        self.gridLayout.addWidget(self.mill_position_txt, 3, 2, 1, 1)
        self.microexpansionCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.microexpansionCheckBox.setObjectName("microexpansionCheckBox")
        self.gridLayout.addWidget(self.microexpansionCheckBox, 9, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 3)
        self.lamella_count_txt = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lamella_count_txt.setFont(font)
        self.lamella_count_txt.setObjectName("lamella_count_txt")
        self.gridLayout.addWidget(self.lamella_count_txt, 8, 1, 1, 2)
        self.show_lamella = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.show_lamella.setObjectName("show_lamella")
        self.gridLayout.addWidget(self.show_lamella, 9, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 0, 1, 1)
        self.lamella_index = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.lamella_index.setMinimum(0)
        self.lamella_index.setObjectName("lamella_index")
        self.gridLayout.addWidget(self.lamella_index, 11, 1, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 11, 2, 1, 1)
        self.go_to_lamella = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.go_to_lamella.setObjectName("go_to_lamella")
        self.gridLayout.addWidget(self.go_to_lamella, 12, 1, 1, 1)
        self.remill_fiducial = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.remill_fiducial.setObjectName("remill_fiducial")
        self.gridLayout.addWidget(self.remill_fiducial, 13, 0, 1, 1)
        self.move_lamella_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.move_lamella_button.setObjectName("move_lamella_button")
        self.gridLayout.addWidget(self.move_lamella_button, 13, 1, 1, 1)
        self.run_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.run_button.setFont(font)
        self.run_button.setStyleSheet("background-color: darkGreen")
        self.run_button.setObjectName("run_button")
        self.gridLayout.addWidget(self.run_button, 15, 0, 1, 3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 2, 421, 613))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.stageRotationLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.stageRotationLabel.setObjectName("stageRotationLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.stageRotationLabel)
        self.stage_rotation = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.stage_rotation.setMaximum(1000.0)
        self.stage_rotation.setObjectName("stage_rotation")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.stage_rotation)
        self.stageTiltLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.stageTiltLabel.setObjectName("stageTiltLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.stageTiltLabel)
        self.stage_tilt = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.stage_tilt.setMaximum(10000.0)
        self.stage_tilt.setObjectName("stage_tilt")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.stage_tilt)
        self.beamShiftAttemptsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.beamShiftAttemptsLabel.setObjectName("beamShiftAttemptsLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.beamShiftAttemptsLabel)
        self.beamshift_attempts = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.beamshift_attempts.setObjectName("beamshift_attempts")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.beamshift_attempts)
        self.scanDirectionLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.scanDirectionLabel.setObjectName("scanDirectionLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.scanDirectionLabel)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.label_5)
        self.lengthLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.lengthLabel.setObjectName("lengthLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lengthLabel)
        self.fiducial_length = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.fiducial_length.setMaximum(1000.0)
        self.fiducial_length.setObjectName("fiducial_length")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.fiducial_length)
        self.widthLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.widthLabel.setObjectName("widthLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.widthLabel)
        self.width_fiducial = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.width_fiducial.setMaximum(1000.0)
        self.width_fiducial.setObjectName("width_fiducial")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.width_fiducial)
        self.depthLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.depthLabel.setObjectName("depthLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.depthLabel)
        self.depth_fiducial = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.depth_fiducial.setMaximum(1000.0)
        self.depth_fiducial.setObjectName("depth_fiducial")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.depth_fiducial)
        self.millingCurrentLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.millingCurrentLabel.setObjectName("millingCurrentLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.millingCurrentLabel)
        self.current_fiducial = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.current_fiducial.setMaximum(1000.0)
        self.current_fiducial.setObjectName("current_fiducial")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.current_fiducial)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.label_9)
        self.stageLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.stageLabel.setObjectName("stageLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.stageLabel)
        self.stage_lamella = QtWidgets.QComboBox(self.formLayoutWidget)
        self.stage_lamella.setObjectName("stage_lamella")
        self.stage_lamella.addItem("")
        self.stage_lamella.addItem("")
        self.stage_lamella.addItem("")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.stage_lamella)
        self.widthLabel_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.widthLabel_2.setObjectName("widthLabel_2")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.widthLabel_2)
        self.lamella_width = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.lamella_width.setMaximum(1000.0)
        self.lamella_width.setObjectName("lamella_width")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lamella_width)
        self.heightLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.heightLabel.setObjectName("heightLabel")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.heightLabel)
        self.lamella_height = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.lamella_height.setMaximum(1000.0)
        self.lamella_height.setObjectName("lamella_height")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lamella_height)
        self.trenchHeightLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.trenchHeightLabel.setObjectName("trenchHeightLabel")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.trenchHeightLabel)
        self.trench_height = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.trench_height.setMaximum(1000.0)
        self.trench_height.setObjectName("trench_height")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.trench_height)
        self.millingDepthLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.millingDepthLabel.setObjectName("millingDepthLabel")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.millingDepthLabel)
        self.depth_trench = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.depth_trench.setMaximum(1000.0)
        self.depth_trench.setObjectName("depth_trench")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.depth_trench)
        self.offsetLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.offsetLabel.setObjectName("offsetLabel")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.offsetLabel)
        self.offset = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.offset.setObjectName("offset")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.offset)
        self.sizeRatioLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sizeRatioLabel.setObjectName("sizeRatioLabel")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.sizeRatioLabel)
        self.size_ratio = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.size_ratio.setObjectName("size_ratio")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.size_ratio)
        self.millingCurrentLabel_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.millingCurrentLabel_2.setObjectName("millingCurrentLabel_2")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.millingCurrentLabel_2)
        self.current_lamella = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.current_lamella.setMaximum(1000.0)
        self.current_lamella.setObjectName("current_lamella")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.current_lamella)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.SpanningRole, self.label_10)
        self.widthLabel_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.widthLabel_3.setObjectName("widthLabel_3")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.widthLabel_3)
        self.micro_exp_width = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.micro_exp_width.setMaximum(1000.0)
        self.micro_exp_width.setObjectName("micro_exp_width")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.micro_exp_width)
        self.heightLabel_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.heightLabel_2.setObjectName("heightLabel_2")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.heightLabel_2)
        self.micro_exp_height = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.micro_exp_height.setMaximum(1000.0)
        self.micro_exp_height.setObjectName("micro_exp_height")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.micro_exp_height)
        self.distanceLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.distanceLabel.setObjectName("distanceLabel")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.distanceLabel)
        self.micro_exp_distance = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.micro_exp_distance.setMaximum(10000.0)
        self.micro_exp_distance.setObjectName("micro_exp_distance")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.micro_exp_distance)
        self.export_protocol = QtWidgets.QPushButton(self.formLayoutWidget)
        self.export_protocol.setObjectName("export_protocol")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.FieldRole, self.export_protocol)
        self.scanDirectionComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.scanDirectionComboBox.setObjectName("scanDirectionComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.scanDirectionComboBox)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
        self.menubar.setObjectName("menubar")
        self.menuAutoLamella = QtWidgets.QMenu(self.menubar)
        self.menuAutoLamella.setObjectName("menuAutoLamella")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.create_exp = QtWidgets.QAction(MainWindow)
        self.create_exp.setObjectName("create_exp")
        self.load_exp = QtWidgets.QAction(MainWindow)
        self.load_exp.setObjectName("load_exp")
        self.platinum = QtWidgets.QAction(MainWindow)
        self.platinum.setObjectName("platinum")
        self.action_load_protocol = QtWidgets.QAction(MainWindow)
        self.action_load_protocol.setObjectName("action_load_protocol")
        self.menuAutoLamella.addAction(self.create_exp)
        self.menuAutoLamella.addAction(self.load_exp)
        self.menuAutoLamella.addAction(self.action_load_protocol)
        self.menuTools.addAction(self.platinum)
        self.menubar.addAction(self.menuAutoLamella.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Console Log"))
        self.label_17.setText(_translate("MainWindow", " Horizontal Field Width (µm)"))
        self.label_11.setText(_translate("MainWindow", "Autolamella"))
        self.label_6.setText(_translate("MainWindow", "Imaging"))
        self.RefImage.setText(_translate("MainWindow", "Take Images"))
        self.label_8.setText(_translate("MainWindow", "Protocol Name"))
        self.label.setText(_translate("MainWindow", "Movement"))
        self.move_fiducial_button.setText(_translate("MainWindow", "Move fiducial"))
        self.add_button.setText(_translate("MainWindow", "Add Lamella"))
        self.tilt_button.setText(_translate("MainWindow", "Move to Mill Angle"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Stable Movement"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Eucentric Movement"))
        self.microexpansionCheckBox.setText(_translate("MainWindow", "Microexpansion Joints"))
        self.label_2.setText(_translate("MainWindow", " Mode:"))
        self.label_7.setText(_translate("MainWindow", "Setup"))
        self.lamella_count_txt.setText(_translate("MainWindow", "Out of: 0 lamellas"))
        self.show_lamella.setText(_translate("MainWindow", "Show Lamella Pattern"))
        self.label_4.setText(_translate("MainWindow", "Current Lamella"))
        self.save_button.setText(_translate("MainWindow", "Save current lamella"))
        self.go_to_lamella.setText(_translate("MainWindow", "Go to position"))
        self.remill_fiducial.setText(_translate("MainWindow", "Remill fiducial"))
        self.move_lamella_button.setText(_translate("MainWindow", "Move lamella"))
        self.run_button.setText(_translate("MainWindow", "Run Autolamella"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "General"))
        self.stageRotationLabel.setText(_translate("MainWindow", "Stage rotation"))
        self.stageTiltLabel.setText(_translate("MainWindow", "Stage tilt"))
        self.beamShiftAttemptsLabel.setText(_translate("MainWindow", "Beam shift attempts"))
        self.scanDirectionLabel.setText(_translate("MainWindow", "Scan Direction"))
        self.label_5.setText(_translate("MainWindow", "Fiducial Parameters"))
        self.lengthLabel.setText(_translate("MainWindow", "Length (µm)"))
        self.widthLabel.setText(_translate("MainWindow", "Width (µm)"))
        self.depthLabel.setText(_translate("MainWindow", "Depth (µm)"))
        self.millingCurrentLabel.setText(_translate("MainWindow", "Milling current (nA)"))
        self.label_9.setText(_translate("MainWindow", "Lamella Parameters "))
        self.stageLabel.setText(_translate("MainWindow", "Stage"))
        self.stage_lamella.setItemText(0, _translate("MainWindow", "1. Rough Cut"))
        self.stage_lamella.setItemText(1, _translate("MainWindow", "2. Regular Cut"))
        self.stage_lamella.setItemText(2, _translate("MainWindow", "3. Polishing Cut"))
        self.widthLabel_2.setText(_translate("MainWindow", "Lamella width (µm)"))
        self.heightLabel.setText(_translate("MainWindow", "Lamella height (µm)"))
        self.trenchHeightLabel.setText(_translate("MainWindow", "Trench height (µm)"))
        self.millingDepthLabel.setText(_translate("MainWindow", "Milling depth (µm)"))
        self.offsetLabel.setText(_translate("MainWindow", "Offset (µm)"))
        self.sizeRatioLabel.setText(_translate("MainWindow", "Size ratio"))
        self.millingCurrentLabel_2.setText(_translate("MainWindow", "Milling current (nA)"))
        self.label_10.setText(_translate("MainWindow", "Microexpansion Joints Parameters"))
        self.widthLabel_3.setText(_translate("MainWindow", "Width (µm)"))
        self.heightLabel_2.setText(_translate("MainWindow", "Height (µm)"))
        self.distanceLabel.setText(_translate("MainWindow", "Distance (µm)"))
        self.export_protocol.setText(_translate("MainWindow", "Save protocol to file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Protocol"))
        self.menuAutoLamella.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.create_exp.setText(_translate("MainWindow", "Create Experiment"))
        self.load_exp.setText(_translate("MainWindow", "Load Experiment"))
        self.platinum.setText(_translate("MainWindow", "Splutter Platinum"))
        self.action_load_protocol.setText(_translate("MainWindow", "Load Protocol"))
