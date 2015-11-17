# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hud.ui'
#
# Created: Sun Jun  7 13:55:05 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setEnabled(True)
        Form.resize(245, 180)
        Form.setMinimumSize(QtCore.QSize(245, 127))
        Form.setMaximumSize(QtCore.QSize(245, 180))
        Form.setWindowTitle(_fromUtf8(""))
        Form.setWindowOpacity(0.8)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(_fromUtf8("background: rgb(0, 0, 0)"))
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(8, 9, 235, 161))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.countdown = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.countdown.setFont(font)
        self.countdown.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.countdown.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255)"))
        self.countdown.setAlignment(QtCore.Qt.AlignCenter)
        self.countdown.setObjectName(_fromUtf8("countdown"))
        self.gridLayout.addWidget(self.countdown, 2, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255)"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet(_fromUtf8("color: rgb(128, 128, 128)"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 20)
        self.gridLayout.setRowStretch(3, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.countdown.setText(_translate("Form", "0", None))
        self.pushButton.setText(_translate("Form", "Dismiss", None))
        self.label_2.setText(_translate("Form", "Move mouse cursor to click location", None))
        self.label.setText(_translate("Form", "0 click locations collected", None))

