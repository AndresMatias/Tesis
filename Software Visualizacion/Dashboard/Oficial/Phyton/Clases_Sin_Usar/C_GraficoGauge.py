from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import matplotlib.pyplot  as ylim
import matplotlib.pyplot
import numpy as np
import random
import matplotlib.patches as mpatches
 


class GraficoGauge(QWidget):
    
    def __init__(self, colorW, parent = None):
        QWidget.__init__(self, parent)
        self.__fig1=plt.Figure(facecolor=colorW) #Figura contendra mi dibujo gauge
        self.__gauge=self.__fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi gauge
        self.__canvas = FigureCanvas(self.__fig1) #Usando plt.figure pq esta devuelve un Objeto tipo Figure()
        vertical_layout = QVBoxLayout() #Layout 
        vertical_layout.addWidget(self.__canvas) #Agrego mi lienzo al layout
        parent.setLayout(vertical_layout)#Agrego el layout al widget
        self.__gauge.axis("off") #Desactivo ejes
    
    def ploteo(self,porcetaje):
        #El calculo del angulo porcentaje
        anguloPorcentaje=180-(porcetaje*180)/100
        #----------Configuraciones Iniciales antes de cada dibujo
        self.__gauge.clear() #Borro todo lo que hay en gauge
        self.__gauge.axis("off") #Desactivo Ejes
        self.__gauge.set_ylim(0,6)
        self.__gauge.set_xlim(-9,9)
        #--------Constantes de Ajuste------------------
        cte1=[1.5,0.5] #Ajuste de tamaño de arco
        cte2=[0,1] #Punto de ubicancion del arco
        #--------------Limites externos-------------
        pac1 = mpatches.Arc(cte2, 10*cte1[0], 10*cte1[1], 0, theta1=0, theta2=180, hatch = '') # Limite Superior
        pac2 = mpatches.Arc(cte2, 4*cte1[0], 4*cte1[1], 0, theta1=0, theta2=180, hatch = '') # Limite inferior
        pac1.set_color('cyan')
        pac2.set_color('cyan')
        self.__gauge.add_patch(pac1)
        self.__gauge.add_patch(pac2)
        #--------------Limites internos----------------
        pac3 = mpatches.Arc(cte2, 8*cte1[0], 8*cte1[1], 0, theta1=0, theta2=180, hatch = '') # Limite Superior
        pac4 = mpatches.Arc(cte2, 6*cte1[0], 6*cte1[1], 0, theta1=0, theta2=180, hatch = '') # Limite inferior
        pac3.set_color('red')
        pac4.set_color('red')
        self.__gauge.add_patch(pac3)
        self.__gauge.add_patch(pac4)
        #---------------Relleno-----------------------
        lista=np.arange(6, 8, 0.01) #Nro de arcos
        vector=np.array(lista)
        for i in range(0,len(vector)):
            pacn= mpatches.Arc(cte2, vector[i]*cte1[0], vector[i]*cte1[1], 0, theta1=anguloPorcentaje, theta2=180, hatch = '')
            pacn.set_color('green')
            self.__gauge.add_patch(pacn)
        #Actualizo Dibujo    
        self.__fig1.canvas.draw()  
