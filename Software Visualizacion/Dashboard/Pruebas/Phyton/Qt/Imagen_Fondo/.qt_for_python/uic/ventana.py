# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Logos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(868, 910)
        MainWindow.setStyleSheet(u"\n"
"QLabel#label_2{\n"
"	border-image: url(:/Logos Principales/Logo 1.jpg);\n"
"	background-color: rgb(85, 255, 0);\n"
"}\n"
".QLabel{\n"
"	background-color: rgb(40, 40, 40);\n"
"}background-color: rgb(255, 170, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 420, 141, 91))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 560, 161, 91))
        self.label_2.setStyleSheet(u"")
        self.l1 = QLabel(self.centralwidget)
        self.l1.setObjectName(u"l1")
        self.l1.setGeometry(QRect(70, 680, 111, 81))
        self.w1 = QWidget(self.centralwidget)
        self.w1.setObjectName(u"w1")
        self.w1.setGeometry(QRect(280, 150, 65, 31))
        self.w1.setStyleSheet(u"background-color: rgb(255, 76, 201);")
        self.verticalLayout = QVBoxLayout(self.w1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.l2 = QLabel(self.w1)
        self.l2.setObjectName(u"l2")

        self.verticalLayout.addWidget(self.l2)

        self.w2 = QWidget(self.centralwidget)
        self.w2.setObjectName(u"w2")
        self.w2.setGeometry(QRect(310, 260, 311, 161))
        self.w2.setStyleSheet(u"background-color: rgb(255, 76, 201);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.l1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.l2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

