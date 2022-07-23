#-----Mis Clases de Vista------

#-----Mis Clases de Modelo------

#-----Mis Clases de Controlador------

#-----Clase de Hilos------
from threading import Lock

#-----Clases PyQt5-----
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation,QRect
import sys


#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    """La clase ventana implementa la ventana principal del programa y la configuracion grafica contenida en el archivo .ui
    realizada a travez de Qt Designer y las clases que dan funcionalidad al interfaz todo esto siguendo el modelo MVC(Modelo Vista Controlador) 
    , los archivos.py que comiencen con M_ pertenecen a grupo de modelo, los C_ al grupo controlador y V_ a vista"""
    #Método constructor de la clase
    def __init__(self):
        """Configuraciones iniciales"""
        #Iniciar el objeto QMainWindow(Ventana)
        QMainWindow.__init__(self)
        uic.loadUi("V_Interfaz_3.ui", self)
        self.f1=QWidget(self.cp) #Lamina principal de la interfaz de carga
        #self.showMaximized() #Maximizo
        self.f1.setStyleSheet('background-color: rgb(85, 170, 255);') #Estilizo
        #Ubicacion y tamaño de f1
        #self.f1.move(0,0) #Ubico
        self.f1.resize(600,600) #Muevo
        self.toggleExpand()
    
    def toggleExpand(self):
        w_p=self.cp.width() #Obtengo ancho

        #Componentes y propiedades de unión
        self.animation = QPropertyAnimation(self.f1, b'geometry')
        # Establecer tiempo de animación
        self.animation.setDuration(1000)
        # Establecer el estado inicial de la animación
        self.animation.setStartValue(QRect(w_p/3, 0, 300, 300))
        # Establecer el estado final de la animación
        self.animation.setEndValue(QRect(w_p/3, 0, 300, 0))
        # Iniciar animación
        self.animation.start()
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()
        

        

        
    

         


