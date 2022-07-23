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

#-------Clase Graficadora2-------------
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

#-------------Hilo Qt----------------
class HiloQ(QThread):
    sig = pyqtSignal(str)
    
    def __init__(self,Grafica,parent=None):
        super(HiloQ, self).__init__(parent)
        self.Grafica=Grafica
    
    def run(self):  
        self.Grafica.ploteo([1,2,3,4],[1,2,1,2],[10,11,12,13,14],[5,6,7,6,5])

    def graficar(self,x1,y1,x2,y2):
        self.Grafica.ploteo(x1,y1,x2,y2)



class Ventana(QMainWindow):
    #Método constructor de la clase
    sig2=pyqtSignal(list,list,list,list)
    def __init__(self):
        self.i=0
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ventana.ui", self) #Esto sale del programa de diseño de interfaz y no lo tengo
        # self.graficar=Grafico('red',self.grafico)
        # self.graficar.ploteo([1,2,3,4],[1,2,1,2],[10,11,12,13,14],[5,6,7,6,5])
        self.MiGrafica=Grafico('red',self.grafico)
        #-----------HiloQ---------------
        self.thread2 = HiloQ(self.MiGrafica)
        self.sig2.connect(self.thread2.graficar) #Conecto Señal
        self.thread2.start()
        
        self.pushButton.clicked.connect(self.buttonClicked2)          
    
    def buttonClicked2(self):
        self.i=self.i+1
        self.updateGrafico(self.i)
    
    def updateGrafico(self, i):
        self.sig2.emit([1+i,2+i,3+i,4+i],[1,2,1,2],[10+i,11+i,12+i,13+i,14+i],[5,6,7,6,5])

    


#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()