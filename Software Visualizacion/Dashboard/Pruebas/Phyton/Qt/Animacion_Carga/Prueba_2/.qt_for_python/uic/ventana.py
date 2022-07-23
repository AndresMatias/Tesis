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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(685, 807)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.frame_1 = QFrame(self.centralwidget)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setGeometry(QRect(70, 210, 100, 100))
        self.frame_1.setMinimumSize(QSize(100, 100))
        self.frame_1.setMaximumSize(QSize(300, 300))
        self.frame_1.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.b_1 = QPushButton(self.centralwidget)
        self.b_1.setObjectName(u"b_1")
        self.b_1.setGeometry(QRect(120, 120, 101, 41))
        self.b_2 = QPushButton(self.centralwidget)
        self.b_2.setObjectName(u"b_2")
        self.b_2.setGeometry(QRect(290, 120, 111, 41))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(260, 340, 321, 191))
        self.frame.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(100, 100))
        self.frame_2.setMaximumSize(QSize(300, 300))
        self.frame_2.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 100))
        self.frame_3.setMaximumSize(QSize(300, 300))
        self.frame_3.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(70, 590, 100, 100))
        self.frame_4.setMinimumSize(QSize(100, 100))
        self.frame_4.setMaximumSize(QSize(300, 300))
        self.frame_4.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.b_3 = QPushButton(self.centralwidget)
        self.b_3.setObjectName(u"b_3")
        self.b_3.setGeometry(QRect(460, 120, 111, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b_1.setText(QCoreApplication.translate("MainWindow", u"Expandir", None))
        self.b_2.setText(QCoreApplication.translate("MainWindow", u"Geometrico", None))
        self.b_3.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
    # retranslateUi

