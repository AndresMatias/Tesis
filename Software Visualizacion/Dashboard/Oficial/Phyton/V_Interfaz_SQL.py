#-----Clases Pyqt5-----
from PyQt5.QtWidgets import QDialog,QLineEdit
from PyQt5 import uic,QtCore

#-----Mis Clases de Controlador------
from C_Interfaz_SQL import *

#-----Mis Clases de Vista------
from V_Interfaz_Carga import VentanaCarga

#-----Recursos para pyinstaller-----
from recursos import *

class VentanaSql(QDialog):
    """ Ventana de dialogo que contiene la interfaz para ingresar los datos para conectarse a la bbdd 
        Parametros:
            datos: datos de conexion en caso de que haya credenciales guardadas de bbdd\n
            bandera: Bandera para indicar si esta ventana es la primera vez que se abre o el programa ya esta corriendo\n
            ls: Widget indicador para el usuario\n
            ls2: widget indicador para el usuario\n"""
    def __init__(self,datos,bandera,ls,ls2):
        QDialog.__init__(self)
        #----Carga Archivo ui----
        # Forma 1 de Carga UI
        # uic.loadUi("V_ConexionSQL.ui",self)
        
        # Forma 2 de Carga UI
        # ventana_path = resource_path("V_ConexionSQL.ui")
        # uic.loadUi(ventana_path, self)
        
        # Forma 3 de Carga UI
        fileh = QtCore.QFile('V_ConexionSQL.ui')
        fileh.open(QtCore.QFile.ReadOnly)
        uic.loadUi(fileh, self)
        fileh.close()
        self.setWindowTitle("Conexion SQL") #Texto
        #------Variables------
        ancho=830
        alto=536
        self.setFixedSize(ancho, alto)
        self.carga=VentanaCarga(self,self.cp_1,ancho, alto)
        self.__botones=(self.conectarSql,self.desconectarSql)
        self.__campos=(self.server,self.bbdd,self.user,self.passw)
        self.passw.setEchoMode(QLineEdit.Password)
        self.__Control=ControladorVentanaSql(self.__botones,self.__campos,self.carga) #Clase para manejar los eventos de los botones
        
        #----Widgets que indican al usuario el estado de la conexion----
        self.__ls=ls
        self.__ls2=ls2

        #----Enlazo Señales-Slots----
        self.__Control.conexionOk.connect(self.conexionOk)
        self.__Control.conexionNOk.connect(self.conexionNOk)
        
        #-----Si hay credenciales de conexion, conecta automatiamente
        if datos!=None: 
            self.server.setText(datos[0])
            self.bbdd.setText(datos[1])
            self.user.setText(datos[2])
            self.passw.setText(datos[3])
            if bandera ==True: #Si es el programa se acaba de abrir
                self.__Control.conectar()
        
    def cierreVentana(self):
        self.close()
    
    def conexionOk(self):
        """ Metodo para poner en verde los widgets indicadores de estado de conexion """
        self.__ls.setStyleSheet('background-color: rgb(0, 255, 0);')
        self.__ls2.setStyleSheet('background-color: rgb(0, 255, 0);')

    def conexionNOk(self):
        """ Metodo para poner en rojo los widgets indicadores de estado de conexion """
        self.__ls.setStyleSheet('background-color: rgb(255, 0, 0);')
        self.__ls2.setStyleSheet('background-color: rgb(255, 0, 0);')
        