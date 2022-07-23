import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation,QRect


#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ventana.ui", self) #Esto sale del programa de diseño de iterfax y no lo tengo
        #Creo widgets
        self.b_1=QPushButton("Expandir")

        self.f1=QWidget()
        self.f1.setStyleSheet('background-color: rgb(255, 170, 0);')

        self.f2=QWidget()
        self.f2.setStyleSheet('background-color: rgb(85, 170, 255);')

        self.f3=QWidget()
        self.f3.setStyleSheet('background-color: rgb(85, 170, 255);')

        self.f4=QWidget()
        self.f4.setStyleSheet('background-color: rgb(85, 170, 255);')

        #Creo layauts
        self.h1=QVBoxLayout()
        self.h2=QHBoxLayout()

        #Agrego componentes a layout
        #h1
        self.h1.addWidget(self.b_1)
        self.h1.addWidget(self.f1)
        #h2
        self.h2.addWidget(self.f2)
        self.h2.addWidget(self.f3)
        self.h2.addWidget(self.f4)

        self.cp.setLayout(self.h1)
        self.f1.setLayout(self.h2)

        self.b_1.clicked.connect(self.toggleExpand)


    def toggleExpand(self):
        w_p=self.f1.width() #Obtengo ancho

        #Componentes y propiedades de unión
        self.animation = QPropertyAnimation(self.f4, b'geometry')
        # Establecer tiempo de animación
        self.animation.setDuration(1000)
        # Establecer el estado inicial de la animación
        self.animation.setStartValue(QRect(w_p/3, 0, 300, 300))
        # Establecer el estado final de la animación
        self.animation.setEndValue(QRect(w_p/3, 0, 300, 0))
        # Iniciar animación
        self.animation.start()
        #self.f4.deleteLater() lo elimina de una pero no es la idea sino esperar un tiempo para que no vuelva a aparecer      
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()