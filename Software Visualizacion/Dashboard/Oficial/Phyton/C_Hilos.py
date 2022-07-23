import imp
import threading
from datetime import datetime,timedelta
import time
import matplotlib.pyplot as plt
from PyQt5.QtCore import * #pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#-----Mis Clases-----
from C_GraficoBarrasH import GraficoBarras
from Constantes import *
from C_Gestion import *

class ConsultaAutomatica(threading.Thread):
    """ Esta clase implementa una consulta automatica de sql cada cierto tiempo seteado en el metodo run, mas especificamente con el for y time.sleep() """
    def __init__(self,nombre_hilo,miLista,candado,miConsulta):
        threading.Thread.__init__(self,name=nombre_hilo,target=ConsultaAutomatica.run)# Herencia, cuando ejecuta este hilo, ejecuta el metodo run de esta clase
        #--------Inicializar varaibles, todas son compartidas con el hilo principal por eso utilizo un candado(Lock) para sincronismo--------
        self.__candado=candado #Variable para asegurar que este hilo ejecute la consulta automatica y solo este hilo
        self.__miConsulta=miConsulta #Clase que contiene las consultas sql
        self.__miLista=miLista #Filtro de Tiempo
        self.__cierreHilo=False

    def run(self):
        """ Metodo que ejecuta la programacion del hilo de la consultaAutomatica, basicamente este metodo realiza una consulta sql sobre las ultimas 12Hs de la maquina cada cierto tiempo que se establece
        de acuerdo al for y time.sleep en este metodo, y bajo ciertas condiciones que son basicamente que no se cierre la ventana principal
        y que no se esten consultando datos en una fecha determinada desde el panel de seleccion de fechas """

        while self.__cierreHilo==False:
            #-----------Minuto a minuto se ejecuta la consulta automatica---------------
            ahora=datetime.now()
            mm=ahora.minute
            mmAux=(ahora+timedelta(minutes=1)).minute
            while mm!=mmAux and self.__cierreHilo==False:
                mm=datetime.now().minute
                time.sleep(0.01)
            #--------------Ejecucion de la consulta automatica-----------------
            if self.__miLista.estado2==True and self.__cierreHilo==False:
                self.__candado.acquire() #Pongo candando para que el unicamente este hilo ejecute esta funcion        
                self.__consultaAutomatica() #Consulta automatica de las ultimas 12 hs
                self.__candado.release() #Libero candado       
        self.__miConsulta.cerrarConexion()# Cierro conexion sql

    def __consultaAutomatica(self):
        """ Este metodo contiene la programacion para ejecutar una consulta sql cada 30 segundos de los ultimos datos agregaos a la tabla, 
        se recomienda consultar las ultimas 12 hs de la maquina una sola vez """
        banderaSimMolde,sim=self.__miLista.condicionesConsulta()
        datosMaquinas=[] #Variable para contener a sim juntos con las velocidades normales y lentas(vlns) y los golpes de la maquina: [sim,vlns,CGolpes]
        if banderaSimMolde==True:
            datos,CGolpes,ahora=self.__miConsulta.consulta12Hs(sim)
            self.__miLista.indicadorConsulta=0
            for i in range(0,len(sim)):
                    datosMaquinas.append((sim[i],CGolpes[i]))
            self.__miLista.actualizacionGraficos(datos,datosMaquinas,ahora)
        else:
            pass
            #Introducir cartel de error o algo asi

    def cierreHilo(self,cierreHilo):
        """ Metodo para indicarle al hilo mediante una bandera que debe finalizar su ejecucion 
            Argumentos:
                cierreHilo: Bandera True o False cerrar el hilo(True para cerrar, False para mantener funcionando)"""
        self.__cierreHilo=cierreHilo

class ConsultaAutomatica2(QThread):
    """ Esta clase implementa una consulta automatica de sql cada cierto tiempo seteado en el metodo run, para verificar los avisos importantes"""
    actualizarInfoAvisos= pyqtSignal(str,int,bool)
    cerrarPest= pyqtSignal(int) #Cierro la ventana de dialogo 
    def __init__(self,candado,miConsulta,miProceso,parent=None):
        super(ConsultaAutomatica2, self).__init__(parent)
        #--------Inicializar varaibles, algunas son compartidas con el hilo principal por eso utilizo un candado(Lock) para sincronismo--------
        self.__candado=candado #Variable para asegurar que este hilo ejecute la consulta automatica y solo este hilo
        self.__miConsulta=miConsulta #Clase que contiene las consultas sql
        self.__cierreHilo=False
        self.__MiProcesamiento=miProceso
        parent.cierreHilo.connect(self.cierreHilo)

    def run(self):
        """ Metodo que ejecuta la programacion del hilo de la consultaAutomatica, basicamente este metodo realiza una consulta sql sobre las ultimas 12Hs de la maquina cada cierto tiempo que se establece
        de acuerdo al for y time.sleep en este metodo, y bajo ciertas condiciones que son basicamente que no se cierre la ventana principal
        y que no se esten consultando datos en una fecha determinada desde el panel de seleccion de fechas """

        while self.__cierreHilo==False:
            #-----------Tiempo Minimo de Ejecucion---------------
            time.sleep(5) #5 Segundos
            #--------------Ejecucion de la consulta automatica-----------------
            if self.__cierreHilo==False:
                self.__candado.acquire() #Pongo candando para que el unicamente este hilo ejecute esta funcion        
                self.__consultaAutomatica() #Consulta automatica de las ultimas 12 hs
                self.__candado.release() #Libero candado

    def __consultaAutomatica(self):
        """ Este metodo contiene la programacion para ejecutar una consulta sql cada pocos segundos para revisar los avisos importantes """
        datos=self.__miConsulta.consultaAvisos()
        self.__MiProcesamiento.cargarDatos(datos)
        s=self.__MiProcesamiento.prosesamientosIniciales()
        bandera=False #Utilizo la bandera para indicar a ventana que cambie el color de la pestaña en caso de que haya avisos
        for i in range(0,len(s)):
            if(isinstance(s[i],str)==True):
                bandera=True
                self.actualizarInfoAvisos.emit(s[i],i,bandera)
            else:
                self.actualizarInfoAvisos.emit('N/A',i,bandera)

    def cierreHilo(self,cierreHilo):
        """ Metodo para indicarle al hilo mediante una bandera que debe finalizar su ejecucion 
            Argumentos:
                cierreHilo: Bandera True o False cerrar el hilo(True para cerrar, False para mantener funcionando)"""
        self.__cierreHilo=cierreHilo
        self.terminate() #Termino el Hilo
        

class CirculoProgreso(QThread):
    """ Hilo para generar la animacion del circuilo de progreso """
    #----Señales----
    actualizarProgreso = pyqtSignal(int) #genero señal
    cerrarVentana= pyqtSignal() #genero señal
    cerrarAnimacion= pyqtSignal() #genero señal

    def __init__(self,ventanaCarga) -> None:
        super(CirculoProgreso,self).__init__(parent=None)
        #--------Inicializar varaibles----------------
        self.ventanaCarga=ventanaCarga
        self.__cierreHilo=None

    # def __init__(self,progreso):
        
    def run(self):
        """ Metodo que mueve la animacion """
        time.sleep(0.01)
        while self.__cierreHilo==None: #Ampliar condiciones de conexion en caso de que falle
            #print(self.banderaConexion)
            for i in range(0,120):
                self.actualizarProgreso.emit(i)
                time.sleep(0.001)
                
        if self.__cierreHilo==True:
            #print("Hilo:",self.__cierreHilo)
            #self.cerrarAnimacion.emit()
            self.cerrarVentana.emit()
            pass
            #poner circulo en verde
        
        if self.__cierreHilo==False:
            self.cerrarAnimacion.emit()
            #self.cerrarVentana.emit()
            pass
            #Para poner error en el circuilo de caga
        

    def cierreHilo(self,bandera):
        """ Metodo para terminar el hilo """
        self.__cierreHilo=bandera

class GraficoEstado(QThread):
    """ Esta clase implementa un hilo para graficar la barra de estado"""
    #----Señales----
    cierreHilo= pyqtSignal() #genero señal
    def __init__(self,padre,VentanaPrincipal) -> None:
        """ Parametros:
            padre:Widget que va a contener la grafia
            VentanaPrincipal: Referencia a la ventanaPrincipal para enlazar señales """
        super(GraficoEstado,self).__init__(parent=None)
        #--------Inicializar varaibles----------------
        self.__MiEstado=GraficoBarras(grisNegro,padre)
        self.__estados=None #Informacion para Graficar
        self.__cierreHilo=True #Bandera para indicar cierre de hilo
        self.__actualizarGrafico=False #Bandera para indicar si actualizo o no el grafico

        #----Enlazo Señales----
        VentanaPrincipal.cierreHilo.connect(self.cierreHilo) #Señal para cerrar todos los hilos que cree

    def run(self):
        """ Metodo grafica el estado """
        while self.__cierreHilo!=False: #Ampliar condiciones de conexion en caso de que falle
            time.sleep(1) #Tiempo de espera de 1 segundo
            if self.__actualizarGrafico!=False:
                self.__MiEstado.ploteo(self.__estados[0],self.__estados[1],self.__estados[2],self.__estados[3],self.__estados[4])
                self.__actualizarGrafico=False
    
    def cierreHilo(self,bandera):
        """ Metodo para terminar el hilo
            Parametros:
                bandera: boleeano true(seguir) o false(cerrar hilo) para terminar el hilo """
        self.__cierreHilo=bandera

    def actualizarGrafico(self,estados):
        """ Metodo para actualizar grafico de barra temporal en una pestaña existente\n
            Parametros:\n
                estados: Informacion para graficar la barra de estados, dicha informacion la provee la clase de procesamiento de datos\n """
        self.__estados=estados #Guardo informacion para graficar
        self.__actualizarGrafico=True #Habilito al hilo para graficar

