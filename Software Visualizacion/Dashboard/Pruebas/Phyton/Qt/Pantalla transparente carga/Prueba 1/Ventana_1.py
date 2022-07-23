import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt


#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("transparente.ui", self) #Esto sale del programa de diseño de iterfax y no lo tengo
        #self.setWindowOpacity(0.3) #Toda la ventana 
        """ self.cp.setAttribute(Qt.Qt.WA_TranslucentBackground, True )
        self.cp.setAttribute(Qt.Qt.WA_NoSystemBackground, False)      
        self.cp.setWindowFlags(Qt.Qt.FramelessWindowHint)

        self.cp.setStyleSheet("Principal{background-color: rgba(0, 215, 55, 70);}")  """
        #Widget 4
        self.widget_4.setAttribute(Qt.WA_TranslucentBackground) #totalmente transparente solo el widget que contiene todo
        self.widget_4.setStyleSheet("background-color: rgba(20, 20, 20, 170);") #Hereda a todos los componentes del contenedor widget
        #Widget 3
        self.widget_3.setStyleSheet("background-color: rgba(20, 20, 20, 170);")
        #Widget 2
        self.cp.setStyleSheet("QWidget#widget_2{background-color: rgba(20, 20, 20, 170);}") #Solo al contenedor widget_2, no hereda a componentes
  
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()