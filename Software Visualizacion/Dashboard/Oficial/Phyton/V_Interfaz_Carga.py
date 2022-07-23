from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from C_Hilos import CirculoProgreso

class VentanaCarga():
    """ Esta clase implementa un widget circuilar de carga
        \nParametros:
            parent: Clase padre de la ventana que contendra al widget de carga\n
            cp: widget principal de la clase padre\n
            ancho: ancho de cp\n
            alto: alto de cp\n """
    def __init__(self,parent,cp,ancho,alto):
        #----Variables----
        self.__cp=cp #Widget Contenedor principal
        self.ancho = ancho
        self.alto = alto    
        self.f1=QWidget(self.__cp) #Lamina principal de la interfaz de carga
        self.layout1=QVBoxLayout()
        self.progreso1=circuloProgreso(self.alto/4)
        self.__parent=parent #Clase QDialog


    def inicioInterfaz(self):
        #-----Variables-------   
        self.__Hilo_1=CirculoProgreso(self)

        #----Conecto señales con slots----
        self.__Hilo_1.actualizarProgreso.connect(self.progreso1.set_valor)
        self.__Hilo_1.cerrarVentana.connect(self.__parent.cierreVentana)
        self.__Hilo_1.cerrarAnimacion.connect(self.terminarAnimacion)

        #----Muestro y estilizo al widget que contendra al circulo de carga----
        self.f1.show()
        self.f1.setStyleSheet('background-color: rgb(85, 170, 255);') #Estilizo

        #----Ubicacion y tamaño de f1----
        self.f1.move(self.ancho/4,self.alto/4) #Ubico
        self.f1.resize(self.ancho/2,self.alto/2) #Muevo
        # self.f1.move(830/4,536/4) #Ubico
        # self.f1.resize(830/2,536/2) #Muevo

        #----Configuracion de circulo de progreso----
        self.progreso1.setMinimumSize(self.progreso1.alto,self.progreso1.ancho)
        self.progreso1.set_texto='Conectando...'

        #----Agrego componentes layout----
        self.layout1.addWidget(self.progreso1,Qt.AlignCenter,Qt.AlignCenter)
        self.f1.setLayout(self.layout1)
        self.__Hilo_1.start()

    def terminarAnimacion(self):
        """ Metodo que utiliza el hilo de animacion para termiar la animacion """
        self.f1.hide()
    

    def modficarInterfaz():
        """ Metodo para cambiar colores y texto del circuilo de progreso"""
        pass

    def indicarCierre(self,bandera):
        """ Metodo para terminar animacion """
        self.__Hilo_1.cierreHilo(bandera)

class circuloProgreso(QWidget):
    """ Esta clase implementa el dibujo del circuilo de carga 
        Parametros:
            tam: ancho de cp"""
    def __init__(self,tam):
        QWidget.__init__(self)

        #Propiedades por defecto
        # self.valor=0
        self.ancho=tam
        self.alto=tam
        self.angInit=0
        self.progreso_cap=True
        self.progreso_color1='blue'
        self.progreso_color2='white'
        self.max_value=100
        self.enable_shadow=True
        self.set_texto=''
        self.set_font='Arial'
        self.set_font_tam=13
        self.color_texto='white'
        self.resize(self.ancho,self.alto)
        # self.setStyleSheet('background-color: rgb(255, 170, 0);')

    def set_valor(self,i):
        """ Metodo para setear la posicion de barra de carga
            Parametros:
                i:angulo que quiero gire """
        self.angInit=i*3
        try:
            self.repaint()
        except Exception as err:
            pass

    def paintEvent(self,event):
        """ Metodo para dibujar el circulo """
        ancho=self.ancho
        alto=self.alto
        #margen=self.progreso/2
        margen=10
        #valor=self.valor*360/self.max_value #Angulo
        angInit=self.angInit

        #Pintor
        paint=QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) #Remueve pixelado
        paint.setFont(QFont(self.set_font,self.set_font_tam))

        #Creo rectangulo
        rect=QRect(0,0,self.ancho,self.alto)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        #Lapiz 1
        pen=QPen()  
        pen.setWidth(margen)


        #Creo arco
        pen.setColor(QColor(self.progreso_color1))
        paint.setPen(pen)
        paint.drawArc(margen,margen,ancho-20,alto-20,0*16,360*16)

        pen.setColor(QColor(self.progreso_color2))
        paint.setPen(pen)
        paint.drawArc(margen,margen,ancho-20,alto-20,angInit*16,45*16)

        #Texto
        pen.setColor(QColor(self.color_texto))
        paint.setPen(pen)
        paint.drawText(rect,Qt.AlignCenter,f"{self.set_texto}")
        a=2
        if a==1: #Cmabiar condicion pero es para poner que se conecto a la bbdd
            pen.setColor(QColor('green'))
            paint.setPen(pen)
            paint.drawArc(margen,margen,ancho-20,alto-20,0*16,360*16)  
        #Fin
        paint.end
