import pyodbc
from datetime import datetime,time,timedelta
import pandas as pd


#-----Parametros de Conexion-----
direccion_servidor='DESKTOP-TVTMCR0'
nombre_bd='Inyectora'
nombre_usuario ='alladio'
password='12345'

try:
    #-----Especificar el controlador ODBC, el nombre del servidor, la base de datos, etc. directamente-----
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)
    cursor=conexion.cursor()

    #-----Armo Consulta SQL para averiguar sim sin repetir-----
    query="SELECT SIM from Tabla_Pruebas1 GROUP BY SIM" #Agrupo por SIM

    #-----Ejecuto consulta SQL a la bbdd mediante pandas-----
    df=pd.read_sql_query(query,con=conexion)
    print(df)
    
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
finally:
    cursor.close()
