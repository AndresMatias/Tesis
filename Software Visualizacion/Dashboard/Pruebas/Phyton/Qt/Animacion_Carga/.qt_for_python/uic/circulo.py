# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'circulo.ui'
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
        MainWindow.resize(635, 558)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.progresbar = QFrame(self.frame)
        self.progresbar.setObjectName(u"progresbar")
        self.progresbar.setGeometry(QRect(180, 170, 300, 300))
        self.progresbar.setMinimumSize(QSize(300, 300))
        self.progresbar.setStyleSheet(u"QFrame{\n"
"border-radius:150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:{stop1} rgba(85, 85, 255, 255), stop:{stop2} rgba(255, 255, 255, 255));\n"
"}")
        self.progresbar.setFrameShape(QFrame.StyledPanel)
        self.progresbar.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.progresbar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 20, 260, 260))
        self.frame_2.setMinimumSize(QSize(260, 260))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"border-radius:130px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

