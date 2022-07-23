from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random
     
class Ventana(QMainWindow):
    
    def __init__(self):
        
        QMainWindow.__init__(self)

        loadUi("con_promocionar.ui",self)

        self.setWindowTitle("Mi_Ejemplo")
        #Graficos
        tupla=["Ana","Juan","Diana","Catalina"]
        self.Grafico_1.ploteo(tupla)
        self.Grafico_2.ploteo()
        self.Grafico_3.ploteo()
        
        
app = QApplication([])
window = Ventana()
window.show()
app.exec_()