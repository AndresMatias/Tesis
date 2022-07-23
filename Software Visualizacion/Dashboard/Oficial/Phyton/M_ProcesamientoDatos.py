from datetime import datetime,time, timedelta,date

import math
import pandas as pd
import numpy as np
import locale
import matplotlib.pyplot as plt
from timeit import default_timer as timer

#-----Mis Clases-----
from Constantes import *
locale.setlocale(locale.LC_ALL, 'es-ES') #Para formato fechas en español

#----------------------------------------------------------------------------------------------------------------------------------
#NOTAS:
#----------------------------------------------------------------------------------------------------------------------------------
class SeparacionDatos():
    """ Esta clase separa los datos por sim """
    def __init__(self) -> None:
        pass

    def separacionDatos(self,df,datosMaquinas):
        """ Este metodo separa y ordena(por fecha y reindexa) los datos por sim en distintos dataframes\n
            Retorno:\n
                df2: Lista de dataframe por maquina\n
                sim: Lista sim consultada ordenada en el mismo orden de los dataframe\n
                Golpes: Lista de golpes maximo de cada sim ordenada en el mismo orden de los dataframe\n
                banderaAux: Indica si todas las sim tienen datos(True) o hay alguno que no(False)\n """
        #------Variables----------
        df2=[] #Lista de dataframe por sim
        Golpes=[]
        banderaAux=False

        #---Preprocesamiento----
        df1=df.groupby(nroMaquina) #Agrupo por sim
        sim=list(df1.groups.keys()) #Obtengo las calves de grupos sim y los pongo en una lista
        if len(sim)==len(datosMaquinas):
            banderaAux=True #Todas las sims consutladas tienen datos
        
        #----Separacion de Datos----     
        for i in range(0,len(sim)): #Primer for Analisis por SIM
            dfAux=df1.get_group(int(sim[i]))
            #--------Ordeno las velocidades y golpes en el orden de los sims de los dataframe----------
            for j in range(0,len(datosMaquinas)):
                if int(sim[i])==int(datosMaquinas[j][0]):
                    Golpes.append(datosMaquinas[j][1])
            #------Ordeno datos por fechas------
            dfAux=dfAux.sort_values(by=fecha) #ordeno y reindexo valores, inplace=True para que trabaje sobre el mismo dataframe y drop para que no haga una nueva columna con los antiguos index
            dfAux=dfAux.reset_index() #reindexo
            dfAux.drop(['index'],axis=1,inplace=True) #borro columna index de los indices anteriores y trbajo sobre el mismo dataframe(inplace=True)
            df2.append(dfAux) #Guardo Datos
        
        return df2,sim,Golpes,banderaAux

class ProcesamientosDatos():
    """ El proposito de esta clase es procesar los datos de la consulta sql para poner ordenarlos de tal forma que sean 
    legibles para las clases que grafican los datos y muestran en las etiquetas labels"""
    def __init__(self,datosEstado,indicadorConsulta,Golpes,ahora,filtroTiempo) -> None:
        """ El constructor de esta clase inicializa las variables a utilizar, ordena las datos segun las fechas con un metodo accesible solo por la clase y
        calcula la velocidad de cada pieza
        \nArgumentos:
            datosEstado: Dataframe de la consulta Sql\n
            indicadorConsulta:  Es un int que me indica si que tipo de consulta sql se realizo:\n  
                                    0: Datos de las12Hs \n
                                    1: Datos de un Año\n
                                    2: Datos de un Año y mes\n
                                    3: Datos de un Año,mes y dia\n
                                    4: Datos de un Año,mes,dia y turno\n
            Golpes: Numero maximo de golpes de la maquina 
                    independiente del filtro de tiempo\n
            ahora:Datetime en el que se realizo la consulta sql, 
                    es decir mi fecha actual\n
            filtroTiempo:   Lista con los valores seteados en el filtro de 
                            tiempo por el usuario y tres tuplas de dos 
                            posiciones cada una que contienen los horarios 
                            de inicio y fin de cada turno en formato time
                            (Año,Mes,Dia,Turno, hora de inicio y fin turno 1,
                            hora de inicio y fin turno 2, hora de inicio y 
                            fin turno 3)\n
        """
                                                                                                
        #--------Varaibles globales privadas a utilizar---------
        self.__indicadorConsulta=indicadorConsulta #Indicador de que tipo de consulta sql se realizo, si de 12hs, año, etc
        self.__datos=datosEstado
        self.__coloresIndicadores=("#FFFFFF","#FFF700","#36FF00","#FF0000","#FF6800") #coloresIndicadores(no se sabe(blanco),velocidad lenta(amarrillo), velocidadad normal(verde), detenida(rojo), fuera de rango(naranja))
        self.__meses={1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
        self.__ahora=ahora
        self.__filtroTiempo=filtroTiempo #Filtro de tiempo seteado por el usuario (año,mes,dia,turno)

        #----------Variables y listas de calculo de datos-----------
        self.__velocidad=[] #Lista que contendra las velocidad de cada pieza
        self.__cont=[] #Variable para guardar las velocidades acumulativas
        self.__coord=[] #Lista de coord x para graficar barra de estado
        self.__color=[] #Lista de colores de cada pieza en funcion de su velocidad

        #--------Configuraciones Iniciales---------
        self.__procesamientosIniciales()

    def __procesamientosIniciales(self):
        #-------------------------------------------------------------
        #Nota: El calculo de velocidad funciona sin el estado, si se llega a incluir la variable estado tengo que reconsiderar el calculo de la velocidad
        #-------------------------------------------------------------

        """ Metodo interno a la clase que ordena los datos por fecha, calcula las velociades de cada pieza y asigna los respectivos colores a cada velocidad"""


        #----Calculo de velocidades de comparacion en base a Piezas Hora----
        self.__datos['vel_normal']=(3600/self.__datos[piezasHs])
        self.__datos['vel_lenta']=self.__datos['vel_normal']+(self.__datos['vel_normal']*0.10)  #Tolerancia del 10%
        self.__datos['vel_fueraRango']=self.__datos['vel_normal']+(self.__datos['vel_normal']*0.20)  #Tolerancia del 10%
        
        #-----Calculo velocidades y colores-------
        self.__datos['vel']=self.__datos[fecha].diff().dt.total_seconds() #Resultado en timedelta pasados a segundos puedo usarlo para la barra de estado
        self.__datos.loc[0,'vel']=0
        
        #----Condiciones para determinar la velocidad----
        condiciones = [
        (self.__datos['vel'] >= self.__datos['vel_normal']) & (self.__datos['vel'] < self.__datos['vel_lenta']), #Vel lenta 
        (self.__datos['vel'] >=self.__datos['vel_lenta']) & (self.__datos['vel'] < self.__datos['vel_fueraRango']), #Vel Fuera de rango
        (self.__datos['vel'] < self.__datos['vel_normal']), #Vel normal
        (self.__datos['vel'] >= self.__datos['vel_fueraRango'])] #Parada
        colores = ['yellow', 'orange', 'green','red'] #Colores de velocidad para las condiciones

        #**************************************************************************
        #****Procesamiento de datos de velocidad y sus respectivos colores****
        self.__datos['color'] = np.select(condiciones, colores, default='white') #Asigno color a cada velociadad
        
        #----Genero mascaras----
        mask1=self.__datos['color'].eq(self.__datos['color'].shift(periods=1)) #Creo un df dezplado una poscion adelante y comparo
        mask2=self.__datos['color'].eq(self.__datos['color'].shift(periods=-1)) #Creo un df dezplado una poscion atras y comparo
        self.__datos['mask']=mask1&mask2 #mascara resultante para diesmar datos repetidos en intervalos

        #----Aplico mascara y separo datos----
        dfAux=pd.DataFrame(self.__datos[self.__datos['mask']==False]) #Dataframe auxiliar con los datos diezmados
        dfAux['velAux']=dfAux[fecha].diff().dt.total_seconds() #Velocidades Auxiliares para cada segmento de color
        dfAux.loc[0,'velAux']=0

        #----Extraigo datos en lista numpy----
        cont_1=len(self.__datos[self.__datos['color']=='green']) #Nro de piezas ok
        cont_2=len(self.__datos[self.__datos['color']=='yellow']) #Nro de piezas lentas
        cont_3=len(self.__datos[self.__datos['color']=='orange']) #Nro de piezas muy lentas
        cont_3=len(self.__datos[self.__datos['color']=='red']) #Nro de piezas muy lentas
        #print('Cont1',cont3)
        self.__cont=[cont_1,cont_2,cont_3] #Nro de piezas
        self.__velocidad=dfAux['velAux'].to_numpy() #Lista de velocidades
        self.__color=dfAux['color'].to_numpy() #Lista de colores de cada pieza   

    def datosProcesadosEstadoMaquina(self): #Indicador me va indicar si el perido es de 12 hs, año, año y mes, etc
        """ Metodo que genera las divisiones de tiempo en la barra de estado y devuelve los datos para graficar dicha barra"""
        #---------------------------Variables Locales-------------------------------
        vTiempo=[]
        tam=len(self.__datos)
        ejes=None #Nombres de los ejes x e y

        #-------------------------Calculo del vector tiempo------------------------------
        delta,inicio=self.__filtroDelta()
        for i in range(0,5): #Calculo las divisiones de tiempo de la barra de estado de la maquina
            t=inicio+(delta*i)
            if self.__indicadorConsulta==0: #Consulta de 12 hs
                t=str(time(t.hour,t.minute,t.second))
                ejes=('Ultimas 12 Hs Registradas','Estado')

            elif self.__indicadorConsulta==1: #Consulta año
                t=self.__meses[int(t.month)]
                ejes=('Meses','Estado')

            elif self.__indicadorConsulta==2: #Consulta año y mes
                t=str(t.day)+" de "+self.__meses[int(t.month)]
                ejes=('Dias','Estado')

            elif self.__indicadorConsulta==3: #Consulta año, mes y dia
                t=str(time(t.hour,t.minute,t.second))
                ejes=('Hs','Estado')

            elif self.__indicadorConsulta==4: #Consulta año, mes, dia y turno
                t=str(time(t.hour,t.minute,t.second))
                ejes=('Hs x Turno','Estado')

            #t=str(t.year)+"-"+str(t.month)+"-"+str(t.day)+"\n"+str(time(t.hour,t.minute,t.second))    
            vTiempo.append(t)
        else:
            ejes=('N/A','Estado')                 
        #---------------Retorno de valores----------------------
        return (self.__velocidad,self.__color,self.__coloresIndicadores,vTiempo,ejes) #Modificar para enviar el vector de self.__velocidades para dimensionar bien la barra

    def datosProcesadosGolpesVsTiempo(self): #Grafico de piezas vs tiempo y ver cartel de alerta
        """ Metodo para calcular el nro de piezas vs tiempo(hs/turno/dias/mes/año) """
        #---------Variables locales para armar los vectores x e y del grafico x e y-------------
        x=[] #Eje Tiempo
        y=[] #Eje Piezas
        Vdiv=[]
        maximo=0
        divisiones=0
        tam=len(self.__datos)
        datosAgrupados=0
        ejes=None #Tupla para contener a los nombres de los ejes
        self.__datos['ContAux']=1 #Genero una columna auxilar unitaria para contar la cantidad de datos segun mes dias turnos u horas
        #------------------Filtro de piezas por mes si selecciono un año-------------------------------
        if self.__indicadorConsulta==1 and tam!=0:
            datosAgrupados= self.__datos.groupby(pd.Grouper(key=fecha, freq='M')).sum()
            datosAgrupados.reset_index(inplace=True) #reindexo  
            datosAgrupados['Mes'] = datosAgrupados[fecha].dt.strftime('%B') #Creo columna solo con el mes para los graficos
            x=x+datosAgrupados['Mes'].tolist()
            ejes=['Meses','Nro de piezas']

        #---------------Filtro de piezas por dia si escogo mes y año------------------------------
        elif self.__indicadorConsulta==2 and tam!=0:
            datosAgrupados=self.__datos.groupby(pd.Grouper(key='Fecha', freq='D')).sum()
            datosAgrupados.reset_index(inplace=True) #reindexo  
            datosAgrupados['Dia'] = datosAgrupados['Fecha'].dt.strftime('%d') #Creo columna solo con el dia para el grafico
            x=x+datosAgrupados['Dia'].tolist()
            ejes=['Días','Nro de piezas']

        #----------------Filtro de piezas por turno u hora? si escogo dia mes y año---------------
        elif self.__indicadorConsulta==3 and tam!=0:
            datosAgrupados=self.__datos.groupby(pd.Grouper(key=fecha, freq='H')).sum()
            datosAgrupados.reset_index(inplace=True) #reindexo  
            datosAgrupados['Hora'] = datosAgrupados[fecha].dt.strftime('%H:%M') #Creo columna solo con la hora
            x=x+datosAgrupados['Hora'].tolist()
            ejes=['Hs','Nro de piezas']

        #----------------Filtro por hora si escojo dia mes año y turno y tambien valido para filtrado de ultimas 12hs--------------------------
        elif (self.__indicadorConsulta==4 or self.__indicadorConsulta==0) and tam!=0:
            datosAgrupados=self.__datos.groupby(pd.Grouper(key=fecha, freq='H')).sum()
            datosAgrupados.reset_index(inplace=True) #reindexo  
            datosAgrupados['Hora'] = datosAgrupados[fecha].dt.strftime('%H:%M') #Creo columna solo con la hora
            x=x+datosAgrupados['Hora'].tolist()
            ejes=['Hs','Nro de piezas']

        else:
            pass
        #----------------Calculo de las divisiones paralelas al eje x, y paso los valores de datosAgrupados a la lista x e y para graficar
        if tam==0: #Si no hay datos
            #Poner cartel que no se detectaron datos en la bbdd en el tiempo que se realizo la consulta
            #Datos de grafica poner cero
            ejes=['N/A','Nro de piezas']
        else:  
            y=y+datosAgrupados['ContAux'].tolist() #Lista de piezas
            maximo=max(y)
            divisiones=math.ceil(maximo/5) #Numero de envases entre cada division, tomo el maximo numero de piezas por hr/mes/año etc
            Vdiv=[divisiones,divisiones*2,divisiones*3,divisiones*4,divisiones*5] #Vector de divisiones paralelas al eje x

        #------ Retorno de valores----------------
        return(x,y,Vdiv,ejes)

    def datosProcesadosGraficoVelAcumulativas(self):
        """ Metodo que devuelve la cantidad de piezas en segun velocidad de fabricacion
            Retorno:
                self.__cont[0]: Nro de piezas en velocidad normal\n
                self.__cont[1]: Nro de piezas en velocidad lenta\n
                self.__cont[2]: Nro piezas fuera de rango de velocidad o que no se pudo calcular su velocidad\n """
                
        #------------Retorno de Variable-------------------------
        return(str(self.__cont[0]),str(self.__cont[1]),str(self.__cont[2]))
    
    def __filtroDelta(self):
        """ Metodo que calcula el delta de tiempo para la barra de estado y agrega los tiempos muertos al principio y final de la lista de self.__velocidades para que se vaya midiendo correctamente """
        #----Varaible Locales------
        tam=len(self.__datos)
        delta=None
        inicio=None
        ht1=self.__filtroTiempo[4] #Tupla de dos elementos tipo time como los horarios de incio y fin del turno 1
        ht2=self.__filtroTiempo[5] #Tupla de dos elementos tipo time como los horarios de incio y fin del turno 1
        ht3=self.__filtroTiempo[6] #Tupla de dos elementos tipo time como los horarios de incio y fin del turno 1
        
        #----Fecha y Hora actual-----
        yearActual=self.__ahora.year
        monthActual=self.__ahora.month
        dayActual=self.__ahora.day
        horaActual=time(self.__ahora.hour,self.__ahora.minute,self.__ahora.second)

        #-----Fecha Seteada en el filtro de tiempo-----
        if self.__indicadorConsulta==4: #Apenas inicia el programa no utilizo esta parte
            #----------------Configuro un time con el inicio del turno seteado en el filtro de tiempo--------------
            if int(self.__filtroTiempo[3])==1:
                inicioTurno=ht1[0]
                finTurno=ht1[1]
            elif int(self.__filtroTiempo[3])==2:
                inicioTurno=ht2[0]
                finTurno=ht2[1]
            elif int(self.__filtroTiempo[3])==3:
                inicioTurno=ht3[0]
                finTurno=ht3[1]
            else:
                inicioTurno=None
        #----------------Configuro un time con el inicio del turno en el cual se esta trabajando actualmente--------------
        if horaActual<=ht1[1] and horaActual>=ht1[0]: 
            turnoActual=1
        elif horaActual<=ht2[1] and horaActual>=ht2[0]:
            turnoActual=2
        elif horaActual<=ht3[1] and horaActual>=ht3[0]:
            turnoActual=3
        else:
            turnoActual=None
        if(self.__filtroTiempo[1]!='Mes'):
            mes=list(self.__meses.keys())[list(self.__meses.values()).index(self.__filtroTiempo[1])] #Convierto el mes a su numero correspondiente en base al diccionario del constructor

        #------------Calculo del delta de tiempo para la barra de estado mas el inicio y fin en tiempo de la barra de estado
        if self.__indicadorConsulta==0: #Ultimas 12 hs
            delta=timedelta(hours=12)/4
            inicio=self.__ahora-(delta*4)
            
        elif self.__indicadorConsulta==1: #Año
            inicio=datetime(int(self.__filtroTiempo[0]),1,1,0,0,0)
            if inicio.year<yearActual:
                delta=(datetime(int(inicio.year),12,31)-inicio)/4 #Delta de un año completo divido 4, no uso timedelta por si llega a ser año bisiesto
            else:
                delta=(self.__ahora-inicio)/4 #Delta del presente actual menos principio del año actual dividido 4
            
        elif self.__indicadorConsulta==2: #Año y mes
            inicio=datetime(int(self.__filtroTiempo[0]),mes,1,0,0,0)
            if inicio.month==monthActual and inicio.year==yearActual:
                delta=(self.__ahora- inicio)/4 #Delta de tiempo entre incio de mes y mi tiempo actual
            else:
                NroDias=self.__diasMes(date(inicio.year,inicio.month,1)).day #Calculo los nros de dias del mes
                delta=timedelta(days=NroDias)/4
            
        elif self.__indicadorConsulta==3: #Año, mes y dia
            inicio=datetime(int(self.__filtroTiempo[0]),mes,int(self.__filtroTiempo[2]),0,0,0)
            
            if inicio.day==dayActual and inicio.month==monthActual and inicio.year==yearActual:
                inicio=datetime(int(self.__filtroTiempo[0]),mes,int(self.__filtroTiempo[2]),0,0,0)
                delta=(self.__ahora-inicio)/4  
            else:
                delta=timedelta(hours=24)/4
            
        elif self.__indicadorConsulta==4: #Año, mes, dia y turno
            inicio=datetime(int(self.__filtroTiempo[0]),mes,int(self.__filtroTiempo[2]))
            if inicio.day==dayActual and inicio.month==monthActual and inicio.year==yearActual and int(self.__filtroTiempo[3])==turnoActual:
                inicio=datetime(int(self.__filtroTiempo[0]),mes,int(self.__filtroTiempo[2]),inicioTurno.hour,inicioTurno.minute,inicioTurno.second)
                delta=(self.__ahora-inicio)/4
            else:
                inicio=datetime(int(self.__filtroTiempo[0]),mes,int(self.__filtroTiempo[2]),inicioTurno.hour,inicioTurno.minute,inicioTurno.second)
                if int(self.__filtroTiempo[3])==3: #Si el turno consultado es el 3 significa que termine el dia siguiente por lo cual tengo q sumar un 1 en el campo dia del datetime siguiente
                    fin=datetime(int(self.__filtroTiempo[0]),mes,int(self.__filtroTiempo[2]),finTurno.hour,finTurno.minute,finTurno.second)+timedelta(days=1)
                else:#Si no la resta se realiza dentro del mismo dia
                    fin=datetime(int(self.__filtroTiempo[0]),mes,int(self.__filtroTiempo[2]),finTurno.hour,finTurno.minute,finTurno.second)
                delta=(fin-inicio)/4 #Siempre es un delta fijo porque el horario de los turnos son fijos

        fin=inicio+(delta*4)
        
        #-----------Agrego Tiempos Faltantes para completar la ventana temporar seteada----------------
        if tam==0: #Si no hay datos en el tiempo que se realizo la consulta sql
            self.__velocidad.append((fin-inicio).total_seconds())
            self.__color.append(self.__coloresIndicadores[3])

        else:
            ultimoDato=datetime(self.__datos.loc[tam-1,fecha].year,self.__datos.loc[tam-1,fecha].month,self.__datos.loc[tam-1,fecha].day,self.__datos.loc[tam-1,fecha].hour,self.__datos.loc[tam-1,fecha].minute,self.__datos.loc[tam-1,fecha].second,self.__datos.loc[tam-1,fecha].microsecond)
            primerDato=datetime(self.__datos.loc[0,fecha].year,self.__datos.loc[0,fecha].month,self.__datos.loc[0,fecha].day,self.__datos.loc[0,fecha].hour,self.__datos.loc[0,fecha].minute,self.__datos.loc[0,fecha].second,self.__datos.loc[0,fecha].microsecond)
            self.__velocidad=np.insert(self.__velocidad,0,(primerDato-inicio).total_seconds())
            self.__velocidad=np.insert(self.__velocidad,len(self.__velocidad),(fin-ultimoDato).total_seconds())
            self.__color=np.insert(self.__color,0,self.__coloresIndicadores[3])
            self.__color=np.insert(self.__color,len(self.__color),self.__coloresIndicadores[3])
            
        return delta,inicio

    def __diasMes(self,any_day):
        """ Metodo que calculo la cantidad de dias del mes y año seleccionado """
        next_month=any_day.replace(day=28)+timedelta(days=4)
        return next_month-timedelta(days=next_month.day)

class ProcesamientosDatosAvisos():
    """ El proposito de esta clase es procesar los datos de la consulta sql de los avisos importantes """
    def __init__(self,datos) -> None:
        self.__datos=datos
    
    def prosesamientosIniciales(self):
        """ Metodo para simplificar la programacion, obtengo los datos filtrados y los pongo en varaibles para retornar
            Argumentos:
                any
            Retorno:
                s1:Sims con corte de luz\n
                s2:Sims con max temperatura\n
                s3:Sims con max cantidad de piezas\n
                s4:Sims con aberturas en sus cajas de scrap\n
                s5:Sims con violaciones en sus cajas de seguridad 
        """
        s1=self.__prosesamientosAvisoSeleccionado(corteLuz) #Maquinas que no tienen electricidad
        s2=self.__prosesamientosAvisoSeleccionado(maxTemp)  #Maquinas que superaron su temperatura permitida
        s3=self.__prosesamientosAvisoSeleccionado(maxPiezas) #Cajas de scrap que estan llenas
        s4=self.__prosesamientosAvisoSeleccionado(abertura) #Cajas de scrap que estan siendo abiertas legitimamente
        s5=self.__prosesamientosAvisoSeleccionado(violacionCaja) #Violacion a la seguridad de las cajas de scrap
        return (s1,s2,s3,s4,s5)

    def __prosesamientosAvisoSeleccionado(self,columna):
        """ Metodo que filtra sims de maquina en funcion de una columna booleana de dataframe determinada 
            que se pasa como argumento a esta funcion\n
            Argumentos:\n
                columna(string): Nombre de la columna que se desea filtrar\n
            Retorno:\n
                sims: variable string que contiene las sims del filtrado de la columna ingresada"""
        dfFiltrado=self.__datos[self.__datos[columna]==True] #Aplico filtro
        if(len(dfFiltrado)==0):
            return False
        sims=dfFiltrado[nroMaquina].to_numpy() #Extraigo en un array sims filtradas
        arraySims=self.__vectorString(sims)
        return arraySims
    
    def __vectorString(self,array):
        """ Metodo para convertir array numpy a string y ponerlo en una etiqueta de texto
            Argumentos:
                array: Vector numpy
            Retorno:
                sims: String ordenado para poner en una Qlabel 
        """
        #--Variables--
        sims=''
        
        if(isinstance(array,bool)==True): #Si array es un booleano entra en el if
            return False

        for i in array:
            sims=sims+'*'+str(i)+'\n'
        return sims 

    def cargarDatos(self,datos):
        """ Metodo para cargar datos de dataframe 
            Parametros:
                datos: Dataframe de datos de avisos importantes"""
        self.__datos=datos

