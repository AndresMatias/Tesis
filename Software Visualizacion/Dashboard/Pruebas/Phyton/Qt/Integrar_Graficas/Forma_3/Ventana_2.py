import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5 import uic
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Graficas import *


#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("MainWindow2.ui", self) #Esto sale del programa de diseño de iterfax y no lo tengo
        self.setWindowTitle("Cambiando el título de la ventana")
        #Pongo a la escucha al boton1
        self.boton1.clicked.connect(self.botonA)
        #Valores de Prueba
        manzanas = [20,10,25,30]
        nombres = ["Ana","Juan","Diana","Catalina"]
        self.x1=[1,2,3,4]
        self.y1=self.x1 
        self.x2=[4,5,6,7]
        self.y2=[3,2,1,1] 
        #Grafico todo
        
        self.Grafica1=Canvas(self.dibujo1) #Circulo 
        self.Grafica2=Canvas2(self.dibujo2) #Gauge
        self.Grafica3=Canvas3(self.dibujo3) #Recta

        self.Grafica1.ploteo(manzanas,nombres)
        self.Grafica2.ploteo(50)
        self.Grafica3.ploteo(self.x1,self.y1,self.x2,self.y2)

    def botonA(self):   
        self.Grafica1.ploteo([10,10,1],["a","b","c"])
        self.Grafica3.ploteo([1,2,3,4],[1,2,1,2],[10,11,12,13,14],[5,6,7,6,5])
        self.Grafica2.ploteo(10)


  
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()