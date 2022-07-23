# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'V_ConexionSQL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_cp(object):
    def setupUi(self, cp):
        if not cp.objectName():
            cp.setObjectName(u"cp")
        cp.resize(830, 536)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cp.sizePolicy().hasHeightForWidth())
        cp.setSizePolicy(sizePolicy)
        cp.setStyleSheet(u"*{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"}\n"
".QWidget{\n"
"	\n"
"	background-color: rgb(40, 40, 40);\n"
"	border-radius: 2;\n"
"\n"
"}\n"
".QLabel{\n"
"	background-color: rgb(40, 40, 40);\n"
"	font: bold;\n"
"}\n"
"QWidget#cp{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"}\n"
"\n"
"QPushButton#conectarSql:hover{\n"
"background-color: orange;\n"
"}\n"
"\n"
"QPushButton#desconectarSql:hover{\n"
"background-color: orange;\n"
"}")
        self.gridLayout_3 = QGridLayout(cp)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cp_1 = QWidget(cp)
        self.cp_1.setObjectName(u"cp_1")
        self.verticalLayout_2 = QVBoxLayout(self.cp_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.cp_1)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.cp_3 = QWidget(self.cp_1)
        self.cp_3.setObjectName(u"cp_3")
        self.verticalLayout = QVBoxLayout(self.cp_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.cp_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.server = QLineEdit(self.cp_3)
        self.server.setObjectName(u"server")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.server.sizePolicy().hasHeightForWidth())
        self.server.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.server.setFont(font)

        self.gridLayout.addWidget(self.server, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.label_2 = QLabel(self.cp_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.bbdd = QLineEdit(self.cp_3)
        self.bbdd.setObjectName(u"bbdd")
        self.bbdd.setFont(font)

        self.gridLayout.addWidget(self.bbdd, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.label_3 = QLabel(self.cp_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.user = QLineEdit(self.cp_3)
        self.user.setObjectName(u"user")
        self.user.setFont(font)

        self.gridLayout.addWidget(self.user, 4, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 1, 1, 1)

        self.label_4 = QLabel(self.cp_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.passw = QLineEdit(self.cp_3)
        self.passw.setObjectName(u"passw")
        self.passw.setFont(font)

        self.gridLayout.addWidget(self.passw, 6, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.conectarSql = QPushButton(self.cp_3)
        self.conectarSql.setObjectName(u"conectarSql")
        font1 = QFont()
        font1.setPointSize(10)
        self.conectarSql.setFont(font1)

        self.horizontalLayout.addWidget(self.conectarSql)

        self.desconectarSql = QPushButton(self.cp_3)
        self.desconectarSql.setObjectName(u"desconectarSql")
        self.desconectarSql.setFont(font1)

        self.horizontalLayout.addWidget(self.desconectarSql)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 30)
        self.verticalLayout.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.cp_3)


        self.gridLayout_3.addWidget(self.cp_1, 0, 0, 1, 1)


        self.retranslateUi(cp)

        QMetaObject.connectSlotsByName(cp)
    # setupUi

    def retranslateUi(self, cp):
        cp.setWindowTitle(QCoreApplication.translate("cp", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("cp", u"<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Conexion SQL</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("cp", u"<html><head/><body><p><span style=\" font-size:12pt; color:#00ffff;\">Servidor</span></p></body></html>", None))
        self.server.setText("")
        self.label_2.setText(QCoreApplication.translate("cp", u"<html><head/><body><p><span style=\" font-size:12pt; color:#00ffff;\">BBDD</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("cp", u"<html><head/><body><p><span style=\" font-size:12pt; color:#00ffff;\">Usuario</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("cp", u"<html><head/><body><p><span style=\" font-size:12pt; color:#00ffff;\">Contrase\u00f1a</span></p></body></html>", None))
        self.conectarSql.setText(QCoreApplication.translate("cp", u"Conectar", None))
        self.desconectarSql.setText(QCoreApplication.translate("cp", u"Desconectar", None))
    # retranslateUi

