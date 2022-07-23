import sys
import threading
import time

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
    
class EmitSignal(QWidget):
    #customSignal = pyqtSignal(int,str) #Objeto creo
    customSignal = pyqtSignal(int,int) #Objeto creo, funciona la linea de arriba tambien pero nose que argumentos usar en pyqtSignal
    def __init__(self):
        super(EmitSignal,self).__init__()
        
        # self.customSignal = pyqtSignal()
        # self.emitCustomSignal()
        #self.customSignal.connect(self.emitido) #Conecto señal a un metodo propio de la clase

    def emitoSenal(self):
        self.customSignal.emit(5,"señal emitida") #emito señal


class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ventana.ui", self) #Esto sale del programa de diseño de interfaz y no lo tengo

        self.senal=EmitSignal()

        self.senal.customSignal.connect(self.cuenta) #Conecto señal

        self.senal.emitoSenal() 


    def cuenta(self,numero,texto):
        print("hola esto es mi slot en clase ventana")
        print("Nro: ",numero)
        print("Texto: ",texto)

#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()