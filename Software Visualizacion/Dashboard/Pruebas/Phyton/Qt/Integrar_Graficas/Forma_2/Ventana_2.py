import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5 import uic
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Canvas(FigureCanvas):
    def __init__(self, parent):
        #fig, self.ax = plt.subplots(figsize=(width/200, height/200), dpi=200)
        fig = plt.figure()

        #self.axes = fig.add_subplot(111)
        super().__init__(fig) #Herencia de Constructores
        self.setParent(parent) #Creo que setea el frame donde se dibuja
        #self.ploteo() #LLamo a funcion que grafica
        
    def ploteo(self):
        #-------------Matplotlib Script--------------------
        manzanas = [20,10,25,30]
        nombres = ["Ana","Juan","Diana","Catalina"]
        colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
        plt.pie(manzanas,labels=nombres, autopct="%0.1f %%", colors=colores)
        plt.axis("equal")
        #plt.show() #si ejecuto este comando se muestra otra figura aparte

class Canvas2(FigureCanvas):
    def __init__(self, parent):
        #fig, self.ax = plt.subplots(figsize=(width/200, height/200), dpi=200)
        fig = plt.figure()

        #self.axes = fig.add_subplot(111)
        super().__init__(fig) #Herencia de Constructores
        self.setParent(parent) #Creo que setea el frame donde se dibuja
        #self.ploteo() #LLamo a funcion que grafica
        
    def ploteo(self):
        #-------------Matplotlib Script--------------------
        manzanas = [20,10,25,30]
        nombres = ["A","J","D","C"]
        colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
        plt.pie(manzanas,labels=nombres, autopct="%0.1f %%", colors=colores)
        plt.axis("equal")
        #plt.show() #si ejecuto este comando se muestra otra figura aparte

#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("MainWindow2.ui", self) #Esto sale del programa de diseño de iterfax y no lo tengo
        self.setWindowTitle("Cambiando el título de la ventana")
        #Creo los layout que van a ser seteados dentro de cada widget
        vertical_layout1 = QVBoxLayout()
        vertical_layout2 = QVBoxLayout()
        
        #Creo la grafica, la agrego al layout 1 y la seteo en el widget de dibujo_1
        Graficar=Canvas(self.dibujo1)
        vertical_layout1.addWidget(Graficar)
        self.dibujo1.setLayout(vertical_layout1)
        Graficar.ploteo()

        #Creo la grafica, la agrego al layout 2 y la seteo en el widget de dibujo_2
        Graficar2=Canvas2(self.dibujo2)
        vertical_layout1.addWidget(Graficar2)
        self.dibujo2.setLayout(vertical_layout2)
        Graficar2.ploteo()
        
        #self.setCentralWidget(Graficar)

  
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()