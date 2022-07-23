import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PyQt5 import uic

class Ventana(QMainWindow):
  def __init__(self):
    QMainWindow.__init__(self)
    uic.loadUi("circulo.ui",self)
    self.control.setMinimum(0)
    self.control.setMaximum(100)
    self.control.setSingleStep(1)
    #self.control.setValue(0)
    self.control.valueChanged.connect(self.barraProgreso)

  def barraProgreso(self): #Evento Boton
    estilo="""QFrame{
                border-radius:150px;
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:{stop1} rgba(85, 85, 255, 255), stop:{stop2} rgba(255, 255, 255, 255), stop:{stop3} rgba(85, 85, 255, 255), stop:{stop4} rgba(255, 255, 255, 255));
                    }"""
    valor=self.control.value()/100               
    """ stop1=str(valor-0.001)
    stop2=str(1)  """
    stop1=str(valor-0.0010)
    stop2=str(valor)
    #Se corren casi un 20 %
    stop3=str(valor-0.199999999)
    stop4=str(valor-0.20)
    #nuevo_estilo=estilo.replace('{stop1}',stop1).replace('{stop2}',stop2)
    nuevo_estilo=estilo.replace('{stop1}',stop1).replace('{stop2}',stop2).replace('{stop3}',stop3)  .replace('{stop4}',stop4)                   
    self.progresbar.setStyleSheet(nuevo_estilo)

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_()