from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

import matplotlib.pyplot as plt

class GraficoPastel(QWidget):
    """La clase Grafico_Pastel grafica datos en formato pastel mediante la libreria matplot"""
    def __init__(self, colorW, parent = None):
        """ En el constructor se llevan a acabo las configuraciones iniciales para que el grafico se adapte bien al tamaño del widget """
        vertical_layout = QVBoxLayout() #Layout 
        QWidget.__init__(self, parent)#Indico que esta clase va a tener por padre al argumento pasado en el constructor
        self.__fig1=plt.Figure(facecolor=colorW) #Figura contendra mi dibujo
        self.__circulo=self.__fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi circuilo
        canvas=FigureCanvas(self.__fig1) #Usando plt.figure pq esta devuelve un Objeto tipo Figure()
        vertical_layout.addWidget(canvas) #Agrego Mi lienzo al layout
        parent.setLayout(vertical_layout)#Agrego el layout al widget
        self.__circulo.axis("off") #Desactivo Ejes
        #print("Color background:"+color)

    def ploteo(self,tuplaNombres,tuplaDatos):
        """Metodo para graficar y actulizar grafico"""
        self.__circulo.clear() #Limpio el grafico antes volver a graficar
        #colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"] #COnfiguracion de colores de cada seccion del grafico
        #self.__circulo.pie(datos,labels=nombres, autopct="%0.1f %%", colors=colores) #Grafico datos con colores
        self.__circulo.pie(tuplaDatos,labels=tuplaNombres, autopct="%0.1f %%") #Grafico datos
        self.__circulo.axis("equal")
        #Actualizar dibujo
        self.__fig1.canvas.draw()
