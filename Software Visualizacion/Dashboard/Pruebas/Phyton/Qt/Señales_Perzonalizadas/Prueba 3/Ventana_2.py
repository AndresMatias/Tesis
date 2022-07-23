import sys
import threading
import time

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#threading.Thread
class signalPrueba(threading.Thread):
    # signal=pyqtSignal()
    # def __init__(self):
    #     super().__init__(parent=None)

    def __init__(self,nombre_hilo):
        
        threading.Thread.__init__(self,name=nombre_hilo,target=signalPrueba.run)
        super(signalPrueba,self).__init__()
        pass
        
    def run(self):
        for i in range(0,10):
            time.sleep(0.2)
            print("hilo_Secundario")
            # self.signal.emit()

    def ejecutaseñal(self):
        pass

class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ventana.ui", self) #Esto sale del programa de diseño de interfaz y no lo tengo

        self.senal=signalPrueba("hola")
        #self.senal.signal.connect(self.cuenta)
        self.senal.start() #Como el thread esta creado a partir de Qthread este ya configura todo para que sea llamado el metodo run
        self.prueba()
        
    def prueba(self):
        for i in range(0,10):
            time.sleep(0.5)
            print("hilo principal")

    def cuenta(self):
        print("hola esto es mi slot en clase ventana")

#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()