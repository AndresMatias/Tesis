import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize=(3, 3), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

        """ 
        Matplotlib Script
        """
        manzanas = [20,10,25,30]
        nombres = ["Ana","Juan","Diana","Catalina"]
        colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
        plt.pie(manzanas,labels=nombres, autopct="%0.1f %%", colors=colores)
        plt.axis("equal")
#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("MainWindow.ui", self) #Esto sale del programa de diseño de iterfax y no lo tengo
        self.setWindowTitle("Cambiando el título de la ventana")
        Graficar=Canvas(self)
  
  
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()