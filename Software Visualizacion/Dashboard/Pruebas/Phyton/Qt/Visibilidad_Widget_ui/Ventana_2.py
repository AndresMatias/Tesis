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
        #Si cargo los dos me genera una especie de erro abajo
        #uic.loadUi("transparente1.ui", self) #Esto sale del programa de diseño de iterfax y no lo tengo
        uic.loadUi("transparente.ui", self) #Esto sale del programa de diseño de iterfax y no lo tengo
        self.widget_2.deleteLater() #Elimino un widget_2
        #self.cp.deleteLater()
        #self.setWindowOpacity(0.3) #Toda la ventana 
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()