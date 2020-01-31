# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SHASHI\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\gui_speech\gui_speech_dockwidget_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DTDIDockWidgetBase(object):
    def setupUi(self, DTDIDockWidgetBase):
        DTDIDockWidgetBase.setObjectName("DTDIDockWidgetBase")
        DTDIDockWidgetBase.resize(300, 500)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.startButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.startButton.setGeometry(QtCore.QRect(180, 50, 31, 31))
        self.startButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/MIC_START.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon)
        self.startButton.setObjectName("startButton")
        self.startLabel = QtWidgets.QLabel(self.dockWidgetContents)
        self.startLabel.setGeometry(QtCore.QRect(290, 50, 41, 41))
        self.startLabel.setText("")
        self.startLabel.setPixmap(QtGui.QPixmap("D:/MIC_START.png"))
        self.startLabel.setScaledContents(True)
        self.startLabel.setObjectName("startLabel")
        self.querTextArea = QtWidgets.QTextEdit(self.dockWidgetContents)
        self.querTextArea.setGeometry(QtCore.QRect(80, 130, 251, 141))
        self.querTextArea.setObjectName("querTextArea")
        self.stopLabel = QtWidgets.QLabel(self.dockWidgetContents)
        self.stopLabel.setGeometry(QtCore.QRect(350, 60, 31, 31))
        self.stopLabel.setText("")
        self.stopLabel.setPixmap(QtGui.QPixmap("D:/MIC_STOP.png"))
        self.stopLabel.setScaledContents(True)
        self.stopLabel.setObjectName("stopLabel")
        self.textRadioButton = QtWidgets.QRadioButton(self.dockWidgetContents)
        self.textRadioButton.setGeometry(QtCore.QRect(70, 100, 91, 21))
        self.textRadioButton.setObjectName("textRadioButton")
        self.stopButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.stopButton.setGeometry(QtCore.QRect(230, 50, 31, 31))
        self.stopButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/MIC_STOP.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setObjectName("stopButton")
        self.speechRadioButton = QtWidgets.QRadioButton(self.dockWidgetContents)
        self.speechRadioButton.setGeometry(QtCore.QRect(70, 60, 131, 21))
        self.speechRadioButton.setObjectName("speechRadioButton")
        self.executeButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.executeButton.setGeometry(QtCore.QRect(340, 170, 75, 23))
        self.executeButton.setObjectName("executeButton")
        DTDIDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(DTDIDockWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(DTDIDockWidgetBase)

    def retranslateUi(self, DTDIDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        DTDIDockWidgetBase.setWindowTitle(_translate("DTDIDockWidgetBase", "Katha Chitra"))
        self.textRadioButton.setText(_translate("DTDIDockWidgetBase", "TEXT INPUT"))
        self.speechRadioButton.setText(_translate("DTDIDockWidgetBase", "SPEECH INPUT"))
        self.executeButton.setText(_translate("DTDIDockWidgetBase", "EXECUTE"))

