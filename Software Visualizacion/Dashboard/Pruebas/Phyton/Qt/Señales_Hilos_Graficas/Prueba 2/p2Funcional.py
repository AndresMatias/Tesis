import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
 
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pyplot as plt

import threading

#-------Clase Graficadora-------------
class Grafico(QWidget):
    
    def __init__(self, colorW, parent):
        """ En el constructor se ejecutan configuraciones iniciales para que el dibujo se cree y amolde al tamaño del widget
            \nArgumentos:
                colorW: color de fondo de grafico
                parent: widget en donde se desea implementar el grafico """
        QWidget.__init__(self, parent)
        self.__colorW=colorW
        self.__fig1=plt.Figure(facecolor=self.__colorW) #Figura contendra mi dibujo xy
        self.xy=self.__fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi xy
        self.canvas = FigureCanvas(self.__fig1) #Usando plt.figure pq esta devuelve un Objeto tipo Figure()
        vertical_layout = QVBoxLayout() #Layout 
        vertical_layout.addWidget(self.canvas) #Agrego mi lienzo al layout
        parent.setLayout(vertical_layout)#Agrego el layout al widget
        self.xy.axis("off") #Desactivo Ejes
    
    def ploteo(self,x1,y1,x2,y2):
        self.xy.clear()
        self.xy.plot(x1,y1) #Recta uno
        self.xy.plot(x2,y2)       #Recta dos
        self.xy.plot([7,12],[1,6])       #Recta tres
        self.__fig1.canvas.draw()   #Actualizar dibujo	

#-------------Hilo multiproceso----------------
class MiThread(threading.Thread):  
    sig = pyqtSignal(str)
    def __init__(self, padre,color):  
        threading.Thread.__init__(self)  
        self.padre=padre
        self.color=color
        self.MiGrafico=Grafico(color,padre)
    
    def run(self):  
        self.MiGrafico.ploteo([1,2,3,4],[1,2,1,2],[10,11,12,13,14],[5,6,7,6,5])


class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ventana.ui", self) #Esto sale del programa de diseño de interfaz y no lo tengo
        #-----------HiloQ---------------
        self.thread1 = MiThread(self.grafico,'red')
        self.pushButton.clicked.connect(self.buttonClicked2)          
    
    def buttonClicked2(self):
        self.thread1.start()

    


#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()