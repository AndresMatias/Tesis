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
        uic.loadUi("interfaz2.ui", self) #Esto sale del programa de diseño de interfaz y no lo tengo
        self.tab.setStyleSheet( 'background-color: #55ffff;')
        tab1=QWidget()
        self.tabWidget.addTab(tab1,'hola')
        tab1.setStyleSheet( 'background-color: rgb(255,0,0);')

#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()