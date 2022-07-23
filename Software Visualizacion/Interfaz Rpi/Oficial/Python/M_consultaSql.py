import pyodbc
import pandas as pd

from C_conexionSql import *

def singleton(cls): #Implemento patron singleton para EjecutaConsulta
    obj = cls()
    # Siempre devuelve el mismo objeto
    cls.__new__ = staticmethod(lambda cls: obj)
    # Desabilita __init__
    try:
        del cls.__init__
    except AttributeError:
        pass
    return cls

@singleton #Decorador para implementar singleton
class EjecutaConsulta():
    """ Esta clase contiene las consultas sql solo de lectura a la bbdd """
    def __init__(self) -> None:
        #---------Variables que no se setean desde el constructor----------------
        self.__datosConexion=None#[Nombre del Servidor, nombre de la bbdd, usuario,contraseña]      
        self.__miConector_1=conexionSql()
        self.__miConexion=None #Nota: EL cursor es obtenido depues de usar el metodo dameConexion y este es usado en el hilo de consultaAutomatico por la cual ya se cuenta con el cursor y no hace falta volver a obtenerlo desde el hilo principal
        #---------Variables Preseteadas----------------
        self.__tabla='Combinaciones' #Tabla de datos a consultar
        self.__campos='*'

    def consultaTabla(self):
        """ Metodo que consulta toda la tabla de combinaciones al pincipio del programa """
        query="SELECT "+self.__campos+" from "+self.__tabla #Consulto a partir de una fecha mayor a la que esta en convert
        datos=self.__baseConsulta(query,False)
        return datos
    
    def escribirID(self,sim,ID,piezasHrs):
        """ Metodo que escribe el ID de la combinacion seleccionado en todos los campos IdCode que compartan la sim seleccionada\n
            Parametros:\n
                sim: Nro de identificacion de la maquina seleccionada\n
                ID: id(de la tabla sql consultada al principio del programa) de la combinacion sim-molde-codigo\n
                piezasHrs: Numero de piezas por horas\n """
        query="UPDATE "+self.__tabla+" SET IdCode="+ID+",PiezasHoras="+piezasHrs+" where SIM="+sim
        bandera=self.__baseConsulta(query,True)
        return bandera

    def __baseConsulta(self,query,bandera):
        """ Metodo accecible unicamente por la clase que ejecuta las consultas sql preparadas por los metodos anteriores\n
            Argumentos:\n
                query: Consulta sql que se desea realizar\n
                bandera: Para indicar si es una consulta de lectura o una escritura a la bbdd(False: lectura, True: Escritura)\n
            Retorno:\n
                datos: datos de la consulta sql en formato pandas """
	    #------Varibles Locales----------
        datos=False #Por Defecto en caso de que algo falle 
        #-------------Conexion, Consulta y Manejo de Datos-----------
        try: 
            if bandera==False: #Lectura a la bbdd
                datos=pd.read_sql_query(query,con=self.__miConexion) #Ejecuto consulta con pandas
            else:
                cursor=self.__miConector_1.dameCursor()#Obtengo el cursor para escribir en al BBDD
                cursor.execute(query) #Escritura a la bbdd
                cursor.commit() #Confirmo Escritura
                datos=True #Para indicar que se escribio con exito
		#-----------------------------Excepciones SQL----------------------------
        except pyodbc.OperationalError as err:
            print("Ocurrió un error del tipo 'OperationalError': \n", err)
        except pyodbc.DataError as err:
            print("Ocurrió un error del tipo 'DataError': \n", err)
        except pyodbc.IntegrityError as err:
            print("Ocurrió un error del tipo 'IntegrityError': \n", err)
        except pyodbc.InternalError as err:
            print("Ocurrió un error del tipo 'InternalError': \n", err)
        except pyodbc.ProgrammingError as err:
            print("Ocurrió un error del tipo 'ProgrammingError': \n", err)
        except pyodbc.NotSupportedError as err:
            print("Ocurrió un error del tipo 'NotSupportedError': \n", err)
        except pyodbc.DatabaseError as err: 
            print("Ocurrió un error del tipo 'DatabaseError': \n", err)
        except pyodbc.Error as err: #Excepcion Clase base de pyodbc, puedo detectar el resto solo con esta
            print("Ocurrió un error del tipo 'Error': \n", err)
        except pyodbc.Warning as err: #Excepcion Clase base de pyodbc, puedo detectar el resto solo con esta
            print("Ocurrió un error del tipo 'Warning': \n", err)
        except Exception as err: #Excepcion base que captura cualquier excepcion
            # Atrapar error
            print("Ocurrió un error al conectar a SQL Server 2: ", err)
        return datos 

    def dameConexion(self,server,bbdd,user,passw,puerto):
        """ Metodo que conenecta a la bbdd, no devuelve nada\n 
            Parametros:\n
                server: Ip de la maquina\n
                bbdd: Nombre de la base de datos\n
                user: Usuario\n
                passw: Contraseña\n
                puerto: Puerto de conexion(COnfigurable en la maquina donde esta la bbdd)\n """
        self.__datosConexion=(server,bbdd,user,passw,puerto)
        (self.__miConexion,self.__bandera)=self.__miConector_1.conectar(self.__datosConexion[0],self.__datosConexion[1],self.__datosConexion[2],self.__datosConexion[3],self.__datosConexion[4])
    
    def cerrarConexion(self):
        """ Metodo que cierra la conexion a la bbdd, no devuelve nada """
        self.__miConector_1.cerrarCursor()
        self.__bandera=False

    def estadoConexion(self):
        """ Metodo que devuelve el estado de conexion de la bbdd, True si esta conectado, False no conectado """
        return self.__miConector_1.estadoConexion()