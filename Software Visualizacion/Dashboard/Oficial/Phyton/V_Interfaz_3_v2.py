# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'V_Interfaz_3_v2.ui'
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
        MainWindow.resize(982, 916)
        MainWindow.setStyleSheet(u"*{\n"
"	\n"
"	background-color: rgb(120, 120, 120);\n"
"}\n"
".QWidget{\n"
"	\n"
"	background-color: rgb(40, 40, 40);\n"
"	border-radius: 2;\n"
"}\n"
".QLabel{\n"
"	background-color: rgb(40, 40, 40);\n"
"	font: bold;\n"
"}\n"
"QWidget#cp{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"}\n"
"QWidget#filtroTiempo{\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 2;\n"
"}\n"
"\n"
"QTabWidget::pane{\n"
"	background-color: rgb(120, 120, 120);\n"
"	border:0px solid #000000;\n"
"}\n"
"QTabBar::tab {\n"
"  background: gray;\n"
"  color: white;\n"
"  padding: 10px;\n"
" }\n"
" QTabBar::tab:selected {\n"
"  background: lightgray;\n"
" }\n"
"\n"
"QPushButton#botonAF:hover{\n"
"background-color: orange;\n"
"}\n"
".QFrame{\n"
"	background-color: rgb(40, 40, 40);\n"
"	border-radius: 2;\n"
"}\n"
"QPushButton#botonSql1:hover{\n"
"background-color: orange;\n"
"}\n"
"\n"
"QPushButton#botonSql2:hover{\n"
"background-color: orange;\n"
"}\n"
"QScrollArea{\n"
"border: none;\n"
"}")
        self.actionConexion_SQL = QAction(MainWindow)
        self.actionConexion_SQL.setObjectName(u"actionConexion_SQL")
        self.cp = QWidget(MainWindow)
        self.cp.setObjectName(u"cp")
        self.verticalLayout_2 = QVBoxLayout(self.cp)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.cp)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nroMaquina = QLabel(self.widget)
        self.nroMaquina.setObjectName(u"nroMaquina")

        self.horizontalLayout.addWidget(self.nroMaquina)

        self.horizontalSpacer = QSpacerItem(312, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.l_8 = QLabel(self.widget)
        self.l_8.setObjectName(u"l_8")
        self.l_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.l_8)

        self.nroGolpes = QLabel(self.widget)
        self.nroGolpes.setObjectName(u"nroGolpes")
        self.nroGolpes.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.nroGolpes)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.servidor = QLabel(self.widget)
        self.servidor.setObjectName(u"servidor")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.servidor.sizePolicy().hasHeightForWidth())
        self.servidor.setSizePolicy(sizePolicy)
        self.servidor.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.servidor.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.servidor)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout_2.addWidget(self.widget)

        self.tabs = QTabWidget(self.cp)
        self.tabs.setObjectName(u"tabs")
        self.filtroTiempo = QWidget()
        self.filtroTiempo.setObjectName(u"filtroTiempo")
        self.verticalLayout_10 = QVBoxLayout(self.filtroTiempo)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.filtroTiempo)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.t_sim_2 = QFrame(self.filtroTiempo)
        self.t_sim_2.setObjectName(u"t_sim_2")
        self.t_sim_2.setFrameShape(QFrame.StyledPanel)
        self.t_sim_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.t_sim_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.t_sim_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_13.addWidget(self.label_7)


        self.gridLayout.addWidget(self.t_sim_2, 0, 0, 1, 1)

        self.t_molde_2 = QFrame(self.filtroTiempo)
        self.t_molde_2.setObjectName(u"t_molde_2")
        self.t_molde_2.setFrameShape(QFrame.StyledPanel)
        self.t_molde_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.t_molde_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.t_molde_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_14.addWidget(self.label_9)


        self.gridLayout.addWidget(self.t_molde_2, 0, 1, 1, 1)

        self.scMa = QScrollArea(self.filtroTiempo)
        self.scMa.setObjectName(u"scMa")
        self.scMa.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 376, 295))
        self.scMa.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout.addWidget(self.scMa, 1, 0, 1, 1)

        self.scMo = QScrollArea(self.filtroTiempo)
        self.scMo.setObjectName(u"scMo")
        self.scMo.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 376, 295))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label = QLabel(self.scrollAreaWidgetContents_4)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_16.addWidget(self.label)

        self.molde1 = QComboBox(self.scrollAreaWidgetContents_4)
        self.molde1.addItem("")
        self.molde1.setObjectName(u"molde1")
        font1 = QFont()
        font1.setPointSize(11)
        self.molde1.setFont(font1)

        self.horizontalLayout_16.addWidget(self.molde1)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_2 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_2)

        self.molde2 = QComboBox(self.scrollAreaWidgetContents_4)
        self.molde2.addItem("")
        self.molde2.setObjectName(u"molde2")
        self.molde2.setFont(font1)

        self.horizontalLayout_17.addWidget(self.molde2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_3)

        self.molde3 = QComboBox(self.scrollAreaWidgetContents_4)
        self.molde3.addItem("")
        self.molde3.setObjectName(u"molde3")
        self.molde3.setFont(font1)

        self.horizontalLayout_18.addWidget(self.molde3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_4)

        self.molde4 = QComboBox(self.scrollAreaWidgetContents_4)
        self.molde4.addItem("")
        self.molde4.setObjectName(u"molde4")
        self.molde4.setFont(font1)

        self.horizontalLayout_19.addWidget(self.molde4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setFont(font)

        self.horizontalLayout_20.addWidget(self.label_12)

        self.molde5 = QComboBox(self.scrollAreaWidgetContents_4)
        self.molde5.addItem("")
        self.molde5.setObjectName(u"molde5")
        self.molde5.setFont(font1)

        self.horizontalLayout_20.addWidget(self.molde5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_20)

        self.scMo.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout.addWidget(self.scMo, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 6)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_9.addLayout(self.gridLayout)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_5 = QFrame(self.filtroTiempo)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_16.addWidget(self.label_13)


        self.verticalLayout_15.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.filtroTiempo)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.mm_1 = QLabel(self.frame_6)
        self.mm_1.setObjectName(u"mm_1")
        sizePolicy1.setHeightForWidth(self.mm_1.sizePolicy().hasHeightForWidth())
        self.mm_1.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.mm_1)

        self.mm_17 = QLabel(self.frame_6)
        self.mm_17.setObjectName(u"mm_17")
        sizePolicy1.setHeightForWidth(self.mm_17.sizePolicy().hasHeightForWidth())
        self.mm_17.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.mm_17)

        self.mm_11 = QLabel(self.frame_6)
        self.mm_11.setObjectName(u"mm_11")
        sizePolicy1.setHeightForWidth(self.mm_11.sizePolicy().hasHeightForWidth())
        self.mm_11.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.mm_11)


        self.verticalLayout_17.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.mm_2 = QLabel(self.frame_6)
        self.mm_2.setObjectName(u"mm_2")
        sizePolicy1.setHeightForWidth(self.mm_2.sizePolicy().hasHeightForWidth())
        self.mm_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.mm_2)

        self.mm_20 = QLabel(self.frame_6)
        self.mm_20.setObjectName(u"mm_20")
        sizePolicy1.setHeightForWidth(self.mm_20.sizePolicy().hasHeightForWidth())
        self.mm_20.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.mm_20)

        self.mm_12 = QLabel(self.frame_6)
        self.mm_12.setObjectName(u"mm_12")
        sizePolicy1.setHeightForWidth(self.mm_12.sizePolicy().hasHeightForWidth())
        self.mm_12.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.mm_12)


        self.verticalLayout_17.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.mm_3 = QLabel(self.frame_6)
        self.mm_3.setObjectName(u"mm_3")
        sizePolicy1.setHeightForWidth(self.mm_3.sizePolicy().hasHeightForWidth())
        self.mm_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_12.addWidget(self.mm_3)

        self.mm_23 = QLabel(self.frame_6)
        self.mm_23.setObjectName(u"mm_23")
        sizePolicy1.setHeightForWidth(self.mm_23.sizePolicy().hasHeightForWidth())
        self.mm_23.setSizePolicy(sizePolicy1)

        self.horizontalLayout_12.addWidget(self.mm_23)

        self.mm_13 = QLabel(self.frame_6)
        self.mm_13.setObjectName(u"mm_13")
        sizePolicy1.setHeightForWidth(self.mm_13.sizePolicy().hasHeightForWidth())
        self.mm_13.setSizePolicy(sizePolicy1)

        self.horizontalLayout_12.addWidget(self.mm_13)


        self.verticalLayout_17.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.mm_4 = QLabel(self.frame_6)
        self.mm_4.setObjectName(u"mm_4")
        sizePolicy1.setHeightForWidth(self.mm_4.sizePolicy().hasHeightForWidth())
        self.mm_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_13.addWidget(self.mm_4)

        self.mm_26 = QLabel(self.frame_6)
        self.mm_26.setObjectName(u"mm_26")
        sizePolicy1.setHeightForWidth(self.mm_26.sizePolicy().hasHeightForWidth())
        self.mm_26.setSizePolicy(sizePolicy1)

        self.horizontalLayout_13.addWidget(self.mm_26)

        self.mm_14 = QLabel(self.frame_6)
        self.mm_14.setObjectName(u"mm_14")
        sizePolicy1.setHeightForWidth(self.mm_14.sizePolicy().hasHeightForWidth())
        self.mm_14.setSizePolicy(sizePolicy1)

        self.horizontalLayout_13.addWidget(self.mm_14)


        self.verticalLayout_17.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.mm_5 = QLabel(self.frame_6)
        self.mm_5.setObjectName(u"mm_5")
        sizePolicy1.setHeightForWidth(self.mm_5.sizePolicy().hasHeightForWidth())
        self.mm_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_14.addWidget(self.mm_5)

        self.mm_29 = QLabel(self.frame_6)
        self.mm_29.setObjectName(u"mm_29")
        sizePolicy1.setHeightForWidth(self.mm_29.sizePolicy().hasHeightForWidth())
        self.mm_29.setSizePolicy(sizePolicy1)

        self.horizontalLayout_14.addWidget(self.mm_29)

        self.mm_15 = QLabel(self.frame_6)
        self.mm_15.setObjectName(u"mm_15")
        sizePolicy1.setHeightForWidth(self.mm_15.sizePolicy().hasHeightForWidth())
        self.mm_15.setSizePolicy(sizePolicy1)

        self.horizontalLayout_14.addWidget(self.mm_15)


        self.verticalLayout_17.addLayout(self.horizontalLayout_14)


        self.verticalLayout_15.addWidget(self.frame_6)

        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 6)

        self.verticalLayout_9.addLayout(self.verticalLayout_15)


        self.horizontalLayout_21.addLayout(self.verticalLayout_9)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(self.filtroTiempo)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.filtroTiempo)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.year = QComboBox(self.widget_4)
        self.year.addItem("")
        self.year.setObjectName(u"year")
        font2 = QFont()
        font2.setPointSize(12)
        self.year.setFont(font2)

        self.horizontalLayout_3.addWidget(self.year)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 4)

        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_5 = QWidget(self.filtroTiempo)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_8)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.widgetm = QWidget(self.filtroTiempo)
        self.widgetm.setObjectName(u"widgetm")
        self.horizontalLayout_5 = QHBoxLayout(self.widgetm)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.month = QComboBox(self.widgetm)
        self.month.addItem("")
        self.month.setObjectName(u"month")
        self.month.setFont(font2)

        self.horizontalLayout_5.addWidget(self.month)


        self.verticalLayout_4.addWidget(self.widgetm)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 4)

        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_7 = QWidget(self.filtroTiempo)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_10)


        self.verticalLayout_5.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.filtroTiempo)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.day = QComboBox(self.widget_8)
        self.day.addItem("")
        self.day.setObjectName(u"day")
        self.day.setFont(font2)

        self.horizontalLayout_7.addWidget(self.day)


        self.verticalLayout_5.addWidget(self.widget_8)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 4)

        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_9 = QWidget(self.filtroTiempo)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_11 = QLabel(self.widget_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_11)


        self.verticalLayout_6.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.filtroTiempo)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.turno = QComboBox(self.widget_10)
        self.turno.addItem("")
        self.turno.setObjectName(u"turno")
        self.turno.setFont(font2)

        self.horizontalLayout_9.addWidget(self.turno)


        self.verticalLayout_6.addWidget(self.widget_10)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 4)

        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.widget_22 = QWidget(self.filtroTiempo)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.botonSql1 = QPushButton(self.widget_22)
        self.botonSql1.setObjectName(u"botonSql1")
        font3 = QFont()
        font3.setPointSize(9)
        self.botonSql1.setFont(font3)
        self.botonSql1.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.botonSql1)

        self.botonSql2 = QPushButton(self.widget_22)
        self.botonSql2.setObjectName(u"botonSql2")
        self.botonSql2.setFont(font3)

        self.horizontalLayout_15.addWidget(self.botonSql2)


        self.verticalLayout_7.addWidget(self.widget_22)

        self.servidor_2 = QLabel(self.filtroTiempo)
        self.servidor_2.setObjectName(u"servidor_2")
        self.servidor_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.servidor_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.servidor_2)

        self.verticalLayout_7.setStretch(0, 2)
        self.verticalLayout_7.setStretch(1, 2)
        self.verticalLayout_7.setStretch(2, 2)
        self.verticalLayout_7.setStretch(3, 2)
        self.verticalLayout_7.setStretch(4, 1)
        self.verticalLayout_7.setStretch(5, 1)

        self.horizontalLayout_21.addLayout(self.verticalLayout_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_21)

        self.tabs.addTab(self.filtroTiempo, "")

        self.verticalLayout_2.addWidget(self.tabs)

        MainWindow.setCentralWidget(self.cp)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 982, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionConexion_SQL)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConexion_SQL.setText(QCoreApplication.translate("MainWindow", u"Conexion SQL", None))
        self.nroMaquina.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Sistema Industrial de Monitoreo</span></p></body></html>", None))
        self.l_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#55ffff;\">Nro Golpes</span></p></body></html>", None))
        self.nroGolpes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#55ffff;\">N/A</span></p></body></html>", None))
        self.servidor.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Servidor</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#55ffff;\">Filtros de Tiempo-Maquinas-Moldes</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#97fff6;\">Seleccione Maquinas (Max 5)</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#97fff6;\">Seleccione Moldes (Max 5)</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#55ffff;\">Molde 1</span></p></body></html>", None))
        self.molde1.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccione un Molde", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#55ffff;\">Molde 2</span></p></body></html>", None))
        self.molde2.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccione un Molde", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#55ffff;\">Molde 3</span></p></body></html>", None))
        self.molde3.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccione un Molde", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#55ffff;\">Molde 4</span></p></body></html>", None))
        self.molde4.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccione un Molde", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#55ffff;\">Molde 5</span></p></body></html>", None))
        self.molde5.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccione un Molde", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#97fff6;\">Maquinas y Moldes que Seleccion\u00f3</span></p></body></html>", None))
        self.mm_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">N/A</span></p></body></html>", None))
        self.mm_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">----------&gt;</span></p></body></html>", None))
        self.mm_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">N/A</span></p></body></html>", None))
        self.mm_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">N/A</span></p></body></html>", None))
        self.mm_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">----------&gt;</span></p></body></html>", None))
        self.mm_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">N/A</span></p></body></html>", None))
        self.mm_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">N/A</span></p></body></html>", None))
        self.mm_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">----------&gt;</span></p></body></html>", None))
        self.mm_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">N/A</span></p></body></html>", None))
        self.mm_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">N/A</span></p></body></html>", None))
        self.mm_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">----------&gt;</span></p></body></html>", None))
        self.mm_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">N/A</span></p></body></html>", None))
        self.mm_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">N/A</span></p></body></html>", None))
        self.mm_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">----------&gt;</span></p></body></html>", None))
        self.mm_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#55ffff;\">N/A</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#97fff6;\">A\u00f1o</span></p></body></html>", None))
        self.year.setItemText(0, QCoreApplication.translate("MainWindow", u"A\u00f1o", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#97fff6;\">Mes</span></p></body></html>", None))
        self.month.setItemText(0, QCoreApplication.translate("MainWindow", u"Mes", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#97fff6;\">Dia</span></p></body></html>", None))
        self.day.setItemText(0, QCoreApplication.translate("MainWindow", u"Dia", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#97fff6;\">Turno</span></p></body></html>", None))
        self.turno.setItemText(0, QCoreApplication.translate("MainWindow", u"Turno", None))

        self.botonSql1.setText(QCoreApplication.translate("MainWindow", u"Consulta", None))
        self.botonSql2.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.servidor_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Servidor</span></p></body></html>", None))
        self.tabs.setTabText(self.tabs.indexOf(self.filtroTiempo), QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

