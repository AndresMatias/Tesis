import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QPropertyAnimation,QRect


#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ventana.ui", self) #Esto sale del programa de diseño de iterfax y no lo tengo
        self.b_1.clicked.connect(self.expandir)
        self.b_2.clicked.connect(self.geometrico)
        self.b_3.clicked.connect(self.toggleExpand)

    def expandir(self):
        width_menu=self.frame_1.width() #Obtengo ancho
        #Se setea el ancho final en funcion del ancho original
        width=100
        if width_menu>=100:
            width=300
        #Comienzo Animacion
        self.animacion=QPropertyAnimation(self.frame_1,b'minimumWidth')
        self.animacion.setStartValue(width_menu)
        self.animacion.setEndValue(width)
        self.animacion.setDuration(500)
        self.animacion.start()

    def geometrico(self):
        # Componentes y propiedades de unión
        self.animation = QPropertyAnimation(self.frame_2, b'geometry')
        # Establecer tiempo de animación
        self.animation.setDuration(1000)
        # Establecer el estado inicial de la animación
        self.animation.setStartValue(QRect(0, 0, 50, 50))
        # Establecer el estado final de la animación
        self.animation.setEndValue(QRect(0, 0, 350, 350))
        # Establecer el número de reproducciones de animación -1 significa ilimitado
        #self.animation.setLoopCount(-1)
        # Iniciar animación
        self.animation.start()

    def toggleExpand(self):
        width_menu=self.frame_4.width() #Obtengo ancho
        #Se setea el ancho final en funcion del ancho original
        width=100
        if width_menu==100:
            width=300
         # Componentes y propiedades de unión
        self.animation = QPropertyAnimation(self.frame_4, b'geometry')
        # Establecer tiempo de animación
        self.animation.setDuration(1000)
        # Establecer el estado inicial de la animación
        self.animation.setStartValue(QRect(0, 0, width_menu, width_menu))
        # Establecer el estado final de la animación
        self.animation.setEndValue(QRect(0, 0, width, width))
        # Iniciar animación
        self.animation.start()      
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()