import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5 import uic
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.patches as mpatches

class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig1=plt.Figure(facecolor='#92edff') #Figura contendra mi dibujo y adentro determino color de fondo tambien en vez de hexa puedo usar rgb o rgba ej:(.18, .31, .31)
        self.circulo=self.fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi circuilo
        super().__init__(self.fig1) #Herencia de Constructores
        self.setParent(parent) #Creo que setea el frame donde se dibuja
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self) #Funciona despues de set parent nose porque
        parent.setLayout(vertical_layout)

        
        
    def ploteo(self):
        #-------------Matplotlib Script--------------------
        manzanas = [20,10,25,30]
        nombres = ["Ana","Juan","Diana","Catalina"]
        colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
        self.circulo.pie(manzanas,labels=nombres, autopct="%0.1f %%", colors=colores)
        self.circulo.axis("equal")
        #self.circulo.axes.set_facecolor((.18, .31, .31))
        



class Canvas2(FigureCanvas):
    def __init__(self, parent):
        self.fig1=plt.Figure() #Figura contendra mi dibujo
        self.gauge=self.fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi circuilo
        super().__init__(self.fig1) #Herencia de Constructores
        self.setParent(parent) #Creo que setea el frame donde se dibuja
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self) #Funciona despues de set parent nose porque
        parent.setLayout(vertical_layout)
        self.gauge.axis("off") #Desactivo Ejes
        self.gauge.set_ylim(0,6)
        self.gauge.set_xlim(-9,9)     
        
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

class Canvas3(FigureCanvas):
    def __init__(self, parent):
        self.fig1=plt.Figure() #Figura contendra mi dibujo
        self.xy=self.fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi circuilo
        super().__init__(self.fig1) #Herencia de Constructores
        self.setParent(parent) #Creo que setea el frame donde se dibuja
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self) #Funciona despues de set parent nose porque
        parent.setLayout(vertical_layout)
        self.xy.axis("off") #Desactivo Ejes
        self.xy.set_ylim(0,6)
        self.xy.set_xlim(0,9)
        
        
    def ploteo(self):
        self.xy.plot([1, 2, 3, 4],[1, 2, 3, 4]) #Recta uno
        self.xy.plot([4,5,6,7],[3,2,1,1])       #Recta dos
        self.xy.plot([7,12],[1,6])       #Recta tres      
