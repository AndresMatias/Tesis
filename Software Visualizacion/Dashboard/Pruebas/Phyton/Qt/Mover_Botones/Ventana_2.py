import sys

from PyQt5 import uic
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt

#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("interfaz.ui", self) #Esto sale del programa de diseño de interfaz y no lo tengo
        #self.showFullScreen()

    def mousePressEvent(self, event):
        try:
            #print("Clicks presionado") #Cuando hago click sobre el boton no me lo detecta al click
            if event.button() == Qt.LeftButton:
                self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
                event.accept()
        except Exception as err:
            print("error 1:",err)        

    def mouseMoveEvent(self, event):
        try:
            #print("mouse moviendose mientras mantengo el click")
            if event.buttons() == Qt.LeftButton:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
        except Exception as err:
            print("error 2:",err)

    def keyPressEvent(self, event): # Evento de teclado
        key = event.key()
        if key == Qt.Key_Escape: #Si presiono escape
            print("Escape")
            cajaMensaje=QMessageBox()
            self.setStyleSheet("QMessageBox{background-color: rgb(255, 255, 255);}")
            #cajaMensaje.setStyleSheet("background-color: rgb(155, 115, 155);")
            respuesta=cajaMensaje.question(self,"Cerrar Ventana","Desea Salir del programa",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if respuesta==QMessageBox.Yes:
                self.close()    
            else:
                event.ignore()
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()