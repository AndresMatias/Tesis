import pyodbc
from datetime import datetime,time
import pandas as pd
import numpy as np
import locale
from timeit import timeit
locale.setlocale(locale.LC_ALL, 'es-ES') 

def separacionDatos(df):
    df2=[] #Lista de dataframe por sim
    df1=df.groupby('SIM') #Agrupo por sim
    sim=list(df1.groups.keys()) #Obtengo los grupos sim y los pongo en una lista
    #for i in range(0,len(sim)): #Primer for Analisis por SIM)
    for i in range(0,len(sim)):
        dfAux=df1.get_group(int(sim[i]))    
        #------Ordeno datos por fechas------
        dfAux=dfAux.sort_values(by="Fecha") #ordeno y reindexo valores, inplace=True para que trabaje sobre el mismo dataframe y drop para que no haga una nueva columna con los antiguos index
        dfAux=dfAux.reset_index() #reindexo
        dfAux.drop(['index'],axis=1,inplace=True) #borro columna index de los indices anteriores y trbajo sobre el mismo dataframe(inplace=True)
        df2.append(dfAux) #Guardo Datos
        # print(dfAux.dtypes)
        # print(dfAux['Fecha'].diff())
        dfAux['Fecha'].diff()

def separacionDatos2(df):
        #------Ordeno datos por fechas------
        df=df.sort_values(by="Fecha") #ordeno y reindexo valores, inplace=True para que trabaje sobre el mismo dataframe y drop para que no haga una nueva columna con los antiguos index
        df=df.reset_index() #reindexo
        df.drop(['index'],axis=1,inplace=True) #borro columna index de los indices anteriores y trbajo sobre el mismo dataframe(inplace=True)
        #-----Calculo velocidades y colores-------
        df['vel']=df['Fecha'].diff().dt.total_seconds() #Resultado en timedelta pasados a segundos puedo usarlo para la barra de estado
        
        #Nota: talvez pueda en las constate poner df['vel_hr']
        condiciones = [
        (df['vel'] >= 3600) & (df['vel'] < 6000), #Vel lenta 
        (df['vel'] >=6000) & (df['vel'] < 10000), #Vel Fuera de rango
        (df['vel'] < 3600 ), #Vel normal
        (df['vel'] >= 10000 )] #Parada

        colores = ['yellow', 'orange', 'green','red']
        df['color'] = np.select(condiciones, colores, default='white')
        print(df)

#-----Parametros de Conexion-----
direccion_servidor='DESKTOP-TVTMCR0'
nombre_bd='Inyectora'
nombre_usuario ='alladio'
password='12345'

try:
    #-----Especificar el controlador ODBC, el nombre del servidor, la base de datos, etc. directamente-----
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)

    #-----Armo Consulta SQL-----
    query='SELECT * FROM Tabla_Pruebas2 where SIM=5600438 and YEAR(Fecha)=2021'

    #-----Ejecuto consulta SQL a la bbdd mediante pandas-----
    df=pd.read_sql_query(query,con=conexion)

    #-----Ordeno Datos-----
    # df=df.sort_values(by="Fecha").reset_index() #Ordeno por fecha y reindexo para acceder con un for ordenamente al reordenamiento de fecha
    start =timeit() #Inicio para medir tiempo
    separacionDatos2(df)
    end =timeit() #Fin para medir tiempo
    print ('Tiempo de Ejecucion',end-start)
    # print(dfa)
    # print(sim)


except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
finally:
    pass
    #cursor.close()

# print(listaTiempo[1])
# print(listaEstado[:])
print("Fin Programa")   