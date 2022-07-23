import sys

from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ventana.ui", self) #Esto sale del programa de diseño de iterfax y no lo tengo
        

    def paintEvent(self, event):
        ancho=30
        alto=30
        margen=100
        valor=90 #grados
        angInicio=360
        #Pintor
        paint=QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) #Remueve pixelado

        #Creo rectangulo
        rect=QRect(0,0,ancho,alto)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        #PEN
        pen=QPen()
        pen.setColor(QColor('blue'))
        pen.setWidth(10)
        # #Set progreso_cap
        # if self.progreso_cap:
        #     pen.setCapStyle(Qt.RoundCap)

        #Creo arco
        paint.setPen(pen)
        paint.drawArc(margen,margen,ancho,alto,angInicio*16,45*16)  #16*angulo para graficar el angulo correcto 
        #paint.drawArc(margen,margen,ancho,alto,50,60*16)  #16*angulo para graficar el angulo correcto  

        #Fin
        paint.end

#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()