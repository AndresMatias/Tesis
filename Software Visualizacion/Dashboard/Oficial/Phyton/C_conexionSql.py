import pyodbc

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
class conexionSql():
    """ Clase que implementa un conector a una base de datos sql """
    def __init__(self) -> None:
        #---Variables---
        self.__bandera=False

    def conectar(self,servidor,bbdd,usuario,contrasena):
        """Este metodo(conectar) implementa la conexion a una base de datos y devuelve el cursor para manejarse en dicha base
        \nArgumentos:
            servidor: Nombre del servidor al cual se quiere conectar
            bbdd: Nombre de la base de datos al cual se quiere conectar
            usuario: Usuario aprobado por la bbdd para conectarse
            contrasena: Contraseña del usuario(la variable no utiliza la ñ porque esa letra siempre trae problemas) 
        \nRetorno:
           Conector Sql del tipo objeto devuelto por pyodbc.connect"""
        self.__conexion=None #la declaro antes para usarla fuera del finally
        self.__cursor=None
        #-------------Conexion, Consulta y Manejo de Datos-----------
        try:
            self.__conexion=pyodbc.connect('DRIVER={SQL Server};SERVER='+servidor+';DATABASE='+bbdd+';UID='+usuario+';PWD='+contrasena)    #Especificar el controlador ODBC, el nombre del servidor, la base de datos, etc. directamente
            self.__cursor=self.__conexion.cursor()#Crea un cursor a partir de la conexión  
            self.__bandera=True
        #-----------------------------Excepciones----------------------------
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
            print("Ocurrió un error al conectar a SQL Server: ", err)
        return (self.__conexion,self.__bandera)

    def cerrarCursor(self):
        """ Metodo para cerrar la conexion a la bbdd y cerrar cursor que maneja la consulta sql,no devuelve nada """
        self.__cursor.close()
    
    def estadoConexion(self):
        """ Metodo que devuelve el estado de la conexion """
        return self.__bandera
