#-----Clases PyQt5-----
from PyQt5 import uic,QtCore
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

#-----Mis Clases-----
from V_ventana import *
from Constantes import *
class VentanaAviso(QDialog):
    cerrarPest= pyqtSignal(int) #genero señal para informar que pestaña se cerro
    def __init__(self,parent,estirar,colorWidget,colorLabel,titulo,tamTitulo,label,tamLabel,i,coord) -> None:
        """ Constructor de la clase donde se aloja todo el codigo que contruye y distribuye todos los componentes graficos\n
        Parametros:\n
            parent: widget del cual va a heredar la clase\n
            estirar: tupla de dos elementos int para indicar en que proporcion se van a distribuir los widgets es decir cual va a ocupar mas espacio\n
            colorwidget: color del widget contenedor\n
            coloresLabels: color de la etiqueta del titulo y/o label del segundo 2do widget\n
            titulo: Nombre que va llevar la etiqueta de texto que va indicar que se esta representando\n
            tamTitulo: Tamaño de letra del titulo\n
            label: Texto de la 2da etiqueta, si no se usa poner None de esa forma no se agregara en la interfaz y se podra usar otro objeto\n
            tamLabel: Tamaño del label\n
            i: Identifiador de ventana\n
            coord: Tupla o vector de dos puntos a donde quiero mover la ventana\n
        """
        QDialog.__init__(self)
        #-----Variables----------
        self.colorWidget=colorWidget
        self.colorLabel=colorLabel
        self.estirar=estirar
        self.titulo=titulo #Nombre del titulo
        self.tamTitulo=tamTitulo
        self.sims=label #Lista de sims
        self.tamSims=tamLabel
        self.i=i
        self.coord=coord

        #------Widgets------
        self.lv=QVBoxLayout()
        self.contenedorTitulo=QWidget()
        self.contenedorObjeto=QWidget()
        self.labelTitulo=QLabel()
        self.labelSims=QLabel()

        #-----Layouts-----
        self.lvTitulo=QVBoxLayout()
        self.lvObjeto=QVBoxLayout()
        
        self.__construirVentana()

    def __construirVentana(self):
        """ Metodo para contruir cuadro de dialogo """
        self.resize(300, 300)
        self.setWindowTitle("Aviso Importante")
        self.etiqueta = QLabel(self)
        self.move(self.coord[0],self.coord[1])
         #-----------Configuraciones----------------
        self.setLayout(self.lv)
        self.lv.setContentsMargins(0,0,0,0)
        self.contenedorTitulo.setLayout(self.lvTitulo)
    
        self.lvTitulo.addWidget(self.labelTitulo)
        self.etiqueta=QLabel()
        self.contenedorObjeto.setLayout(self.lvObjeto) #Incluyo el layout aca porque sino me jode el layout de la clase de dibujo
        self.lvObjeto.addWidget(self.labelSims)

        self.lv.addWidget(self.contenedorTitulo)
        self.lv.addWidget(self.contenedorObjeto)
        self.lv.setStretch(self.estirar[0],self.estirar[1]) #Seteo cual se extiende mas

        #-----------Hoja de Estilos----------------
        self.setStyleSheet('background-color: '+self.colorWidget+';')
        self.contenedorTitulo.setStyleSheet('background-color: '+self.colorWidget+';')
        self.contenedorObjeto.setStyleSheet('background-color: '+self.colorWidget+';')   
        self.estilizar(self.labelTitulo,self.titulo,self.colorLabel,self.tamTitulo,'MS Shell Dlg 2')
        self.estilizar(self.labelSims,self.sims,self.colorLabel,self.tamSims,'MS Shell Dlg 2')

        #----Ejecuto Ventana----
        #self.exec_()

    def actualizarInformacion(self,label):
        """ Metodo para actulizar informacion del cuadro de dialogo """
        #-----Variables----------
        self.sims=label #Lista de sims
        self.estilizar(self.labelTitulo,self.titulo,self.colorLabel,self.tamTitulo,'MS Shell Dlg 2')
        self.estilizar(self.labelSims,self.sims,self.colorLabel,self.tamSims,'MS Shell Dlg 2')
    
    def estilizar(self,etiqueta,titulo,color,tam,fuente):
        """ Metodo para estilizar y setear texto de un label 
            Parametros:
                etiqueta: QLabel que se desea modificar\n
                tiutlo: Texto a mostrar\n
                color: color del texto(preferentemente en formato html)\n
                tam: Tamaño de letra\n
                fuente: Fuente de texto(ej: Arial)\n"""
        etiqueta.setText(titulo) 
        etiqueta.setStyleSheet( 'font-size:'+str(tam)+'pt;\n' 
                                'color:'+color+';\n'
                                'font: '+fuente+';\n'
                                'qproperty-alignment: AlignCenter;')
    
    def cerrarVentana(self):
        """ Metodo para cerrar la ventana """
        self.close()
    
    def closeEvent(self,event):
        """ Metodo que se ejecuta si se cierra la ventana desde la X """
        self.cerrarPest.emit(self.i)

class VentanaAvisoPrueba(QDialog):
     
    def __init__(self) -> None:
        """ Pruebas """
        QDialog.__init__(self)   

    def construirVentana(self):
        """ Metodo para contruir cuadro de dialogo """
        self.resize(300, 300)
        self.setWindowTitle("Cuadro de diálogo")

    def abrirVentana(self):
        self.exec_()

    def cerrarVentana(self):
        """ Metodo para cerrar la ventana """
        self.close()