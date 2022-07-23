__name__="Dasboard Alladio"
__version__="3.0"
__author__="Singls Andres Matias"
__copyright__="Copyright 2021"
__license__="GPL"#Ver que poner
__status__="En Proceso"

import sys
from PyQt5.QtWidgets import QApplication
from V_ventana import *

#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()