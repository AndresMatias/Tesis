from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import numpy as np
import random

class Grafico_1(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.fig1=plt.Figure() #Figura contendra mi dibujo
        self.circulo=self.fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi circuilo
        self.canvas = FigureCanvas(self.fig1) #Usando plt.figure pq esta devuelve un Objeto tipo Figure()
        vertical_layout = QVBoxLayout() #Layout 
        vertical_layout.addWidget(self.canvas) #Agrego Mi lienzo al layout
        self.setLayout(vertical_layout)#Agrego el layout al widget
            
    def ploteo(self,tupla):
        
        #-------------Matplotlib Script--------------------
        manzanas = [20,10,25,30]
        nombres =tupla
        colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
        self.circulo.pie(manzanas,labels=nombres, autopct="%0.1f %%", colors=colores)
        self.circulo.axis("equal")
