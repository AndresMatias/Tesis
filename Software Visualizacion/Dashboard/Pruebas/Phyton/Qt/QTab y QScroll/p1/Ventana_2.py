import sys

from PyQt5 import uic
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        # uic.loadUi("interfaz.ui", self) #Esto sale del programa de diseño de interfaz y no lo tengo
        self.initUI()
    def initUI(self):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        for i in range(1,15):
            # object = QLabel("TextLabel")
            # self.vbox.addWidget(object)
            object = QWidget()
            object.setMinimumSize(50,100)
            object.setStyleSheet('background-color: #55ffff;')
            self.vbox.addWidget(object)
        # # self.contenedorObjeto2.setMinimumSize(50,100)
            

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()

        return

#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()