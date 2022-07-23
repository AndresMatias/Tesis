import sys
import threading
import time

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#threading.Thread
class signalPrueba(QThread):
    signal=pyqtSignal()
    def __init__(self):
        super(signalPrueba,self).__init__(parent=None)

    # def __init__(self,nombre_hilo):
        
    #     threading.Thread.__init__(self,name=nombre_hilo,target=signalPrueba.run)
    #     super(signalPrueba,self).__init__()
    #     pass
        
    def run(self):
        for i in range(0,10):
            time.sleep(0.2)
            self.signal.emit()

class objetoprueba(QObject):
    signal=pyqtSignal()
    def __init__(self):
        super(objetoprueba,self).__init__(parent=None)

    # def __init__(self,nombre_hilo):
        
    #     threading.Thread.__init__(self,name=nombre_hilo,target=signalPrueba.run)
    #     super(signalPrueba,self).__init__()
    #     pass
        
    def run(self):
        for i in range(0,10):
            time.sleep(0.2)
            self.signal.emit()


class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ventana.ui", self) #Esto sale del programa de diseño de interfaz y no lo tengo

        self.mihilo=QThread()
        self.miobjeto=objetoprueba()
        self.miobjeto.moveToThread(self.mihilo)

        #self.miobjeto.signal.connect(self.cuenta)
        self.mihilo.started.connect(self.cuenta)
        self.mihilo.start()

        # self.senal=signalPrueba()
        # self.senal.signal.connect(self.cuenta)
        

        #self.iniciarHilo()
        self.prueba()
        
    def prueba(self):
        for i in range(0,10):
            time.sleep(0.5)
            print("hilo principal")

    def cuenta(self):
        print("hola esto es mi slot en clase ventana")
    
    def iniciarHilo(self):
        self.senal.start() #Como el thread esta creado a partir de Qthread este ya configura todo para que sea llamado el metodo run


#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()