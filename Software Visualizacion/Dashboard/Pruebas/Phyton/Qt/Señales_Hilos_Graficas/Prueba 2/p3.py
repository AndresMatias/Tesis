import sys
import time

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
   
from matplotlib.backends.backend_qt5agg import FigureCanvas

import matplotlib.pyplot as plt

import pyodbc
import pandas as pd
import numpy as np
import time

#-------Clase Graficadora-------------
class Grafico(QWidget):
    
    def __init__(self, colorW, parent):
        """ En el constructor se ejecutan configuraciones iniciales para que el dibujo se cree y amolde al tamaño del widget
            \nArgumentos:
                colorW: color de fondo de grafico
                parent: widget en donde se desea implementar el grafico """
        QWidget.__init__(self, parent)
        self.__colorW=colorW
        self.__fig1=plt.Figure(facecolor=self.__colorW) #Figura contendra mi dibujo xy
        self.xy=self.__fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi xy
        self.canvas = FigureCanvas(self.__fig1) #Usando plt.figure pq esta devuelve un Objeto tipo Figure()
        vertical_layout = QVBoxLayout() #Layout 
        vertical_layout.addWidget(self.canvas) #Agrego mi lienzo al layout
        parent.setLayout(vertical_layout)#Agrego el layout al widget
        self.xy.axis("off") #Desactivo Ejes
    
    def ploteo(self,x1,y1,x2,y2):
        self.xy.clear()
        self.xy.plot(x1,y1) #Recta uno
        self.xy.plot(x2,y2)       #Recta dos
        self.xy.plot([7,12],[1,6])       #Recta tres
        self.__fig1.canvas.draw()   #Actualizar dibujo

#-------Clase Graficadora2-------------
class Grafico(QWidget):
    
    def __init__(self, colorW, parent):
        """ En el constructor se ejecutan configuraciones iniciales para que el dibujo se cree y amolde al tamaño del widget
            \nArgumentos:
                colorW: color de fondo de grafico
                parent: widget en donde se desea implementar el grafico """
        QWidget.__init__(self, parent)
        self.__colorW=colorW
        self.__fig1=plt.Figure(facecolor=self.__colorW) #Figura contendra mi dibujo xy
        self.xy=self.__fig1.add_subplot(111) # Variable que contiene los ejes para graficar mi xy
        self.canvas = FigureCanvas(self.__fig1) #Usando plt.figure pq esta devuelve un Objeto tipo Figure()
        vertical_layout = QVBoxLayout() #Layout 
        vertical_layout.addWidget(self.canvas) #Agrego mi lienzo al layout
        parent.setLayout(vertical_layout)#Agrego el layout al widget
        self.xy.axis("off") #Desactivo Ejes
    
    def ploteo(self,vecV,vecC):
        self.xy.clear()
        #---Datos Diezmados----
        posX=0
        for i in range(0,len(vecC)):
            self.xy.barh('2021',vecV[i],color=vecC[i],left=posX)
            posX=posX+vecV[i] #Determina la poscion en el eje x para graficar la siguiente barra
        self.__fig1.canvas.draw()   #Actualizar dibujo	

#-------------Hilo Qt----------------
class HiloQ(QThread):
    sig = pyqtSignal(str)
    
    def __init__(self,Grafica,parent=None):
        super(HiloQ, self).__init__(parent)
        self.Grafica=Grafica
    
    def run(self):
        self.conexionSql() #Fuera del metodo run no funciona como hilo

    def conexionSql(self):
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
            query='SELECT * FROM Version01 where SIM=5600438 and YEAR(Fecha)=2021'

            #-----Ejecuto consulta SQL a la bbdd mediante pandas-----
            df=pd.read_sql_query(query,con=conexion)

            #-----Ordeno Datos-----
            print('Tamaño del dataframe: ',len(df))
            # start =timer() #Inicio para medir tiempo
            self.separacionDatos(df)
            # end =timer() #Fin para medir tiempo
            # print ('Tiempo de Ejecucion con pandas',end-start)

        except Exception as e:
            # Atrapar error
            print("Ocurrió un error al conectar a SQL Server: ", e)
        finally:
            pass
            #cursor.close()
    
    def separacionDatos(self,df):
        #------Ordeno datos por fechas------
        df=df.sort_values(by="Fecha") #ordeno y reindexo valores, inplace=True para que trabaje sobre el mismo dataframe y drop para que no haga una nueva columna con los antiguos index
        df=df.reset_index() #reindexo
        df.drop(['index'],axis=1,inplace=True) #borro columna index de los indices anteriores y trbajo sobre el mismo dataframe(inplace=True)
        
        #-----Calculo velocidades y colores-------
        df['vel']=df['Fecha'].diff().dt.total_seconds() #Resultado en timedelta pasados a segundos puedo usarlo para la barra de estado
        df.loc[0,'vel']=0

        normal=58
        lento=62
        fueraRango=120
        parado=160

        condiciones = [
        (df['vel'] >= normal) & (df['vel'] < lento), #Vel lenta 
        (df['vel'] >=lento) & (df['vel'] < fueraRango), #Vel Fuera de rango
        (df['vel'] < normal), #Vel normal
        (df['vel'] >= parado)] #Parada

        colores = ['yellow', 'orange', 'green','red']
        df['color'] = np.select(condiciones, colores, default='white')
        #df['cord']=df['vel'].cumsum() #Vector de dezplazamiento

        # velocidad=df['vel'].to_numpy() #Lista de velocidades
        # color=df['color'].to_numpy() #Lista de colores de cada pieza
        # coord=df['cord'].to_numpy()#Coordenadas para graficar barra de estado
        # vel_normal = np.ma.masked_where(float(self.__velocidadNominal) <= self.__datos['vel'], self.__datos['cord'])  
        # vel_lenta = np.ma.masked_where((float(self.__velocidadNominal)>self.__datos['vel'] ) | (float(self.__velocidadLenta)<self.__datos['vel'] ), self.__datos['cord'])
        # vel_fueraRango = np.ma.masked_where((float(self.__velocidadLenta)>= self.__datos['vel']) | (float(self.__fueraRango)<self.__datos['vel'] ), self.__datos['cord'])
        # vel_detenido = np.ma.masked_where((float(self.__fueraRango)>=self.__datos['vel'] ), self.__datos['cord'])


        #----Genero mascaras----
        mask1=df['color'].eq(df['color'].shift(periods=1)) #Creo un df dezplado una poscion adelante y comparo
        mask2=df['color'].eq(df['color'].shift(periods=-1)) #Creo un df dezplado una poscion atras y comparo
        df['mask']=mask1&mask2 #mascara resultante para diesmar datos repetidos en intervalos


        #----Aplico mascara y separo datos----
        dfAux=pd.DataFrame(df[df['mask']==False]) #Dataframe auxiliar con los datos diezmados
        dfAux['velAux']=dfAux['Fecha'].diff().dt.total_seconds() #Velocidades Auxiliares para cada segmento de color
        dfAux.loc[0,'velAux']=0

        vecC=dfAux['color'].to_numpy() #Extraigo vector de colores en numpy(numpy es mas rapido de procesar)
        vecV=dfAux['velAux'].to_numpy()

        print("Tamaño del dataframe diesmado: ",len(dfAux))
        self.Grafica.ploteo(vecV,vecC)



class Ventana(QMainWindow):
    #Método constructor de la clase
    sig2=pyqtSignal()
    def __init__(self):
        self.i=0
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ventana.ui", self) #Esto sale del programa de diseño de interfaz y no lo tengo
        # self.graficar=Grafico('red',self.grafico)
        # self.graficar.ploteo([1,2,3,4],[1,2,1,2],[10,11,12,13,14],[5,6,7,6,5])
        self.MiGrafica=Grafico('red',self.grafico)
        #-----------HiloQ---------------
        self.thread2 = HiloQ(self.MiGrafica)
        self.sig2.connect(self.thread2.conexionSql) #Conecto Señal
        
        self.pushButton.clicked.connect(self.buttonClicked2)          
    
    def buttonClicked2(self):
        self.thread2.start()
        # for i in range(0,10):
        #     time.sleep(1)
        #     print(i)
        #self.sig2.emit()

    


#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()