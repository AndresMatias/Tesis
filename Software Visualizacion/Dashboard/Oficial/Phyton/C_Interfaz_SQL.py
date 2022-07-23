import time

from PyQt5.QtCore import QObject,pyqtSignal
from C_Archivos import *

from M_consultaSql import EjecutaConsulta

class ControladorVentanaSql(QObject):
    conexionOk= pyqtSignal() #genero señal para poner en verde widgets
    conexionNOk= pyqtSignal() #genero señal para poner en rojo widget
    """ Clase que gestiona la conexion y desconexion de la bbdd en la ventana dialog de conexion sql """
        
    def __init__(self,botones,campos,carga):
        super().__init__(parent=None)
        #----Variables----------
        self.__conectarSql=botones[0] #Referencia al widget del boton conectar
        self.__desconectarSql=botones[1] #Referencia al widget del boton desconectar
        self.__server=campos[0] #Nombre del servidor sql
        self.__bbdd=campos[1] #Nombre de la bbdd sql
        self.__user=campos[2] #Nombre del usuario sql
        self.__passw=campos[3] #Contraseña del usuario sql
        self.__Carga=carga #Clase que maneja la animacion de carga
        self.__Mi_Consulta=EjecutaConsulta() #Clase para conectar y ejecutar consultas sql(Tiene patron singleton implementado)
        self.__banderaConectar=True #Bandera para habilatar/desabilitar programacion del boton conectar (True:Habilitado)
        self.__banderaDesconectar=True #Bandera para habilatar/desabilitar programacion del boton desconectar (True:Habilitado)

        #-------Enlaze widget-evento-------
        self.__conectarSql.clicked.connect(self.conectar) #Evento Boton conectar
        self.__desconectarSql.clicked.connect(self.desconectar) #Evento Boton desconectar
        # self.__server.textChanged.connect(self.validar_server)
        # self.__bbdd.textChanged.connect(self.validar_bbdd)
        # self.__user.textChanged.connect(self.validar_user)
        # self.__passw.textChanged.connect(self.validar_passw) 
         

    def conectar(self):
        """ Metodo que gestiona el evento del boton conexion de la ventana de conexion a la bbdd """
        #print(self.__Mi_Consulta.estadoConexion())
        if self.__banderaConectar==True and self.__Mi_Consulta.estadoConexion()==False:
            self.__banderaConectar=False
            #-------Obtengo los textos de los campo----------
            server=self.__server.text()
            bbdd=self.__bbdd.text()
            user=self.__user.text()
            passw=self.__passw.text()
            # if server=="":
            #     self.__server.setStyleSheet("border: 1px solid yellow;")
            # if bbdd=="":
            #     self.__bbdd.setStyleSheet("border: 1px solid yellow;")
            # if user=="":
            #     self.__user.setStyleSheet("border: 1px solid yellow;")
            # if passw=="":
            #     self.__passw.setStyleSheet("border: 1px solid yellow;")
                
            if server!="" and bbdd!="" and user!="" and passw!="":
                self.__Carga.inicioInterfaz()
                self.__Mi_Consulta.dameConexion(server,bbdd,user,passw)
                #self.__Mi_Consulta.dameConexion('DESKTOP-TVTMCR0','Inyectora','alladio','12345','Tabla_Pruebas2')
                time.sleep(1)
                self.__Carga.indicarCierre(self.__Mi_Consulta.estadoConexion())
                #-----------Activar/Desactivar banderas para ejecutar la programacion de este metodo---------------
                if self.__Mi_Consulta.estadoConexion()==True: #Conectado a la bbdd
                    #self.__parent.cierreVentana()
                    archivo=ManejoArchivos() #Variable local
                    archivo.GuardarBBDD((server,bbdd,user,passw))
                    self.conexionOk.emit()
                    self.__banderaConectar=False
                    pass
                elif self.__Mi_Consulta.estadoConexion()==False: #No conectado a la bbdd
                    self.__banderaConectar=True
                    self.conexionNOk.emit()

    def desconectar(self):
        """ Metodo que gestiona el evento del boton desconexion de la ventana de conexion a la bbdd """
        if self.__banderaDesconectar==True:
            self.__banderaDesconectar=False
            self.__Mi_Consulta.cerrarConexion()
            self.__banderaDesconectar=True
            self.__banderaConectar=True
    
        pass
    # def validar_server(self):
    #     #print('hola')
    #     #server=self.__server.text()
    #     # if server!="":
    #     #     self.__server.setStyleSheet("border: 0px;")  #Nota:tengo q obtener hoja de estilo para estilizar borde
	# 	# elif : #Si erro en la conexion
	# 	# 	self.nombre.setStyleSheet("border: 1px solid red;")

	# 	# else: #Conexion aceptada
	# 	# 	self.nombre.setStyleSheet("border: 1px solid green;")
    #     pass

    # def validar_bbdd(self):
    #     pass

    # def validar_user(self):
    #     pass

    # def validar_passw(self):
    #     pass