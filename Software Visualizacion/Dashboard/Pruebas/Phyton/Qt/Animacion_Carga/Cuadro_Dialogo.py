import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PyQt5 import uic
class Dialogo(QDialog):
 def __init__(self):
  QDialog.__init__(self)
  self.resize(300, 300) #Dimension ventana dialogo
  self.setWindowTitle("Cuadro de diálogo") #Texto
  self.etiqueta = QLabel(self) #Etiqueta de texto
  uic.loadUi("formulario.ui",self)
  
class Ventana(QMainWindow):
 def __init__(self):
  QMainWindow.__init__(self)
  self.resize(600, 600) #Tamaño ventana principal
  self.setWindowTitle("Ventana principal") #Titulo
  self.boton = QPushButton(self) #Creo boton
  self.boton.setText("Abrir cuadro de diálogo") #Titulo boton
  self.boton.resize(200, 30) #Dimension Boton
  self.dialogo = Dialogo() #Clase que contiene al cuadro dialogo
  self.boton.clicked.connect(self.abrirDialogo) #Evento Boton
  
 def abrirDialogo(self): #Evento Boton
  self.dialogo.etiqueta.setText("Diálogo abierto desde la ventana principal") #Etiqueta de texto de la clase dialogo
  self.dialogo.exec_() #Ejecuto la ventana de dialogo
  
app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_()