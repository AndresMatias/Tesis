import pyodbc
from datetime import datetime,time
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, 'es-ES') 

#-----Parametros de Conexion-----
direccion_servidor='DESKTOP-TVTMCR0'
nombre_bd='Inyectora'
nombre_usuario ='alladio'
password='12345'

try:
    #-----Especificar el controlador ODBC, el nombre del servidor, la base de datos, etc. directamente-----
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)

    #-----Armo Consulta SQL-----
    query='SELECT * FROM Tabla_Pruebas2'

    #-----Ejecuto consulta SQL a la bbdd mediante pandas-----
    df=pd.read_sql_query(query,con=conexion)

    #-----Ordeno Datos-----
    df=df.sort_values(by="Fecha").reset_index() #Ordeno por fecha y reindexo para acceder con un for ordenamente al reordenamiento de fecha
    print(df)
    #Nota: con strftime puedo cambiar el formato en vez que diga friday puede que diga el numero del dia y asi con los meses
    df['Dia'] = df['Fecha'].dt.strftime('%A') #Creo columna solo con el dia
    df['Mes'] = df['Fecha'].dt.strftime('%B') #Creo columna solo con el mes
    df['Año'] = df['Fecha'].dt.strftime('%Y') #Creo columna solo con el año
    df['Hora'] = df['Fecha'].dt.strftime('%H:%M:%S') #Creo columna solo con la hora
    print(df)


except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
finally:
    pass
    #cursor.close()

# print(listaTiempo[1])
# print(listaEstado[:])
print("Fin Programa")   