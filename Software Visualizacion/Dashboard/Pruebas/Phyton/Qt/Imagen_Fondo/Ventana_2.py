import sys
from typing import Text


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow,QVBoxLayout,QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


import Logos_

#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ventana.ui", self) #Esto sale del programa de diseño de iterfax y no lo tengo
        self.texto()
        
    def texto(self):

        vertical_layout = QVBoxLayout(self.w2) #Creo layout y anexo a widget
        self.la3 = QLabel('self.Logos_1') #Creo label
        vertical_layout.addWidget(self.la3)#Agrego a layout

        #Forma 1 de modificar fuente
        font1 = QFont()
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)

        self.l1.setText('HOLAAAA')
        #self.l1.setFont(font1)

        #self.la3.setFont(font1)
        
        #Forma 2 de modificar Fuente

        self.la3.setStyleSheet( 'font-size:14pt;\n' 
                                'color:#55ffff;\n'
                                'font: bold;\n'
                                'qproperty-alignment: AlignCenter;')
        #self.la3.setAlignment(Qt.AlignCenter) #Alineado
        print(self.la3.styleSheet())
  
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()