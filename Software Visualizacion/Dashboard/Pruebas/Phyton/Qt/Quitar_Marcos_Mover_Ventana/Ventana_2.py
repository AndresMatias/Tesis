import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from Graficas import *
from PyQt5.QtCore import Qt


#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("MainWindow2.ui", self) #Esto sale del programa de diseño de iterfax y no lo tengo
        #self.setWindowFlags(Qt.FramelessWindowHint) #Este no me deja modificar nada
        self.setWindowFlags(Qt.Window | Qt.WindowSystemMenuHint | Qt.CustomizeWindowHint)# este funcioan bien solo tengo que resolver el problema de q no aprece el marco cuando acerco el curso a este
        #Grafico todo
        Grafica1=Canvas(self.dibujo1) #Circuilo
        Grafica2=Canvas2(self.dibujo2) #Gauge
        Grafica3=Canvas3(self.dibujo3) #Recta

        Grafica1.ploteo()
        Grafica2.ploteo()
        Grafica3.ploteo()
    #Esto me permite movilizarla    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
  
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()