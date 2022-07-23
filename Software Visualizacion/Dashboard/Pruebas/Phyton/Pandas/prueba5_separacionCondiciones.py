import pyodbc
from datetime import datetime,time
import pandas as pd
import numpy as np
import locale
from timeit import timeit
from timeit import default_timer as timer
locale.setlocale(locale.LC_ALL, 'es-ES') 

def separacionDatos2(df):
        #------Ordeno datos por fechas------
        df=df.sort_values(by="Fecha") #ordeno y reindexo valores, inplace=True para que trabaje sobre el mismo dataframe y drop para que no haga una nueva columna con los antiguos index
        df=df.reset_index() #reindexo
        df.drop(['index'],axis=1,inplace=True) #borro columna index de los indices anteriores y trbajo sobre el mismo dataframe(inplace=True)
        #-----Calculo velocidades y colores-------
        df['vel']=df['Fecha'].diff().dt.total_seconds() #Resultado en timedelta pasados a segundos puedo usarlo para la barra de estado
        
        #Nota: talvez pueda en las constate poner df['vel_hr']
        condiciones = [
        (df['vel'] >= df['ID']) & (df['vel'] < df['ID']), #Vel lenta 
        (df['vel'] >=df['ID']) & (df['vel'] < df['ID']), #Vel Fuera de rango
        (df['vel'] < df['ID']), #Vel normal
        (df['vel'] >= df['ID'] )] #Parada

        colores = ['yellow', 'orange', 'green','red']
        df['color'] = np.select(condiciones, colores, default='white')
        # print(df)

def separacionDatos(df):
        velocidadNominal=0
        velocidad=[]
        velocidadLenta=0
        fueraRango=0
        coloresIndicadores=("#FFFFFF","#FFF700","#36FF00","#FF0000","#FF6800") #coloresIndicadores(no se sabe(blanco),velocidad lenta(amarrillo), velocidadad normal(verde), detenida(rojo), fuera de rango(naranja))
         #----Variable Locales para velocidades acumulativas----
        cont1=0 #Contador de piezas de mayor velocidad
        cont2=0 #Contador de piezas de menor velocidad
        cont3=1 #Contador de piezas fuera de rango
        vel=0 #velocidad actual

        #----Variables Locales para color de estado----
        color=[]
        
        #------El primer elemento de la lista nunca tengo con que compararlo por lo cual es desconocido-------
        velocidad.append(0) 
        color.append(coloresIndicadores[0]) 
        
        #------Determino velocidades, estados, etc------
        for i in range(1,len(df)):
            antes=datetime(df.loc[i-1,'Fecha'].year,df.loc[i-1,'Fecha'].month,df.loc[i-1,'Fecha'].day)
            ahora=datetime(df.loc[i,'Fecha'].year,df.loc[i,'Fecha'].month,df.loc[i,'Fecha'].day)
            if antes==ahora and df.loc[i-1,'Turno']==df.loc[i,'Turno']: #Si el elmento actual es igual en año,mes,dia y turno al actual
                #------Calcula de velocidad-----------
                antes=datetime(df.loc[i-1,'Fecha'].year,df.loc[i-1,'Fecha'].month,df.loc[i-1,'Fecha'].day,df.loc[i-1,'Fecha'].hour,df.loc[i-1,'Fecha'].minute,df.loc[i-1,'Fecha'].second,df.loc[i-1,'Fecha'].microsecond)
                ahora=datetime(df.loc[i,'Fecha'].year,df.loc[i,'Fecha'].month,df.loc[i,'Fecha'].day,df.loc[i,'Fecha'].hour,df.loc[i,'Fecha'].minute,df.loc[i,'Fecha'].second,df.loc[i,'Fecha'].microsecond)
                vel=(ahora-antes).total_seconds()

                #----------------------------------------------------------------------------
                #Nota: Podria utilizar pandas para agrupar de acuerdo a la velocidad para crear los contadores
                #----------------------------------------------------------------------------
                if vel>float(velocidadNominal) and vel<float(velocidadLenta): #Piezas que tardaron mas
                    cont2=cont2+1
                    color.append(coloresIndicadores[1]) #Amarillo
                   
                elif vel<=float(velocidadNominal): #Piezas que tardaron menos
                    cont1=cont1+1
                    color.append(coloresIndicadores[2]) #Verde

                elif vel>=float(velocidadLenta) and vel<float(fueraRango): #Piezas Fuera de Rango
                    cont3=cont3+1
                    color.append(coloresIndicadores[4]) #Naranja
                
                elif vel>=float(fueraRango): #Maquina StanBy en el mismo turno
                    color.append(coloresIndicadores[3])  #Rojo

                else:
                    pass
                velocidad.append(vel)
            else:
                antes=datetime(df.loc[i-1,'Fecha'].year,df.loc[i-1,'Fecha'].month,df.loc[i-1,'Fecha'].day,df.loc[i-1,'Fecha'].hour,df.loc[i-1,'Fecha'].minute,df.loc[i-1,'Fecha'].second,df.loc[i-1,'Fecha'].microsecond)
                ahora=datetime(df.loc[i,'Fecha'].year,df.loc[i,'Fecha'].month,df.loc[i,'Fecha'].day,df.loc[i,'Fecha'].hour,df.loc[i,'Fecha'].minute,df.loc[i,'Fecha'].second,df.loc[i,'Fecha'].microsecond)
                velocidad.append((ahora-antes).total_seconds()) #Pieza que no tiene comparacion
                color.append(coloresIndicadores[3]) #Rojo

#-----Parametros de Conexion-----
direccion_servidor='DESKTOP-TVTMCR0'
nombre_bd='AlladioV01'
nombre_usuario ='alladio'
password='12345'

try:
    #-----Especificar el controlador ODBC, el nombre del servidor, la base de datos, etc. directamente-----
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)

    #-----Armo Consulta SQL-----
    query='SELECT * FROM Version01 where SIM=5060001 and YEAR(Fecha)=2021'

    #-----Ejecuto consulta SQL a la bbdd mediante pandas-----
    df=pd.read_sql_query(query,con=conexion)

    #-----Ordeno Datos-----
    print('Tamaño del dataframe: ',len(df))
    start =timer() #Inicio para medir tiempo
    separacionDatos2(df)
    end =timer() #Fin para medir tiempo
    print ('Tiempo de Ejecucion con pandas',end-start)

    start =timer() #Inicio para medir tiempo
    separacionDatos(df)
    end =timer() #Fin para medir tiempo
    print ('Tiempo de Ejecucion sin pandas',end-start)


except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
finally:
    pass
    #cursor.close()
print("Fin Programa")   