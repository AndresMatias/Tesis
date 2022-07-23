import pyodbc
from datetime import datetime,time
import pandas as pd
   
#-----Parametros de Conexion-----
direccion_servidor='DESKTOP-TVTMCR0'
nombre_bd='Inyectora'
nombre_usuario ='alladio'
password='12345'

try:
    #-----Especificar el controlador ODBC, el nombre del servidor, la base de datos, etc. directamente-----
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)

    #-----Armo Consulta SQL-----
    query='select * from Tabla_Pruebas1'
    q2='SELECT MAX(CGolpes) FROM Tabla_Pruebas1 where SIM=1'

    #-----Ejecuto consulta SQL a la bbdd mediante pandas-----
    golpes=pd.read_sql_query(q2,con=conexion)
    df=pd.read_sql_query(query,con=conexion)

    #-----Ordeno Datos-----
    #print(df)
    #df=df.sort_values(by="Fecha") #Ordenar por fechas
    #df=df.reset_index() #Reindexo pq si bien se ordena pro fecha cuando accedo pro indice si no se reinici conserva su indice de identificacion inicial
    df=df.sort_values(by="Fecha").reset_index() #Ordeno por fecha y reindexo para acceder con un for ordenamente al reordenamiento de fecha
    #print(df)
    #print(golpes.iloc[0,0])
    print(golpes)
    print(len(golpes))
    print(len(df))

except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
finally:
    pass
    #cursor.close()

# print(listaTiempo[1])
# print(listaEstado[:])
print("Fin Programa")    