from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import matplotlib.pyplot  as ylim
import matplotlib.pyplot
import numpy as np
import random
import matplotlib.patches as mpatches
 


class Grafico_2(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.fig1=plt.Figure() #Figura contendra mi dibujo gauge
        self.gauge=self.fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi gauge
        self.canvas = FigureCanvas(self.fig1) #Usando plt.figure pq esta devuelve un Objeto tipo Figure()
        vertical_layout = QVBoxLayout() #Layout 
        vertical_layout.addWidget(self.canvas) #Agrego mi lienzo al layout
        self.setLayout(vertical_layout)#Agrego el layout al widget
        self.gauge.axis("off") #Desactivo Ejes
        #self.gauge.axis(xmin=0,xmax=8)
        self.gauge.set_ylim(0,6)
        self.gauge.set_xlim(-9,9)
 
        #self.ploteo()
    
    def ploteo(self):
        #Averiguar como borrar lineas de arcos o mas bien actualizar grafico
        #--------------Limites externos-------------
        pac1 = mpatches.Arc([0, 0], 10, 10, 0, theta1=0, theta2=180, hatch = '') # Limite Superior
        pac2 = mpatches.Arc([0, 0], 4, 4, 0, theta1=0, theta2=180, hatch = '') # Limite inferior
        pac1.set_color('cyan')
        pac2.set_color('cyan')
        self.gauge.add_patch(pac1)
        self.gauge.add_patch(pac2)
        #--------------Limites internos----------------
        pac3 = mpatches.Arc([0, 0], 8, 8, 0, theta1=0, theta2=180, hatch = '') # Limite Superior
        pac4 = mpatches.Arc([0, 0], 6, 6, 0, theta1=0, theta2=180, hatch = '') # Limite inferior
        pac3.set_color('red')
        pac4.set_color('red')
        self.gauge.add_patch(pac3)
        self.gauge.add_patch(pac4)
        #---------------Relleno-----------------------
        lista=np.arange(6, 8, 0.01) #Nro de arcos
        vector=np.array(lista)
        for i in range(0,len(vector)):
            pacn= mpatches.Arc([0, 0], vector[i], vector[i], 0, theta1=120, theta2=180, hatch = '')
            pacn.set_color('green')
            self.gauge.add_patch(pacn)      
        
