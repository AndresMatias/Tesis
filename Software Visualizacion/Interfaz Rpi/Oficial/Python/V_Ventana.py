#-----Mis Clases-----
from M_consultaSql import EjecutaConsulta
from C_Filtros import *

#-----Clases PyQt5-----
from PyQt5 import uic,QtCore
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        """ Configuraciones iniciales """
        #---Iniciar el objeto QMainWindow(Ventana)---
        QMainWindow.__init__(self)
    
        #---Carga UI---
        fileh = QtCore.QFile('Interfaz_Pi_V1.ui')
        fileh.open(QtCore.QFile.ReadOnly)
        uic.loadUi(fileh, self)
        fileh.close()

        #----Configuraciones Previas Ventana----
        self.setWindowTitle("Sistema de Cambio de Molde Alladio") #Texto

        #----Clases de Conexion y Filtros----
        self.__MiConsulta=EjecutaConsulta()
        self.__MiFiltro=FiltroMoldes()

        #----Enlazo Señales-Slot----
        #Botones
        self.botonSql1.clicked.connect(self.__MiFiltro.escrituraBBDD)

        #Casilla de Textos
        #NroPiezasHr=self.piezasHr.text()
        self.piezasHr.textChanged.connect(self.__MiFiltro.determinoPiezasHr)

        #ComboBox
        self.simLista.currentTextChanged.connect(self.__MiFiltro.seleccionSim)
        self.moldeLista.currentTextChanged.connect(self.__MiFiltro.seleccionMolde)
        self.codigoLista.currentTextChanged.connect(self.__MiFiltro.seleccionCodigo)
        
        #Señales para armar/modificar la listas de los ComboBox
        self.__MiFiltro.cargarListaSim.connect(self.cargarSim)
        self.__MiFiltro.modfMolde.connect(self.cargarMoldes)
        self.__MiFiltro.modfCodigo.connect(self.cargarCodigos)

        #Señal para ventana de aviso
        self.__MiFiltro.msgAviso.connect(self.ventanaAviso)

        #----Inicio Conexion SQl, Obtengo Datos y los Guardo en mi Filtro----
        self.__MiConsulta.dameConexion('DESKTOP-TVTMCR0','Inyectora','alladio','12345','1433')
        self.__MiFiltro.cargarDataframe(self.__MiConsulta.consultaTabla())

    def cargarSim(self,listaSim):
        """ Este metodo carga los nros de identificacion de las maquinas en una lista comboBox\n
            Parametros:\n
                listaSim: Lista en formato string de los nros de identifiacionde las maquinas\n """
        self.simLista.addItems(listaSim)

    def cargarMoldes(self,listaMoldes):
        """ Este metodo carga los moldes de la maquina seleccionada en una lista comboBox\n
            Parametros:\n
                listaMoldes: Lista en formato string de los moldes\n """
        self.moldeLista.clear() #Limpio elementos de la lista
        self.moldeLista.addItems(listaMoldes) #Agrego elementos en la lista

    def cargarCodigos(self,listaCodigos):
        """ Este metodo carga los codigos del molde seleccionado en una lista comboBox\n
            Parametros:\n
                listaCodigos: Lista en formato string de los nros de los codigos\n """
        self.codigoLista.clear() #Limpio elementos de la lista
        self.codigoLista.addItems(listaCodigos) #Agrego elementos en la lista

    def ventanaAviso(self,titulo,mensaje):
        """ Este metodo implementa una ventana de aviso QMessageBox\n
            Parametros:
                titulo: titulo de la ventana\n
                mensaje: mensaje que va a leer el usuario\n """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        msg.setWindowTitle(titulo)
        msg.exec_()