from PyQt5.QtCore import *
import pandas as pd

#----Mis Clases----
from Constantes import *

class ProcesarDatos(QObject):
    """ Clase que procesa los datos con pandas de la tabla sql """
    def __init__(self):
        super().__init__()
        self.__df=None #DataFrame de tabla SQL
    
    def cargarDataframe(self,df):
        """ Metodo para guardar el dataframe de la tabla sql en esta clase\n
            Paramtros:\n
                df:Dataframe de la tabla sql de las combinaciones molde-maquina\n"""
        self.__df=df
    
    def listaSim(self):
        """ Metodo que extrae la lista de las maquinas sim de la tabla sin repetir\n
            Retorno:\n
               listaSim: Lista con la cantidad de maquinas disponibles """
        return(['SIM']+(self.__df[simSql].unique().astype(str).tolist())) #Lista de SIM sin repetir

    def listaMolde(self,sim):
        """ Metodo que extrae la lista de los moldes de la tabla en base a la sim escogida\n
            Parametros:\n
                sim: Nro de identificacion de la maquina seleccionada\n
            Retorno:\n
                listaMoldes: Lista con la cantidad de moldes disponibles en base a la sim escogida """
        dfAux=self.__df[self.__df[simSql]==float(sim)] #Extraigo nuevo dataframe en base a la sim seleccionada      
        return(['Moldes']+(dfAux[moldeSql].unique().tolist()))        

    def listaCodigo(self,sim,molde):
        """ Metodo que extrae la lista de los codigos de la tabla en base al molde escogido\n
            Parametros:\n
                sim: Nro de identificacion de la maquina seleccionada\n
                molde: Molde seleccionado\n
            Retorno:\n
               listaCodigos: Lista con la cantidad de codigos disponibles en base al molde escogido """
        dfAux=self.__df[(self.__df[simSql]==float(sim)) & (self.__df[moldeSql]==molde)] 
        return(['Codigos']+(dfAux[codigoSql].unique().astype(str).tolist()))   #Devuelvo lista de codigos en formato string

    def listaId(self,sim,molde,codigo):
        """ Metodo que determina el id de la combinacion sim-molde-codigo\n
            Parametros:\n
                sim: Nro de identificacion de la maquina seleccionada\n
                molde: Molde seleccionado\n
                codigo: Codigo seleccionado de la combinacion de la tabla sql\n
            Retorno:\n
               id: id de la combinacion escogida(devuleve false si hay mas de un id) """
        dfAux=self.__df[(self.__df[simSql]==float(sim)) & (self.__df[moldeSql]==molde) & (self.__df[codigoSql]==float(codigo))]
        id=dfAux[idSql].astype(str).tolist()
        if len(id)>1:
            return False
        elif len(id)==1:
            return id[0] #Retorno Id