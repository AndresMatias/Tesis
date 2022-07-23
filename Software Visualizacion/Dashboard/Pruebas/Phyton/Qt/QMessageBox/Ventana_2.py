import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
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
    

    def closeEvent(self, event):
        msgBox = QMessageBox(
            QMessageBox.Question,
            "window Close",
            "Are you sure you want to close the window?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            parent=self)
        msgBox.setDefaultButton(QMessageBox.No)
        msgBox.setStyleSheet(   'QMessageBox {\n'
                                    'background-color: #2b5b84;\n '
                                    'color: white;\n'
                                    '}\n'
                                'QPushButton{'
                                    'color: white;\n'
                                    'font-size: 16px;\n' 
                                    'background-color: #1d1d1d;\n'
                                    'border-radius: 10px;\n' 
                                    'padding: 10px;\n'
                                    'text-align:center;}\n'
                                'QPushButton:hover{\n'
                                    'color: #2b5b84;\n'
                                    '}\n'
                                'QLabel{\n' 
                                    'color: white;\n'
                                    'background-color: rgb(255, 255, 255);\n'
                                    '}')
        msgBox.exec_()
        reply = msgBox.standardButton(msgBox.clickedButton())
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def keyPressEvent(self, event): # Evento de teclado
        print("tecla")
        key=event.key()
        if key==Qt.Key_Escape: #Si presiono escape
            print("Escape")
            msgBox = QMessageBox(
            QMessageBox.Question,
            "window Close",
            "Are you sure you want to close the window?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            parent=self)
            msgBox.setDefaultButton(QMessageBox.No)
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()