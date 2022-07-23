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
       
        self.vertical_layout = QVBoxLayout()
        
        self.fig1=plt.Figure(facecolor='#92edff') #Figura contendra mi dibujo y adentro determino color de fondo tambien en vez de hexa puedo usar rgb o rgba ej:(.18, .31, .31)
        self.__circulo=self.fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi circulo
        self.parent=parent
        super().__init__(self.fig1) #Herencia de Constructores
        self.setParent(self.parent) #Creo que setea el frame donde se dibuja
        self.vertical_layout.addWidget(self) #Funciona despues de set parent nose porque
        self.parent.setLayout(self.vertical_layout)
  
    def ploteo(self,manzanas,nombres):
        #Si no ejecuto esta parte del codigo seguido al dibujo no actualiza ¿pq? nose
   
        #-------------Matplotlib Script--------------------
        #colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
        #self.circulo.pie(manzanas,labels=nombres, autopct="%0.1f %%", colors=colores)
        self.__circulo.clear()
        self.__circulo.pie(manzanas,labels=nombres, autopct="%0.1f %%")  
        self.__circulo.axis("equal")
        #Actualizar dibujo
        self.fig1.canvas.draw()
        #self.circulo.axes.set_facecolor((.18, .31, .31))

class Canvas2(FigureCanvas):
    def __init__(self, parent):
        vertical_layout = QVBoxLayout()
        self.fig1=plt.Figure() #Figura contendra mi dibujo
        self.__gauge=self.fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi circuilo
        super().__init__(self.fig1) #Herencia de Constructores
        self.setParent(parent) #Creo que setea el frame donde se dibuja
        vertical_layout.addWidget(self) #Funciona despues de set parent nose porque
        parent.setLayout(vertical_layout)
           
        
    def ploteo(self,porcetaje):
        #El calculo del angulo porcentaje
        anguloPorcentaje=180-(porcetaje*180)/100
        #----------Configuraciones Iniciales antes de cada dibuejo
        self.__gauge.clear() #Borro todo lo que hay en gauge
        self.__gauge.axis("off") #Desactivo Ejes
        self.__gauge.set_ylim(0,6)
        self.__gauge.set_xlim(-9,9)  
        #--------------Limites externos-------------
        pac1 = mpatches.Arc([0, 0], 10, 10, 0, theta1=0, theta2=180, hatch = '') # Limite Superior
        pac2 = mpatches.Arc([0, 0], 4, 4, 0, theta1=0, theta2=180, hatch = '') # Limite inferior
        pac1.set_color('cyan')
        pac2.set_color('cyan')
        self.__gauge.add_patch(pac1)
        self.__gauge.add_patch(pac2)
        #--------------Limites internos----------------
        pac3 = mpatches.Arc([0, 0], 8, 8, 0, theta1=0, theta2=180, hatch = '') # Limite Superior
        pac4 = mpatches.Arc([0, 0], 6, 6, 0, theta1=0, theta2=180, hatch = '') # Limite inferior
        pac3.set_color('red')
        pac4.set_color('red')
        self.__gauge.add_patch(pac3)
        self.__gauge.add_patch(pac4)
        #---------------Relleno-----------------------
        lista=np.arange(6, 8, 0.01) #Nro de arcos
        vector=np.array(lista)
        for i in range(0,len(vector)):
            #pacn= mpatches.Arc([0, 0], vector[i], vector[i], 0, theta1=120, theta2=180, hatch = '')
            pacn= mpatches.Arc([0, 0], vector[i], vector[i], 0, theta1=anguloPorcentaje, theta2=180, hatch = '')
            pacn.set_color('green')
            self.__gauge.add_patch(pacn)
        #Actualizo Dibujo    
        self.fig1.canvas.draw()     

class Canvas3(FigureCanvas):
    def __init__(self, parent):
        vertical_layout = QVBoxLayout()
        self.fig1=plt.Figure() #Figura contendra mi dibujo
        self.xy=self.fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi circuilo
        super().__init__(self.fig1) #Herencia de Constructores
        self.setParent(parent) #Creo que setea el frame donde se dibuja
        vertical_layout.addWidget(self) #Funciona despues de set parent nose porque
        parent.setLayout(vertical_layout)
        self.xy.axis("off") #Desactivo Ejes
        self.xy.set_ylim(0,6)
        self.xy.set_xlim(0,9)
        
        
        
    def ploteo(self,x1,y1,x2,y2):
        self.xy.clear()
        self.xy.plot(x1,y1) #Recta uno
        self.xy.plot(x2,y2)       #Recta dos
        self.xy.plot([7,12],[1,6])       #Recta tres
        #Actualizo Dibujo
        self.fig1.canvas.draw() 
