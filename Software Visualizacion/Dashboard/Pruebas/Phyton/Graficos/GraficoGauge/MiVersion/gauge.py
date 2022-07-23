import sys
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == '__main__':
        app = QApplication(sys.argv)
        w=QWidget() #Clase Base para hacer todo
        w.resize(250, 150) #Tamaño de Ventana
        w.move(300, 300) #Posicion donde va a aparecer
        w.setWindowTitle('Hello World') #Titulo de la ventana
        w.show() #Muestro Ventana
        sys.exit(app.exec_())