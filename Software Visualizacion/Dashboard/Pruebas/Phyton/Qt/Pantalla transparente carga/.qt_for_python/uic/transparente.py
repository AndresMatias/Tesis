# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transparente.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(849, 613)
        MainWindow.setStyleSheet(u"*{\n"
"	\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
".QWidget{\n"
"	background-color: rgb(20, 20, 20);\n"
"	border-radius: 2;\n"
"\n"
"}\n"
"QWidget#cp{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"}")
        self.cp = QWidget(MainWindow)
        self.cp.setObjectName(u"cp")
        self.gridLayout = QGridLayout(self.cp)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.cp)
        self.widget.setObjectName(u"widget")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.cp)
        self.widget_3.setObjectName(u"widget_3")

        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)

        self.widget_4 = QWidget(self.cp)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_4, 1, 1, 1, 1)

        self.widget_2 = QWidget(self.cp)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.cp)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

