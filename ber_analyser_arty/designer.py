# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ber_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 50, 361, 541))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.toolBox = QtWidgets.QToolBox(self.frame)
        self.toolBox.setGeometry(QtCore.QRect(10, 14, 341, 501))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 341, 408))
        self.page.setObjectName("page")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 302, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.plllabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.plllabel.setObjectName("plllabel")
        self.gridLayout.addWidget(self.plllabel, 3, 1, 1, 1)
        self.lineratelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lineratelabel.setObjectName("lineratelabel")
        self.gridLayout.addWidget(self.lineratelabel, 2, 1, 1, 1)
        self.postcombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.postcombo.setObjectName("postcombo")
        self.postcombo.addItem("")
        self.postcombo.addItem("")
        self.postcombo.addItem("")
        self.postcombo.addItem("")
        self.postcombo.addItem("")
        self.postcombo.addItem("")
        self.postcombo.addItem("")
        self.postcombo.addItem("")
        self.gridLayout.addWidget(self.postcombo, 9, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.precombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.precombo.setObjectName("precombo")
        self.precombo.addItem("")
        self.precombo.addItem("")
        self.precombo.addItem("")
        self.precombo.addItem("")
        self.precombo.addItem("")
        self.precombo.addItem("")
        self.gridLayout.addWidget(self.precombo, 8, 1, 1, 1)
        self.swingcombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.swingcombo.setObjectName("swingcombo")
        self.swingcombo.addItem("")
        self.swingcombo.addItem("")
        self.swingcombo.addItem("")
        self.swingcombo.addItem("")
        self.swingcombo.addItem("")
        self.gridLayout.addWidget(self.swingcombo, 7, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.linklabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.linklabel.setObjectName("linklabel")
        self.gridLayout.addWidget(self.linklabel, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 11, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.txrst = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.txrst.setObjectName("txrst")
        self.gridLayout.addWidget(self.txrst, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)
        self.rxrst = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.rxrst.setObjectName("rxrst")
        self.gridLayout.addWidget(self.rxrst, 10, 1, 1, 1)
        self.txpolcheckbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.txpolcheckbox.setObjectName("txpolcheckbox")
        self.gridLayout.addWidget(self.txpolcheckbox, 5, 1, 1, 1)
        self.rxpolcheckbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.rxpolcheckbox.setObjectName("rxpolcheckbox")
        self.gridLayout.addWidget(self.rxpolcheckbox, 11, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 6, 0, 1, 1)
        self.loopbackcheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.loopbackcheck.setObjectName("loopbackcheck")
        self.gridLayout.addWidget(self.loopbackcheck, 6, 1, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 341, 408))
        self.page_2.setObjectName("page_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 281, 121))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.berlabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.berlabel.setObjectName("berlabel")
        self.gridLayout_2.addWidget(self.berlabel, 3, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 0, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_6, 2, 1, 1, 1)
        self.txconfigcombo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.txconfigcombo.setObjectName("txconfigcombo")
        self.txconfigcombo.addItem("")
        self.txconfigcombo.addItem("")
        self.txconfigcombo.addItem("")
        self.txconfigcombo.addItem("")
        self.gridLayout_2.addWidget(self.txconfigcombo, 0, 1, 1, 1)
        self.rxconfigcombo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.rxconfigcombo.setObjectName("rxconfigcombo")
        self.rxconfigcombo.addItem("")
        self.rxconfigcombo.addItem("")
        self.rxconfigcombo.addItem("")
        self.rxconfigcombo.addItem("")
        self.gridLayout_2.addWidget(self.rxconfigcombo, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 3, 0, 1, 1)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 341, 408))
        self.page_3.setObjectName("page_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.page_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 281, 128))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.drpval = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.drpval.setObjectName("drpval")
        self.gridLayout_3.addWidget(self.drpval, 1, 1, 1, 1)
        self.drpaddr = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.drpaddr.setObjectName("drpaddr")
        self.gridLayout_3.addWidget(self.drpaddr, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 1, 0, 1, 1)
        self.drpreadbutton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.drpreadbutton.setObjectName("drpreadbutton")
        self.gridLayout_3.addWidget(self.drpreadbutton, 2, 1, 1, 1)
        self.drpwritebutton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.drpwritebutton.setObjectName("drpwritebutton")
        self.gridLayout_3.addWidget(self.drpwritebutton, 3, 1, 1, 1)
        self.toolBox.addItem(self.page_3, "")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(50, 10, 251, 20))
        self.label_25.setObjectName("label_25")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MGT Tile location"))
        self.plllabel.setText(_translate("MainWindow", "Locked"))
        self.lineratelabel.setText(_translate("MainWindow", "3 Gbps"))
        self.postcombo.setItemText(0, _translate("MainWindow", "0 dB (00000)"))
        self.postcombo.setItemText(1, _translate("MainWindow", "0.5 dB (00010)"))
        self.postcombo.setItemText(2, _translate("MainWindow", "1 dB (00100)"))
        self.postcombo.setItemText(3, _translate("MainWindow", "2 dB (01000)"))
        self.postcombo.setItemText(4, _translate("MainWindow", "4 dB (01111)"))
        self.postcombo.setItemText(5, _translate("MainWindow", "6 dB (10100)"))
        self.postcombo.setItemText(6, _translate("MainWindow", "8 dB (11000)"))
        self.postcombo.setItemText(7, _translate("MainWindow", "12 dB (11110)"))
        self.label_5.setText(_translate("MainWindow", "TX Reset"))
        self.precombo.setItemText(0, _translate("MainWindow", "0 dB (00000)"))
        self.precombo.setItemText(1, _translate("MainWindow", "0.5 dB (00010)"))
        self.precombo.setItemText(2, _translate("MainWindow", "1 dB (00101)"))
        self.precombo.setItemText(3, _translate("MainWindow", "2 dB (01000) "))
        self.precombo.setItemText(4, _translate("MainWindow", "4 dB (01111)"))
        self.precombo.setItemText(5, _translate("MainWindow", "6 dB (10100)"))
        self.swingcombo.setItemText(0, _translate("MainWindow", "300 mV (0001)"))
        self.swingcombo.setItemText(1, _translate("MainWindow", "500 mV (0100)"))
        self.swingcombo.setItemText(2, _translate("MainWindow", "750 mV (1000)"))
        self.swingcombo.setItemText(3, _translate("MainWindow", "900 mV (1011)"))
        self.swingcombo.setItemText(4, _translate("MainWindow", "1050 mV (1111)"))
        self.label_7.setText(_translate("MainWindow", "TX Polarity"))
        self.linklabel.setText(_translate("MainWindow", "Link"))
        self.label_3.setText(_translate("MainWindow", "MGT Line Rate"))
        self.label_2.setText(_translate("MainWindow", "MGT link status"))
        self.label_12.setText(_translate("MainWindow", "GTP_X0Y0"))
        self.label_9.setText(_translate("MainWindow", "TX Output Swing"))
        self.label_8.setText(_translate("MainWindow", "RX Polarity"))
        self.label_6.setText(_translate("MainWindow", "RX Reset"))
        self.label_10.setText(_translate("MainWindow", "TX Precursor"))
        self.label_4.setText(_translate("MainWindow", "PLL Status"))
        self.txrst.setText(_translate("MainWindow", "Reset"))
        self.label_11.setText(_translate("MainWindow", "TX Postcursor"))
        self.rxrst.setText(_translate("MainWindow", "Reset"))
        self.txpolcheckbox.setText(_translate("MainWindow", "Invert"))
        self.rxpolcheckbox.setText(_translate("MainWindow", "Invert"))
        self.label_15.setText(_translate("MainWindow", "Nr end PMA Loopback"))
        self.loopbackcheck.setText(_translate("MainWindow", "Disable"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "MGT Settings"))
        self.berlabel.setText(_translate("MainWindow", "BER"))
        self.label_16.setText(_translate("MainWindow", "TX PRBS Config             "))
        self.label_17.setText(_translate("MainWindow", "RX PRBS Config"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "0%"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "25%"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "50%"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "75%"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "100%"))
        self.txconfigcombo.setItemText(0, _translate("MainWindow", "7"))
        self.txconfigcombo.setItemText(1, _translate("MainWindow", "15"))
        self.txconfigcombo.setItemText(2, _translate("MainWindow", "23"))
        self.txconfigcombo.setItemText(3, _translate("MainWindow", "31"))
        self.rxconfigcombo.setItemText(0, _translate("MainWindow", "7"))
        self.rxconfigcombo.setItemText(1, _translate("MainWindow", "15"))
        self.rxconfigcombo.setItemText(2, _translate("MainWindow", "23"))
        self.rxconfigcombo.setItemText(3, _translate("MainWindow", "31"))
        self.label_20.setText(_translate("MainWindow", "Inject Error"))
        self.label_21.setText(_translate("MainWindow", "Bit Error Ratio"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "BER Settings"))
        self.label_23.setText(_translate("MainWindow", "DRP Address             0x"))
        self.label_24.setText(_translate("MainWindow", "DRP Value                  0x"))
        self.drpreadbutton.setText(_translate("MainWindow", "DRP Read"))
        self.drpwritebutton.setText(_translate("MainWindow", "DRP Write"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "DRP Interface"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Bit Error Ratio Analyzer </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

