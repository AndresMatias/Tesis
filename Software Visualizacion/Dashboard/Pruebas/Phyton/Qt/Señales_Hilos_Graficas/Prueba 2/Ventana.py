import sys
import time

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import threading

class MiThread(threading.Thread):  
    def __init__(self, q):  
        threading.Thread.__init__(self)  
  
    def run(self):  
        pass


class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ventana.ui", self) #Esto sale del programa de diseño de interfaz y no lo tengo
        t = MiThread()  
        t.start()  
        t.join()
    
    def buttonClicked(self):
        self.thread.start()
    
    def updateLabel(self, text):
        self.label.setText(text)


#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()