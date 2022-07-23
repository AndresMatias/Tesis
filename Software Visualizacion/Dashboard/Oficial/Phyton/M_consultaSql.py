import pyodbc
import pandas as pd
#import sys
from datetime import datetime, timedelta

#-----Mis Clases-----
from Constantes import *
from C_conexionSql import *

def singleton(cls):
    """ Metodo que implementa el patron singleton """
    obj = cls()
    # Siempre devuelve el mismo objeto
    cls.__new__ = staticmethod(lambda cls: obj)
    # Desabilita __init__
    try:
        del cls.__init__
    except AttributeError:
        pass
    return cls

@singleton #Decorador para aplicar el patron singleton a la la clase
class EjecutaConsulta():
    """ Esta clase contiene las consultas sql solo de lectura a la bbdd """
    def __init__(self) -> None:
        #---------Variables que no se setean desde el constructor----------------
        #self.__datosConexion=['VM_TORRETA\SQLEXPRESS','AlladioV01','ngomez_gt','Agosto2020'] #[Nombre del Servidor, nombre de la bbdd, usuario,contraseña]
        self.__datosConexion=None#[Nombre del Servidor, nombre de la bbdd, usuario,contraseña]      
        self.__miConector_1=conexionSql()
        self.__miConexion=None #Nota: EL cursor es obtenido depues de usar el metodo dameConexion y este es usado en el hilo de consultaAutomatico por la cual ya se cuenta con el cursor y no hace falta volver a obtenerlo desde el hilo principal
        self.__bandera=None #Bandera para indicar si se conecto o no correctamente
        self.__CGolpes=None #Vector de numero maximo de golpes de la maquina 

        #---------Variables Preseteadas----------------
        self.__tabla='Piezas_Totales' #Tabla de datos a consultar
        #self.__tabla='Version01' #Tabla de datos a consultar
        # self.__tabla_moldes='Tabla_Moldes' #Tabla donde se van a consultar los moldes para la velocidad
        self.__tabla_moldes='Combinaciones' #Tabla donde se van a consultar los moldes para la velocidad
        #self.__tabla='AlladioV01.dbo.Version01'
        self.__tabla_avisos_importantes='Avisos_Importantes'
        #self.__campos='ID,Fecha,SIM,Golpes,Turno,PiezasHora'
        self.__campos='ID,'+fecha+','+nroMaquina+','+golpes+','+turno+','+piezasHs

    def consulta12Hs(self,sim):
        """ Metodo que prepara una consulta sql de los datos de las ultimas 12 hs
            \nArgumentos:
                sim: int que representa el numero serie de la maquina en la bbdd\n
            \nRetorno:
                Vector de datos de la bbdd
                Golpes de Maquina
                Fecha Actual """

        ahora=datetime.now() #Obtengo fecha y horas actuales locales
        delta=timedelta(hours=12) #Calculo un delta de 12 hs para restar al tiempo actual
        antes=ahora-delta
        antes=str(antes)[:-3] #quito los ultimos 3 digitos porque sino me da error la consulta
        query="SELECT "+self.__campos+" from "+self.__tabla+" where ("+self.__armarStringSims(sim)+") AND Fecha>CONVERT(DATETIME,'"+antes+"',102)" #Consulto a partir de una fecha mayor a la que esta en convert
        datos=self.__baseConsulta(query,sim) #Llamo a al metodo que va a ejecutar mi consulta sql
        return (datos,self.__CGolpes,ahora)	    

    def consultaA(self,year,sim):
        """ Metodo que prepara una consulta sql de lso datos de un año en especifico 
            \nArgumentos:
                year: año que se desea consultar en formato string
                sim: int que representa el numero serie de la maquina en la bbdd\n
            \nRetorno:
                Vector de datos de la bbdd
                Golpes de Maquina
                Fecha Actual """
        
        ahora=datetime.now() #Obtengo fecha y horas actuales locales
        query="SELECT "+self.__campos+" FROM "+self.__tabla+" WHERE ("+self.__armarStringSims(sim)+") AND YEAR(Fecha)="+year #Preparo Consulta
        datos=self.__baseConsulta(query,sim) #Llamo a al metodo que va a ejecutar mi consulta sql
        return (datos,self.__CGolpes,ahora)

    def consultaAM(self,year,month,sim):
        """ Metodo que prepara una consulta sql de lso datos de un año y mes en especifico 
            \nArgumentos:
                    year: año que se desea consultar en formato string
                    month: mes que se desea consultar en formato string
                    sim: int que representa el numero serie de la maquina en la bbdd\n
            \nRetorno:
                Vector de datos de la bbdd
                Golpes de Maquina
                Fecha Actual """
        
        ahora=datetime.now() #Obtengo fecha y horas actuales locales
        query="SELECT "+self.__campos+" FROM "+self.__tabla+" WHERE ("+self.__armarStringSims(sim)+") AND YEAR(Fecha)="+year+"AND MONTH(Fecha)="+month #Preparo Consulta
        datos=self.__baseConsulta(query,sim) #Llamo a al metodo que va a ejecutar mi consulta sql
        return (datos,self.__CGolpes,ahora)

    def consultaAMD(self,year,month,day,sim):
        """ Metodo que prepara una consulta sql de los datos de un año, mes, dia en especifico 
            \nArgumentos:
                        year: año que se desea consultar en formato string
                        month: mes que se desea consultar en formato string
                        day: dia que se desea consultar en formato string
                        sim: int que representa el numero serie de la maquina en la bbdd\n
            \nRetorno:
                Vector de datos de la bbdd
                Golpes de Maquina
                Fecha Actual """

        ahora=datetime.now() #Obtengo fecha y horas actuales locales
        query="SELECT "+self.__campos+" FROM "+self.__tabla+" WHERE ("+self.__armarStringSims(sim)+") AND YEAR(Fecha)="+year+" AND MONTH(Fecha)="+month+"AND DAY(Fecha)="+day #Preparo Consulta
        datos=self.__baseConsulta(query,sim) #Llamo a al metodo que va a ejecutar mi consulta sql
        return (datos,self.__CGolpes,ahora)

    def consultaAMDT(self,ahora,futuro,turno,sim):
        """ Metodo que prepara una consulta sql de los datos de un año, mes, dia y turno en especifico 
        \nArgumentos:
                        ahora: Fecha de inicio del turno 3 consultado\n
                        futuro: Fecha de fin del turno 3 consultado\n
                        turno: turno que se desea consultar en formato string \n
                        sim: tuplas de int que representa el numero serie de la maquina en la bbdd\n
        \nRetorno:
            Vector de datos de la bbdd
            Golpes de Maquina
            Fecha Actual """

        ahora1=datetime.now() #Obtengo fecha y horas actuales locales
        query="SELECT "+self.__campos+" from "+self.__tabla+" where ("+self.__armarStringSims(sim)+") AND (Fecha>=CONVERT(DATETIME,'"+str(ahora)+"',102) AND Fecha<=CONVERT(DATETIME,'"+str(futuro)+"',102)) AND Turno="+turno
        datos=self.__baseConsulta(query,sim) #Llamo a al metodo que va a ejecutar mi consulta sql
        return (datos,self.__CGolpes,ahora1)

    def consultaSims(self):
        """ Metodo que consulta y obtiene las sims de todas las maquinas en la bbdd sin repetir """
        query="SELECT SIM from "+self.__tabla+" GROUP BY SIM" #Agrupo por SIM
        datos=self.__baseConsulta(query,None)
        return datos

    def consultaMoldes(self):
        """ Metodo que consulta todos los moldes con sus respectivas velocidades(normal y lenta) """
        query="SELECT * from "+self.__tabla_moldes #Agrupo por SIM
        datos=self.__baseConsulta(query,None)
        return datos
    
    def consultaAvisos(self):
        """ Metodo que consulta los avisos importantes(corte de luz, violacion, ..., etc)"""
        query="SELECT * from "+self.__tabla_avisos_importantes
        datos=self.__baseConsulta(query,None)
        return datos

    def __baseConsulta(self,query,sim):
        """ Metodo accecible unicamente por la clase que ejecuta las consultas sql preparadas por los metodos anteriores 
            \nArgumentos:
                query: Consulta sql que se desea realizar\n
                sim: Nro de maquina a consultar
            \nRetorno:
                datos: datos de la consulta sql en formato pandas   """
	    #------Varibles Locales----------
        datos=0 
        CGolpes=[]
        #-------------Conexion, Consulta y Manejo de Datos-----------
        try:   
            if sim!=None:
                for i in sim:
                    queryGolpes='SELECT MAX(Golpes) FROM '+self.__tabla+' where SIM='+str(i) #Numero maximpo de Golpes de la maquina
                    datos=pd.read_sql_query(queryGolpes,con=self.__miConexion)
                    #CGolpes.append((i,str(datos.iloc[0,0]))) #[sim,CGolpes]
                    CGolpes.append((str(datos.iloc[0,0])))
                self.__CGolpes=CGolpes #Guardo a nivel clase los datos
            datos=pd.read_sql_query(query,con=self.__miConexion) #Ejecuto consulta con pandas
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

    def dameConexion(self,server,bbdd,user,passw):
        """ Metodo que conenecta a la bbdd, no devuelve nada """
        self.__datosConexion=(server,bbdd,user,passw)
        (self.__miConexion,self.__bandera)=self.__miConector_1.conectar(self.__datosConexion[0],self.__datosConexion[1],self.__datosConexion[2],self.__datosConexion[3])
    
    def cerrarConexion(self):
        """ Metodo que cierra la conexion a la bbdd, no devuelve nada """
        self.__miConector_1.cerrarCursor()
        self.__bandera=False

    def estadoConexion(self):
        """ Metodo que devuelve el estado de conexion de la bbdd, True si esta conectado, False no conectado """
        return self.__miConector_1.estadoConexion()

    def __armarStringSims(self,sim):
        """ Metodo para armar el string de los sims que se van a consultar """
        StringSims=''
        for i in range(0,len(sim)):
            if i!=len(sim)-1:
                StringSims=StringSims+'SIM='+str(sim[i])+' or '
            elif i==len(sim)-1:
                StringSims=StringSims+'SIM='+str(sim[i])
        return StringSims