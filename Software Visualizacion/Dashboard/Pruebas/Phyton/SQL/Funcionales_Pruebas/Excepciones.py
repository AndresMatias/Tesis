import pyodbc
#-------------Parametros  de Conexion-------------- 
direccion_servidor='DESKTOP-TVTMCR0'
nombre_bd='Inyectora'
nombre_usuario ='alladio'
password='12345'
#-------------Conexion, Consulta y Manejo de Datos-----------
try:
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)    #Especificar el controlador ODBC, el nombre del servidor, la base de datos, etc. directamente
    cursor=conexion.cursor()#Crea un cursor a partir de la conexión
    query=('INSERT INTO Tabla_Pruebas(Fecha) Values(CURRENT_TIMESTAMP)')
    cursor.execute(query)
    cursor.commit()
    #------------------#Muestro Informacion---------------------
    for i in cursor:
        print(i) #Muestro Informacion
    #-----------------------------------------------------------    

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
except pyodbc.DatabaseError as err: #Clase base de las excepciones previamente mostradas
    print("Ocurrió un error del tipo 'DatabaseError': \n", err)
except pyodbc.Error as err: #Excepcion Clase base de pyodbc, puedo detectar el resto solo con esta
    print("Ocurrió un error del tipo 'Error': \n", err)
except pyodbc.Warning as err: #Excepcion Clase base de pyodbc, puedo detectar el resto solo con esta
    print("Ocurrió un error del tipo 'Warning': \n", err)
finally:
    cursor.close()

print("Fin Programa")
#Estructura Gerarquica de las Excepciones de pyodbc
'''
StandardError 
| __Warning 
| __Error 
   | __InterfaceError 
   | __DatabaseError 
      | __DataError 
      | __OperationalError 
      | __IntegrityError 
      | __InternalError 
      | __ProgrammingError 
      | __NotSupportedError
'''
#--------------------------------------------------------------------

'''Nota: Si imprimo toda la excecion 'err' se imprime el numero de causa que se peude ver en la tabla de sqlstate mas la causa del error
        pero si inserto dentro de cada excecpion el siguiente codigo y no imprimo 'err': 
            sqlstate = err.args[1]
            print(sqlstate)
        solo se muestra la causa y no el numero de codigo, y si en args cambio el 1 por el 0 se imprime SOLO numero de causa'''

#https://stackoverflow.com/questions/11392709/how-to-catch-specific-pyodbc-error-message Ver pq se puede mejorar la precision de lo que esta pasando para que el usuario tenga idea