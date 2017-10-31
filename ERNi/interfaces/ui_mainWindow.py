# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1534, 1001)
        MainWindow.setMinimumSize(QtCore.QSize(300, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.data_import = QtWidgets.QPushButton(self.centralwidget)
        self.data_import.setGeometry(QtCore.QRect(120, 80, 93, 32))
        self.data_import.setObjectName("data_import")
        self.list_dirs = QtWidgets.QToolButton(self.centralwidget)
        self.list_dirs.setGeometry(QtCore.QRect(270, 130, 26, 22))
        self.list_dirs.setObjectName("list_dirs")
        self.show_before = QtWidgets.QCheckBox(self.centralwidget)
        self.show_before.setGeometry(QtCore.QRect(480, 290, 87, 20))
        self.show_before.setObjectName("show_before")
        self.ele_name = QtWidgets.QTextEdit(self.centralwidget)
        self.ele_name.setGeometry(QtCore.QRect(260, 250, 71, 31))
        self.ele_name.setObjectName("ele_name")
        self.price_label = QtWidgets.QLabel(self.centralwidget)
        self.price_label.setGeometry(QtCore.QRect(210, 260, 31, 16))
        self.price_label.setObjectName("price_label")
        self.tax_rate = QtWidgets.QSpinBox(self.centralwidget)
        self.tax_rate.setGeometry(QtCore.QRect(260, 330, 47, 24))
        self.tax_rate.setProperty("value", 20)
        self.tax_rate.setObjectName("tax_rate")
        self.calcu_price = QtWidgets.QPushButton(self.centralwidget)
        self.calcu_price.setGeometry(QtCore.QRect(210, 400, 113, 32))
        self.calcu_price.setObjectName("calcu_price")
        self.tax_label = QtWidgets.QLabel(self.centralwidget)
        self.tax_label.setGeometry(QtCore.QRect(210, 330, 31, 16))
        self.tax_label.setObjectName("tax_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1534, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        self.menuERNi = QtWidgets.QMenu(self.menubar)
        self.menuERNi.setObjectName("menuERNi")
        MainWindow.setMenuBar(self.menubar)
        self.actionPreference = QtWidgets.QAction(MainWindow)
        self.actionPreference.setObjectName("actionPreference")
        self.menuERNi.addAction(self.actionPreference)
        self.menubar.addAction(self.menuERNi.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.data_import.setText(_translate("MainWindow", "Import..."))
        self.list_dirs.setText(_translate("MainWindow", "..."))
        self.show_before.setText(_translate("MainWindow", "CheckBox"))
        self.price_label.setText(_translate("MainWindow", "Price"))
        self.calcu_price.setText(_translate("MainWindow", "Calculate price"))
        self.tax_label.setText(_translate("MainWindow", "Tax"))
        self.menuERNi.setTitle(_translate("MainWindow", "ERNi"))
        self.actionPreference.setText(_translate("MainWindow", "Preference"))

