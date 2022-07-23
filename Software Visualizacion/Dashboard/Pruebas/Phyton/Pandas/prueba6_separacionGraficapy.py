import pyodbc
import matplotlib.pyplot as plt
from datetime import datetime,time
import pandas as pd
import numpy as np
import locale
from timeit import timeit
from timeit import default_timer as timer
locale.setlocale(locale.LC_ALL, 'es-ES') 

def separacionDatos(df):
        #------Ordeno datos por fechas------
        df=df.sort_values(by="Fecha") #ordeno y reindexo valores, inplace=True para que trabaje sobre el mismo dataframe y drop para que no haga una nueva columna con los antiguos index
        df=df.reset_index() #reindexo
        df.drop(['index'],axis=1,inplace=True) #borro columna index de los indices anteriores y trbajo sobre el mismo dataframe(inplace=True)
        
        #----Calculo de velocidades de comparacion en base a Piezas Hora----
        df['vel_normal']=(3600/df['PiezaHora'])
        df['vel_lenta']=df['vel_normal']+(df['vel_normal']*0.10)  #Tolerancia del 10%
        df['vel_fueraRango']=df['vel_normal']+(df['vel_normal']*0.20)  #Tolerancia del 20% con respecto a la velocidad normal
        
        #-----Calculo velocidades y colores-------
        df['vel']=df['Fecha'].diff().dt.total_seconds() #Resultado en timedelta pasados a segundos puedo usarlo para la barra de estado
        df.loc[0,'vel']=0

        condiciones = [
        (df['vel'] >= df['vel_normal']) & (df['vel'] < df['vel_lenta']), #Vel lenta 
        (df['vel'] >=df['vel_lenta']) & (df['vel'] < df['vel_fueraRango']), #Vel Fuera de rango
        (df['vel'] < df['vel_normal']), #Vel normal
        (df['vel'] >= df['vel_fueraRango'])] #Parada

        colores = ['yellow', 'orange', 'green','red']
        df['color'] = np.select(condiciones, colores, default='white')
        #df['cord']=df['vel'].cumsum() #Vector de dezplazamiento

        # velocidad=df['vel'].to_numpy() #Lista de velocidades
        # color=df['color'].to_numpy() #Lista de colores de cada pieza
        # coord=df['cord'].to_numpy()#Coordenadas para graficar barra de estado

        #----Genero mascaras-----
        mask1=df['color'].eq(df['color'].shift(periods=1)) #Creo un df dezplado una poscion adelante y comparo
        mask2=df['color'].eq(df['color'].shift(periods=-1)) #Creo un df dezplado una poscion atras y comparo
        df['mask']=mask1&mask2 #mascara resultante para diesmar datos repetidos en intervalos


        #----Aplico mascara y separo datos----
        dfAux=pd.DataFrame(df[df['mask']==False]) #Dataframe auxiliar con los datos diezmados
        dfAux['velAux']=dfAux['Fecha'].diff().dt.total_seconds() #Velocidades Auxiliares para cada segmento de color
        dfAux.loc[0,'velAux']=0

        vecC=dfAux['color'].to_numpy() #Extraigo vector de colores en numpy(numpy es mas rapido de procesar)
        vecV=dfAux['velAux'].to_numpy()


        #---------Pruebas-------------------
        cont_1=len(df[df['color']=='green'])
        cont_2=len(df[df['color']=='yellow'])
        cont_3=len(df[df['color']=='orange'])
        dfAux2=df['color'].value_counts()

        print()
        print(dfAux2)
        print()
        print(cont_1)
        print(cont_2)
        print(cont_3)



        #print(df['vel_lenta'])
        print("Tamaño del dataframe diesmado: ",len(dfAux))
        # print("Tamaño del dataframe diesmado 2: ",len(vecC))

        #---Datos Diezmados
        posX=0
        for i in range(0,len(vecC)):
            plt.barh('2021',vecV[i],color=vecC[i],left=posX)
            posX=posX+vecV[i] #Determina la poscion en el eje x para graficar la siguiente barra
        plt.show()

        #---Datos NO Diezmados
        # posX=0
        # for i in range(0,len(velocidad)):
        #     plt.barh('2022',velocidad[i],color=color[i],left=posX)
        #     posX=posX+velocidad[i] #Determina la poscion en el eje x para graficar la siguiente barra

        # plt.show()

def separacionDatos2(df):
        #------Ordeno datos por fechas------
        df=df.sort_values(by="Fecha") #ordeno y reindexo valores, inplace=True para que trabaje sobre el mismo dataframe y drop para que no haga una nueva columna con los antiguos index
        df=df.reset_index() #reindexo
        df.drop(['index'],axis=1,inplace=True) #borro columna index de los indices anteriores y trbajo sobre el mismo dataframe(inplace=True)
        #-----Calculo velocidades y colores-------
        df['vel']=df['Fecha'].diff().dt.total_seconds() #Resultado en timedelta pasados a segundos puedo usarlo para la barra de estado
        df.loc[0,'vel']=0

        #Nota: talvez pueda en las constate poner df['vel_hr']
        normal=3600
        lento=3700
        fueraRango=3800
        parado=4000

        condiciones = [
        (df['vel'] >= normal) & (df['vel'] < lento), #Vel lenta 
        (df['vel'] >=lento) & (df['vel'] < fueraRango), #Vel Fuera de rango
        (df['vel'] < normal), #Vel normal
        (df['vel'] >= parado)] #Parada

        colores = ['yellow', 'orange', 'green','red']
        df['color'] = np.select(condiciones, colores, default='white')
        df['cord']=df['vel'].cumsum() #Vector de dezplazamiento

        print(df)

        vecaux=[50,50,50,50,50,50,50,50]
        #----Vectores de dimension de datos---(puedo usar vector de dezplamiento aca directamente)
        vel_normal = np.ma.masked_where(float(normal) <= df['vel'], df['cord'])  
        vel_lenta = np.ma.masked_where((float(normal)>df['vel'] ) | (float(lento)<df['vel'] ), df['cord'])
        vel_fueraRango = np.ma.masked_where((float(lento)>= df['vel']) | (float(fueraRango)<df['vel'] ), df['cord'])
        vel_detenido = np.ma.masked_where((float(fueraRango)>=df['vel'] ), df['cord'])

        print('----Verde----')
        print(vel_normal)
        print('----Amarillo----')
        print(vel_lenta)
        print('----Naranja----')
        print(vel_fueraRango)
        print('----Rojo----')
        print(vel_detenido)

        #Podria sacar el vector de dezplazamiento y con mascara eliminar 
        y=np.zeros(len(df['vel']))

        plt.scatter(vel_normal, y,color='green')
        # plt.plot(vel_normal, y,linewidth=100.0,color='green')
        
        plt.scatter(vel_lenta, y,color='yellow')
        # plt.plot(vel_lenta, y,linewidth=100.0,color='yellow')
        
        plt.scatter(vel_fueraRango, y,color='orange')
        # plt.plot(vel_fueraRango,y,linewidth=100.0,color='orange')
        
        plt.scatter(vel_detenido, y,color='red')
        # plt.plot(vel_detenido,y,linewidth=100.0,color='red')
        
        # plt.show()

        # fig, ax = plt.subplots()
        # ax.plot(vel_normal,y, vel_lenta, y, vel_fueraRango, y,vel_detenido,y,linewidth=100.0)
        plt.show()


#-----Parametros de Conexion-----
direccion_servidor='DESKTOP-TVTMCR0'

# nombre_bd='Inyectora'
nombre_bd='AlladioV01'

nombre_usuario ='alladio'
password='12345'

try:
    #-----Especificar el controlador ODBC, el nombre del servidor, la base de datos, etc. directamente-----
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)

    #-----Armo Consulta SQL-----
    # query='SELECT * FROM Tabla_Pruebas2 where SIM=5600438 and YEAR(Fecha)=2021'
    query='SELECT * FROM Version01 where SIM=5600438 and ( YEAR(Fecha)=2021 and MONTH(Fecha)=09 and DAY(Fecha)=22)'

    #-----Ejecuto consulta SQL a la bbdd mediante pandas-----
    df=pd.read_sql_query(query,con=conexion)

    #-----Ordeno Datos-----
    print('Tamaño del dataframe: ',len(df))
    # start =timer() #Inicio para medir tiempo
    separacionDatos(df)
    # end =timer() #Fin para medir tiempo
    # print ('Tiempo de Ejecucion con pandas',end-start)

except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
finally:
    pass
    #cursor.close()
print("Fin Programa")   