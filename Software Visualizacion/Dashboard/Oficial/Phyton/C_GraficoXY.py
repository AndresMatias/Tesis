from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas


import matplotlib.pyplot as plt

 


class GraficoXY(QWidget):
    
    def __init__(self,colorW,parent = None):
        """ En el constructor se ejecutan configuraciones iniciales para que el dibujo se cree y amolde al tamaño del widget 
        \nArgumentos:
            colorW: Color de fondo que va a tener el grafico\n
            parent: Clase padre de donde va a heredar el grafico, en este caso la clase padre va ser el QWidget que va a contener al grafico"""
        
        QWidget.__init__(self, parent)
        self.__colorW=colorW
        self.__fig1=plt.Figure(facecolor=self.__colorW) #Figura contendra mi dibujo xy 
        self.__xy=self.__fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi xy
        self.canvas = FigureCanvas(self.__fig1) #Usando plt.figure pq esta devuelve un Objeto tipo Figure()
        vertical_layout = QVBoxLayout() #Layout 
        vertical_layout.addWidget(self.canvas) #Agrego mi lienzo al layout
        parent.setLayout(vertical_layout)#Agrego el layout al widget
        self.__xy.axis("off") #Desactivo Ejes
        self.__xy.set_ylim(0,6)
        self.__xy.set_xlim(0,9)
    
    def ploteo(self,x1,y1,vDiv,ejes):
        """ Metodo que grafica y actualizar la grafica de piezas vs tiempo, no devuelve nada
        \nArgumentos:
            x1: Vector que contiene la cantidad de hs/dias/mes/turno\n
            y1: Vector que contiene la cantidad de piezas correspondiente al vector x1
            vDiv: Vector que contiene el valor de cada linea horizontal en el grafico para indicar nro de piezas a una cierta altura en el eje y\n
            ejes: Lista de dos elements con los nombres de los ejes x e y siendo el 1er elemento el nombre de x"""
        #------------Configuraciones previas a dibujar------------
        self.__xy.clear()#Borro todo lo que hay
        # self.__xy.set_xticks(x1) #Seteo los valores del eje x sin numeros con coma de por medio
        pos=list(range(0,len(x1)))
        self.__xy.set_xticks(pos)
        self.__xy.set_xticklabels(x1)
        color='#FFFFFF'
        self.__xy.set_facecolor(self.__colorW)
        self.__xy.tick_params(labelcolor=color) #Color de los valores en los ejes
        
        #-----Nombre Ejes------
        self.__xy.set_xlabel(ejes[0],color=color,labelpad=0)
        self.__xy.tick_params(axis='x', labelrotation=45) #Funciona pero no se ve bien con la resolucion en pantalla
        self.__xy.set_ylabel(ejes[1],color=color)

        #----Configuracion del recuadro de la grafica de matplot----
        self.__xy.spines['right'].set_visible(False)
        self.__xy.spines['top'].set_visible(False)
        self.__xy.spines['bottom'].set_color(color)
        self.__xy.spines['left'].set_color(color)

        #----Lineas divisorias paralelas a x--------
        if len(vDiv)>1: 
            # self.__xy.hlines(y=vDiv,xmin=0,xmax=x1[len(x1)-1],color='#737373')
            self.__xy.hlines(y=vDiv,xmin=0,xmax=pos[len(pos)-1],color='#737373')

        #------------------Grafico--------------------------
        self.__xy.plot(pos,y1,marker="o",color='#3393FF')
        for i,label in enumerate(y1):
            self.__xy.annotate(label,xy=(pos[i], y1[i]),xycoords='data',xytext=(0,+10),textcoords='offset points',color=color) #Etiqueta de cantidad de piezas en cada punto

        #------------------Actualizo Grafico-----------------
        self.__fig1.canvas.draw()#Actualizar dibujo
        
