#----Mis Clases----
from M_ProcesamientoDatos import *
from M_consultaSql import *
from Constantes import *
#----Clase PyQt5----
from PyQt5.QtCore import *

#----Otros----
import re

class FiltroMoldes(QObject):
    """ Clase que maneja los filtros para cambiar el molde de una maquina"""
    
    #----Señales----
    cargarListaSim=pyqtSignal(list) #Señal para confeccionar la lista sim
    modfMolde=pyqtSignal(list) #Señal para cambiar la lista de moldes si se modifica la sim seleccionada
    modfCodigo=pyqtSignal(list) #Señal para cambiar la lista de codigo si se modifica el molde seleccionado
    msgAviso=pyqtSignal(str,str) #Genro señal para dar un aviso al usuario

    def __init__(self) -> None:
        """ Constructor para inicializar variables"""
        super().__init__()
        #----Variables----
        self.__df=None #Dataframe de tabla SQL
        self.__ProcesarDatos=ProcesarDatos() #Clase para separar datos del dataframe
        self.__sim=None #Nro de Sim seteado
        self.__molde=None #Molde seteado
        self.__codigo=None #Codigo seteado
        self.__id=None #Nro de combinacion escogida en base a la combinacion sim-molde-codigo
        self.__nroPiezasHrs=None #Numero de piezas Horas
        #----Clases----
        self.__MiConsulta=EjecutaConsulta() #Patron Singleton por lo cual es el mismo objeto en cualquier parte del programa

    def seleccionSim(self,sim):
        """ Metodo que es llamado cuando se escoge una sim en la combobox sim y manda a crear/actulizar la lista del combobox de Molde """
        self.__sim=sim #Guardo sim seleccionada
        if sim!='SIM':
            self.modfMolde.emit(self.__ProcesarDatos.listaMolde(sim)) #Cargo/modifico lista de moldes del comboBox
        else:
            self.modfMolde.emit(['Moldes'])

    def seleccionMolde(self,molde):
        """ Metodo que es llamado cuando se escoge una sim  en el combox de Molde y manda a crear/actulizar la lista del combobox de codigo"""
        self.__molde=molde #Guardo el molde seleccionado
        if (self.__molde!='Moldes' and self.__molde!='') and (self.__sim!='SIM' and self.__sim!=''):
            self.modfCodigo.emit(self.__ProcesarDatos.listaCodigo(self.__sim,molde)) #Cargo/modifico lista de codigos del comboBox
        else:
            self.modfCodigo.emit(['Codigos'])
    def seleccionCodigo(self,codigo):
        """ Metodo que es llamado cuando se escoge una sim  en el combobox de Codigo y manda a averigurar el id resultante y si hay una combinacion repetida en base a lo escogido"""
        #----------------------------------------------------------
        #Nota: reemplazar 'Moldes'-'SIM'-'Codigos' por variables en archivos xlm
        #----------------------------------------------------------
        self.__codigo=codigo
        if (self.__molde!='Moldes' and self.__molde!='') and (self.__sim!='SIM' and self.__sim!='') and (self.__codigo!='Codigos' and self.__codigo!=''):
            self.__id=self.__ProcesarDatos.listaId(self.__sim,self.__molde,codigo)

    def determinoPiezasHr(self,texto):
        """ Metodo que recoge el texto de la casilla de piezasHr, comprueba si es un numero y si lo es lo guarda"""
        if texto.isdigit(): #Compruebo que son solo numeros y no hay letras
            self.__nroPiezasHrs=texto 
        else:
            self.__nroPiezasHrs=None
        
    def escrituraBBDD(self):
        """ Metodo para escribir la combinacion seteada en la base de datos cuando se hace click en el boton procesar(boton llamado asi en la interfaz visual) """
        if (self.__molde!='Moldes' and self.__molde!='') and (self.__sim!='SIM' and self.__sim!='') and (self.__codigo!='Codigos' and self.__codigo!=''):
            if self.__nroPiezasHrs!=None:    
                bandera=self.__MiConsulta.escribirID(self.__sim,self.__id,self.__nroPiezasHrs)
                if bandera==True:    
                    self.msgAviso.emit('Aviso','Exito')
                else:
                    self.msgAviso.emit('Aviso','Error en la escritura a la base de datos')
            elif self.__nroPiezasHrs==None:
                self.msgAviso.emit('Aviso','Introdusca solo numeros piezas/Horas')
            else:
                pass
           

    def cargarDataframe(self,df):
        """ Metodo para guardar el dataframe de la tabla sql en esta clase\n
            Paramtros:\n
                df:Dataframe de la tabla sql de las combinaciones molde-maquina\n"""
        self.__df=df
        self.__ProcesarDatos.cargarDataframe(df)
        self.cargarListaSim.emit((self.__ProcesarDatos.listaSim())) #Cargo la lista SIM