from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

import matplotlib.pyplot as plt
 
from matplotlib.lines import Line2D

import numpy as np

class GraficoBarras(QWidget):
    
    def __init__(self, colorW, parent):
        """ En el constructor se ejecutan configuraciones iniciales para que el dibujo se cree y amolde al tamaño del widget
            \nArgumentos:
                colorW: color de fondo de grafico
                parent: widget en donde se desea implementar el grafico """
        QWidget.__init__(self, parent)
        self.__colorW=colorW
        self.__fig1=plt.Figure(facecolor=self.__colorW) #Figura contendra mi dibujo xy
        self.__barras=self.__fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi xy
        self.canvas = FigureCanvas(self.__fig1) #Usando plt.figure pq esta devuelve un Objeto tipo Figure()
        vertical_layout = QVBoxLayout() #Layout 
        vertical_layout.addWidget(self.canvas) #Agrego mi lienzo al layout
        parent.setLayout(vertical_layout)#Agrego el layout al widget
        self.__barras.axis("off") #Desactivo Ejes
    
    def ploteo(self,vel,colorV,Indicadores,tiempos,ejes):
        """ Metodo que grafica y actualiza barras, no devuelve nada
            \nArgumentos:
                vel: vector que contiene las velocidades a graficar
                colorV: color correspendiente a cada velocidad del vector vel
                Indicadores: Vector utilizado en la leyenda(legend) para indicar que significa cada color
                tiempos: contiene las divisiones en el eje y para graficar barras separadoras de fondo
                ejes: Nombre de los ejes x e y """
                     
        color='#FFFFFF'
        #------Configuracion Ejes-------
        self.__barras.clear()#Borro todo lo que hay 
        self.__barras.axis("off") #Desactivo Ejes
        
        #-----Nombre de Ejes---------
        self.__barras.set_xlabel(ejes[0],color=color,labelpad=0)
        self.__barras.set_ylabel(ejes[1],color=color)

        #-----Lineas divisorias de tiempo-------
        #Variables locales para manejar la configuracion de las posiciones de las etiquetas etc
        tam=sum(vel) #Largo que va a ocupar en la grafica el vector color
        alturaY=-0.15 #Alturas de las etiquetas de tiempo en el eje y
        delta=0.035 #Controla el movimiento de las etiquetas de tiempo en el eje x
        if tam!=0:  
            self.__barras.text(tam*(-delta),alturaY,tiempos[0],fontsize=10,color=color)
            self.__barras.text(tam*(0.25-delta),alturaY,tiempos[1],fontsize=10,color=color)
            self.__barras.text(tam*(0.50-delta),alturaY,tiempos[2],fontsize=10,color=color)
            self.__barras.text(tam*(0.75-delta),alturaY,tiempos[3],fontsize=10,color=color)
            self.__barras.text(tam*(1-delta),alturaY,tiempos[4],fontsize=10,color=color)
            self.__barras.vlines(x=[0,tam*0.25,tam*0.50,tam*0.75,tam],ymin=0.4,ymax=1.8,color=color,linestyle=(0, (2,6)))
        
        #------Configuro Legends-------
        if Indicadores!=None:
            custom_lines = [Line2D([0], [0], color=Indicadores[1], lw=4),
                    Line2D([0], [0], color=Indicadores[2], lw=4),
                    Line2D([0], [0], color=Indicadores[3], lw=4),
                    Line2D([0], [0], color=Indicadores[4], lw=4)]
            legend=self.__barras.legend(custom_lines,["Vel baja","Vel Normal","Stand-by","Fuera de Rango"],labelcolor=[Indicadores[1],Indicadores[2],Indicadores[3],Indicadores[4]],loc=0,bbox_to_anchor=(1,1),frameon=False)
            legend.get_frame().set_facecolor(self.__colorW) #Color de fondo de legend
        
        #--------------------------Grafica de Datos------------------------------
        year=["Estados"]
        posX=0
        self.__barras.barh("  ",1,height=0.1,color=self.__colorW)  #Para Centrar la barra
        for i in range(0,len(vel)):
            self.__barras.barh(year,vel[i],color=colorV[i],left=posX)
            posX=posX+vel[i] #Determina la poscion en el eje x para graficar la siguiente barra
            #self.__fig1.canvas.draw()   #El programa no se clava pero actualiza lento tengo que ver que hace
        self.__barras.barh(" ",1,height=0.1,color=self.__colorW) #Para Centrar la barra
    
        #----------------Actualizo Dibujo-----------------
        self.__fig1.canvas.draw()   #Actualizar dibujo	
        
