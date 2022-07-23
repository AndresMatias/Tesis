import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

class prueba():
    def __init__(self,prueba) -> None:
        prueba.activated.connect(self.seleccionitem)
    def seleccionitem(self):
        print("hola2")
#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("prueba1.ui", self) #Esto sale del programa de diseño de interfaz y no lo tengo
        self.year.addItem("hola")
        lista=["1","2","3"]
        self.__p=prueba(self.turno)
        self.turno.addItems(lista) #Agregar una lista
        #self.turno.activated.connect(self.__p.seleccionitem) #Conecto señal de la funcion activated(metodo de QComboBox) con al funcion que yo programe 

    def itemSeleccionado(self):
        print("hola")    
  
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()