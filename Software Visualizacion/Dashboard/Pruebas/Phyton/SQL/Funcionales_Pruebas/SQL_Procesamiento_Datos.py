import pyodbc
from datetime import datetime,time,timedelta
import pandas as pd

def procesamientosIniciales(datos):
    #------Ordeno datos por fechas------
    #datos=datos.sort_values(by="Fecha") #ordeno y reindexo valores, inplace=True para que trabaje sobre el mismo dataframe y drop para que no haga una nueva columna con los antiguos index
    #datos=datos.reset_index() #reindexo
    #datos.drop(['index'],axis=1,inplace=True) #borro columna index de los indices anteriores y trbajo sobre el mismo dataframe(inplace=True)
    
    datos['ContAux'] = 1 #Genero contador auxiliar

    datosAgrupados1= datos.groupby(pd.Grouper(key='Fecha', freq='H')).sum() # groupby each 1 month
    #datosAgrupados2= datos.groupby(pd.Grouper(key='Turno')).sum() # groupby each 1 month
    
    vec=datosAgrupados1['ContAux']
    datosAgrupados1

    print(vec)
    print("")
    #print(datosAgrupados2)
        


#-----Parametros de Conexion-----
direccion_servidor='DESKTOP-TVTMCR0'
nombre_bd='Inyectora'
nombre_usuario ='alladio'
password='12345'

try:
    #-----Especificar el controlador ODBC, el nombre del servidor, la base de datos, etc. directamente-----
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)
    cursor=conexion.cursor()

    #-----Armo Consulta SQL-----
    ahora=datetime.now() #Obtengo fecha y horas actuales locales
    delta=timedelta(hours=12) #Calculo un delta de 12 hs para restar al tiempo actual
    antes=ahora-delta
    antes=str(antes)[:-3] #quito los ultimos 3 digitos porque sino me da error la consulta
    query="SELECT ID,Fecha,SIM,Golpes,Turno from Tabla_Pruebas2 where Fecha>CONVERT(DATETIME,'"+antes+"',102)" #Consulto Ultimas 12hs
    #query="SELECT ID,Fecha,SIM,CGolpes,Turno from Tabla_Pruebas1 WHERE YEAR(Fecha)=2021 AND SIM=1" #Consulto un año
    #query='SELECT * from Tabla_Pruebas1'

    #-----Ejecuto consulta SQL a la bbdd mediante pandas-----
    df=pd.read_sql_query(query,con=conexion)
    
    
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
finally:
    cursor.close()

#-----Funcion a Probar-----
#procesamientosIniciales(df)

#-----Imprimo Datos-----
print(len(df))

print("Fin Programa")    