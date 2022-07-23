from xmlrpc.client import Boolean
from pandas.core.frame import DataFrame

#-----Mis Clases-----
from V_Interfaz_SQL import VentanaSql
from V_Interfaz_Carga import *
from C_Archivos import *
from M_consultaSql import EjecutaConsulta
from V_Ventanas_Auxiliares import VentanaAviso, VentanaAvisoPrueba
from Constantes import *
from M_ProcesamientoDatos import ProcesamientosDatosAvisos

class GestionInicio(QObject):
    """ Esta clase gestiona los eventos de inicio del programa, su carga de archivos y configuraciones iniciales """
    construccionFiltros=pyqtSignal(DataFrame,int) #Señal emitida para construir filtros
    def __init__(self,Mi_Consulta,ls,ls2):
        super().__init__(parent=None)
        #-----Variables-----
        self.__Mi_Consulta=EjecutaConsulta() #Tiene patron singleton
        
        #----Widgets que indican al usuario el estado de la conexion----
        self.__ls=ls
        self.__ls2=ls2
        self.__Archivos=ManejoArchivos() #Clase para manejar archivos
        
    def conexionSql(self,bandera):
        """ Metodo para iniciar ventana de conexion sql por primera vez
            Parametros:
                bandera: Indica si es la primera vez que se abre el programa(True) o no(False)"""
        datos=None
        datos=self.__Archivos.CargaBBDD() #Extraigo datos de conexion de los archivos
        InterfazSql=VentanaSql(datos,bandera,self.__ls,self.__ls2)
        InterfazSql.exec_() #Ejecuto la ventana de dialogo
        
    def cargaSim(self):
        """ Metodo que consulta a la bbdd los sims y las carga en una combobox """
        sims=None
        if self.__Mi_Consulta.estadoConexion()==True: #Conectado a la bbdd
            sims=self.__Mi_Consulta.consultaSims() #Obtengo las sims de las maquinas
            self.construccionFiltros.emit(sims,5) #Contrusyo los filtros, 5 es el numero maximo de variables a consultar

class GestionMenu(QObject):
    #Nota: Clase no terminada, esta clase no forma parte de la V2.0
    """ Clase que gestiona los diferentes eventos del menu """
    def __init__(self, inicio):
        """ Construtor para inicializar variables
            Parametros:
                inicio: Clase de gestion de inicio que reciclo para implementar la conexion sql y construccion de filtros
                        cada vez que conecte a otro bbdd desde el menu del programa """
        super().__init__(parent=None)
        self.__inicio=inicio
    
    def conexionSql(self):
        """ Metodo que gestiona la ventana de conexion sql cuando se invoca desde el menu """
        self.__inicio.conexionSql(False)
        self.__inicio.cargaSim()

class GestionAvisos2(QObject):
    #Nota: Clase no terminada, esta clase no forma parte de la V2.0
    """ Clase que gestiona los eventos del cuadro de dialogo para diferentes avisos importantes de las maquinas"""
    def __init__(self,padre):
        """ Construtor para inicializar variables """
        super().__init__(parent=None)
        self.__padre=padre #Ventana Padre
        #self.__banderaEstado=[False,False,False,False,False] #Bandera que indica si ya ha yun cuadro de dialogo abierto o no, False por defecto significa que no
        self.coloresFondo=(azul,amarillo,rojo,rojo,blanco)
        self.coloresLetra=(rojo,negro,negro,negro,negro)
        self.coordVentana=((0,0),(0,350),(350,0),(700,0),(1100,0))
        self.__titulos=('Maquinas con Corte de Luz','Cajas de Scrap Llenas','Fallo Seguridad Cajas de Scraps','Maxima Temperatura Superada','Cajas de Scrap Abiertas')
        self.__VentanasAvisos=[]

        #Creo las Ventanas Iniciales
        for i in range(0,5):
            p=VentanaAviso(self.__padre,(1,10),self.coloresFondo[i],self.coloresLetra[i],self.__titulos[i],17,'',15,i,self.coordVentana[i])
            p.cerrarPest.connect(self.signalCerrarPosponer) #Enlazo Señales
            self.__VentanasAvisos.append(p)
    
    def signalCerrarPosponer(self,posicion):
        """ Metodo que recibe del cuadro de dialogo para cerrar ventana
            Argumentos:
                posicion: Indice del la ventana que quiero cerrar"""
        #self.__banderaEstado[posicion]=False
        self.__VentanasAvisos[posicion].cerrarVentana()

    def actualizar(self,sims,i):
        """ Metodo para actualizar informacion sin relanzar ventana 
            Argumentos:
                sims: string que contiene las sims a mostrar en los avisos
                i: posicion de la ventana avisa que quiero mostrar"""
        self.__VentanasAvisos[i].actualizarInformacion(sims) #Actualizo datos
        self.abrirDialogo(self.__VentanasAvisos[i]) #Abro ventana si no esta abierta
        #if self.__banderaEstado[i]==False:
            #pass
            #self.abrirDialogo(self.__VentanasAvisos[i]) #Abro ventana si no esta abierta  
            # print('\n')
            # print('Entre')
          
        #self.__banderaEstado[i]=True

    def abrirDialogo(self,ventana):
        """ Metodo para abrir cuadro de dialogo 
            Argumentos:
                ventana: ventana que quiero abrir"""
        ventana.exec_()