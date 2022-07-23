import sys
import time

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

    
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pyodbc
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
        
        #-----Calculo velocidades y colores-------
        df['vel']=df['Fecha'].diff().dt.total_seconds() #Resultado en timedelta pasados a segundos puedo usarlo para la barra de estado
        df.loc[0,'vel']=0

        #Nota: talvez pueda en las constate poner df['vel_hr']
        # normal=3600
        # lento=3700
        # fueraRango=3800
        # parado=4000

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

        #----Genero mascaras
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
        # print("Tamaño del dataframe diesmado 2: ",len(vecC))

        #---Datos Diezmados
        posX=0
        for i in range(0,len(vecC)):
            plt.barh('2021',vecV[i],color=vecC[i],left=posX)
            posX=posX+vecV[i] #Determina la poscion en el eje x para graficar la siguiente barra
        #plt.show()

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

class Graficar(QThread):
    sig = pyqtSignal(str)
    
    def __init__(self,colorW,padre,parent=None):
        super(Graficar, self).__init__(parent)
        print('hola')
        self.graficar=Grafico(colorW,padre)
    
    def run(self):  
        #self.conexionSql()
        self.sig.emit('Grafico Terminado')
    
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
            separacionDatos(df)
            # end =timer() #Fin para medir tiempo
            # print ('Tiempo de Ejecucion con pandas',end-start)

        except Exception as e:
            # Atrapar error
            print("Ocurrió un error al conectar a SQL Server: ", e)
        finally:
            pass
            #cursor.close()


class Ventana(QMainWindow):
    #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("ventana.ui", self) #Esto sale del programa de diseño de interfaz y no lo tengo
    
    def buttonClicked2(self):
        self.thread2.start()
    
    def updateLabel(self, text):
        self.label.setText(text)

    


#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()