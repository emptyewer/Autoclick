# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autoclick.ui'
#
# Created: Sun Jun  7 12:32:15 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import hud
import threading
import autopy
import time

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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        '''

        Initialize global variables for this class and sets up UI elements in QT4.

        '''
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.locations = []
        self.interval = 5
        self.click = False
        self.clickingIndex = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(582, 176)
        MainWindow.setMinimumSize(QtCore.QSize(582, 176))
        MainWindow.setMaximumSize(QtCore.QSize(582, 176))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 561, 141))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.timer = QtGui.QSpinBox(self.gridLayoutWidget)
        self.timer.setMaximum(30)
        self.timer.setSingleStep(5)
        self.timer.setProperty("value", 5)
        self.timer.setObjectName(_fromUtf8("timer"))
        self.gridLayout.addWidget(self.timer, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.chooseLocations = QtGui.QPushButton(self.gridLayoutWidget)
        self.chooseLocations.setObjectName(_fromUtf8("chooseLocations"))
        self.gridLayout.addWidget(self.chooseLocations, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.start = QtGui.QPushButton(self.gridLayoutWidget)
        self.start.setObjectName(_fromUtf8("start"))
        self.gridLayout.addWidget(self.start, 2, 1, 1, 1)
        self.stop = QtGui.QPushButton(self.gridLayoutWidget)
        self.stop.setObjectName(_fromUtf8("stop"))
        self.gridLayout.addWidget(self.stop, 2, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 5)
        self.locationsText = QtGui.QLabel(self.centralwidget)
        self.locationsText.setGeometry(QtCore.QRect(72, 40, 220, 16))
        self.locationsText.setStyleSheet(_fromUtf8("color: rgb(129, 129, 129)"))
        self.locationsText.setObjectName(_fromUtf8("locationsText"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Autoclick", "Autoclick", None))
        self.label_2.setText(_translate("MainWindow", "Repeat Timer (secs)", None))
        self.label.setText(_translate("MainWindow", "Mouse Click Locations", None))
        self.chooseLocations.setText(_translate("MainWindow", "Choose", None))
        self.label_3.setText(_translate("MainWindow", "1", None))
        self.label_4.setText(_translate("MainWindow", "2", None))
        self.label_5.setText(_translate("MainWindow", "3", None))
        self.start.setText(_translate("MainWindow", "Start Autoclick", None))
        self.chooseLocations.clicked.connect(self.chooseMouseLocations)
        self.start.clicked.connect(self.startClicking)
        self.stop.setText(_translate("MainWindow", "Stop Autoclick", None))
        self.stop.clicked.connect(self.stopClicking)
        self.locationsText.setText(_translate("MainWindow", "0 click locations", None))

    def chooseMouseLocations(self):
        self.locations = []
        self.interval = 5
        self.locationsText.setText("%d autoclick locations collected" % len(self.locations))
        self.hud = hud.Ui_Form()
        self.hud.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.hud.show()
        self.hud.countdown.setText("%d" % self.interval)
        threading.Timer(1, self.setTimerText).start()
        self.interval -= 1

    def startClicking(self):
        if self.click == False:
            self.click = True
            self.clicklocations()

    def stopClicking(self):
        if self.click == True:
            self.click = False
            self.start.setText("Start Clicking")


    def clicklocations(self):
        trigger = self.timer.value()
        autopy.mouse.move(self.locations[self.clickingIndex][0], self.locations[self.clickingIndex][1])
        autopy.mouse.click()
        self.start.setText("Location %d @ x = %.2f, y = %.2f)" % (self.clickingIndex+1, self.locations[self.clickingIndex][0], self.locations[self.clickingIndex][1]))
        self.clickingIndex = self.clickingIndex + 1
        if self.clickingIndex == len(self.locations):
            self.clickingIndex = 0
        if self.click == True:
            threading.Timer(trigger, self.clicklocations).start()
        else:
            self.start.setText("Start Clicking")


    def setTimerText(self):
        if self.interval == 0:
            self.locations.append(autopy.mouse.get_pos())
            self.hud.label.setText("%d autoclick locations collected" % len(self.locations))
            self.locationsText.setText("%d autoclick locations collected" % len(self.locations))
            self.interval = 5
        self.hud.countdown.setText("%d" % self.interval)
        self.interval -= 1
        if self.hud.isVisible():
            threading.Timer(1, self.setTimerText).start()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = Ui_MainWindow()
    mainWin.show()
    sys.exit(app.exec_())