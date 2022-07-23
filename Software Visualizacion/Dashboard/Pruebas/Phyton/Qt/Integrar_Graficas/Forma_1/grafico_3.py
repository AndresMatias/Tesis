from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import matplotlib.pyplot  as ylim
import matplotlib.pyplot
import numpy as np
import random
import matplotlib.patches as mpatches
 


class Grafico_3(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.fig1=plt.Figure() #Figura contendra mi dibujo xy
        self.xy=self.fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi xy
        self.canvas = FigureCanvas(self.fig1) #Usando plt.figure pq esta devuelve un Objeto tipo Figure()
        vertical_layout = QVBoxLayout() #Layout 
        vertical_layout.addWidget(self.canvas) #Agrego mi lienzo al layout
        self.setLayout(vertical_layout)#Agrego el layout al widget
        self.xy.axis("off") #Desactivo Ejes
        self.xy.set_ylim(0,6)
        self.xy.set_xlim(0,9)
    
    def ploteo(self):
        self.xy.plot([1, 2, 3, 4],[1, 2, 3, 4]) #Recta uno
        self.xy.plot([4,5,6,7],[3,2,1,1])       #Recta dos
        self.xy.plot([7,12],[1,6])       #Recta tres
        #self.xy.ylabel('Algunos Numeros')
        
