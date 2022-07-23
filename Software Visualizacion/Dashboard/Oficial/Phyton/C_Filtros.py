#----Mis Clases----
from M_ProcesamientoDatos import ProcesamientosDatos, SeparacionDatos
from M_consultaSql import *

#----Clases de Tiempo----
from datetime import timedelta,date,time

#----Clase PyQt5----
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *

class FiltroTiempo(QObject):
    """ Esta clase implementa las funcionalidades del menu de tiempo(año,mes,dia,turno) para seleccionar el periodo de consulta a la bbdd que se desea conocer"""
    actualizar= pyqtSignal(tuple,tuple,int,tuple,int) #genero señal para eliminar pestañas repetidas
    elimnarPest= pyqtSignal(list) #genero señal para eliminar pestañas repetidas
    msgAviso= pyqtSignal(str,str) #Genro señal para dar un aviso al usuario

    def __init__(self,componentes,miConsulta,candado,fs) -> None:
        """ El constructor recibe la referencia a una tupla de los elementos de la QComboBox(year,month,day,turno) para seleccionar el perido de tiempo, los QPushButton de consulta y reiniciar(botonSql2 y boton Sql1) la consulta sql,
        una tupla(direcWidgets) que contiene las referencias a los contenedores donde se van a encapsular las distintas graficas de datos, el objeto con los metodos para hacer las consultas sql(miConsulta) el cual esta compartido con el hilo que ejecuta
        la consulta automatica, el color de fondo de los contenedores de los graficos para que las graficas tengan el mismo color de fondo, ademas de que se inicializan todas las variables y objetos que se van a utilizar y referencia al objeto que maneja
        la configuracion grafica de los labels del nro de golpes,piezas y nro de maquina\n
        \nArgumentos:
            componentes:Tupla que contiene los QComboBox year,month,day,turno y lo QPushButton botonSql1 y botonSql2\n
            miConsulta: OBJETO que contiene las consultas sql y el conector a la bbdd, el objeto "miConsulta" esta compartido con el hilo que ejecuta la consulta automatica\n
            candado: candado para gestion con respecto a los hilos\n
            fs: Filtro sim\n """
        super(FiltroTiempo,self).__init__(parent=None)
        #--------------Constantes a utilizar----------------------
        self.__turno1=(time(5,0,1),time(13,30,0))  #Hora de inicio y fin del turno 1
        self.__turno2=(time(13,30,1),time(22,0,0)) #Hora de inicio y fin del turno 2
        self.__turno3=(time(22,0,1),time(5,0,0)) #Hora de inicio y fin del turno 3

        #----------Variables declaradas como privadas solo accecibles por la clase-----------
        self.__year=componentes[0]
        self.__month=componentes[1]
        self.__day=componentes[2]
        self.__turno=componentes[3]
        self.__botonSql1=componentes[4]
        self.__botonSql2=componentes[5]
        self.__miConsulta=miConsulta #Clase que contiene los metodos para las consultas sql
        self.__estado1=True #Bandera que indica si la progrmacion de botonSql1 y botonSql 2 se puede o no ejecutar, esta bandera la modifica el hilo de la consulta automatica 
        self.estado2=False #Bandera manejado por los botones consulta y reiniciar para habilitar la programacion del hilo de consultaAutomatica
        self.indicadorConsulta=0 #Cero por defecto porque el programa comienza consultando las ultimas 12 hs
        self.__candado=candado #Candado compartido por la el hilo de consulta automatica
        self.__turnoNum=None #Vector que va a contener a los turnos en forma numerica
        
        #----Varaibles para el turno 3----
        self.__ahoraT3=None #Datetime que contiene el inicio del turno 3 en la fecha consultada y que su años mes y dia es valido para los tres turnos
        self.__futuroT3=None #Datetime que contiene el final del turno 3 en la fecha consultada

        #---------------------------------
        self.__FS=fs #Clase del filtro sim
        self.__FM=None #Clase de filtro molde
        self.sim=None #Lista de sims consultadas
        
        #La variable miDic es para adaptar los meses a su numeracion correspondiente para que sea aceptado por el argumento de entrada de las funciones que arman y ejecutan las consultas sql y para calcular los dias del mes
        self.__miDic={"Enero":"01","Febrero":"02","Marzo":"03","Abril":"04","Mayo":"05","Junio":"06","Julio":"07","Agosto":"08","Septiembre":"09","Octubre":"10","Noviembre":"11","Diciembre":"12"}

        #Obtengo los indices de posicion inicial de year month day y turno para poder hacer resetearlos a la configuracion por defecto cuando presiones sobre el boton reiniciar
        self.__indexs=[self.__year.currentIndex(),self.__month.currentIndex(),self.__day.currentIndex(),self.__turno.currentIndex()]
 
    def seleccionYear(self):
        """ Metodo que gestiona el evento del QListWidget year cuando se presiona sobre alguna opcion de este, no devuelve nada """

        if self.__year.currentText()=="Año":
            #Desabilito los QList de mes dia y turno en caso de que no haya seleccionado un año
            self.__month.setEnabled(False)
            self.__day.setEnabled(False)
            self.__turno.setEnabled(False)
        else:
            #Si seleccione un año habilito el QList de mes y recalcula la cantidad de dias del mes si cambio el año
            self.__agregarMeses()
            if self.__month.currentText()!="Mes": 
                self.__agregarDias() #En caso de que cambie el año ya teniendo un mes seleccionado vuelvo a calcular la cantidad de dias de ese mes pero en año distinto
                self.__agregarTurnos()
            self.__month.setEnabled(True)

    def seleccionMonth(self):
        """ Metodo que gestiona el evento del QListWidget month cuando se presiona sobre alguna opcion de este, no devuelve nada  """
        if self.__month.currentText()=="Mes":
            #Deshabilito los QList de dia y turno si no seleccione un mes 
            self.__day.setEnabled(False)
            self.__turno.setEnabled(False)
        else:
            #Activo la QList de dia y calculo los dia del mes y año que seleccione
            self.__agregarDias() #En caso de que cambie el mes vuelve a calcular la cantidad de dias del nuevo mes seleccionado
            if self.__day.currentText()!="Día": 
                self.__agregarTurnos()
            self.__day.setEnabled(True)

    def seleccionDay(self):
        """ Metodo que gestiona el evento del QListWidget day cuando se presiona sobre alguna opcion de este, no devuelve nada  """
        if self.__day.currentText()=="Día":
            self.__turno.setEnabled(False)
        else:
            self.__agregarTurnos()
            self.__turno.setEnabled(True)
            
    def seleccionTurno(self): 
        """ Metodo que gestiona el evento del combobox turno cuando se presiona sobre alguna opcion de este """     
        #----Determino el turno----
        if self.__turno.currentIndex()==0:
            self.__turnoNum=None
        elif self.__turno.currentIndex()==1:
            self.__turnoNum='1'
            self.__calculoTiempoTurnos(self.__turno1,True)
        elif self.__turno.currentIndex()==2:
            self.__turnoNum='2'
            self.__calculoTiempoTurnos(self.__turno2,True)
        elif self.__turno.currentIndex()==3:
            self.__turnoNum='3'
            self.__calculoTiempoTurnos(self.__turno3,False)

    def botonSql1(self):
        """ Metodo que gestiona el evento de botonSql1 "Consultar" cuando se presiona sobre este, el mismo selecciona la 
        consulta sql en base a las opciones elegidas en las QListWidgets de año,mes,dia y turno, no devuelve nada  """
        if self.__estado1==True:
            self.__estado1=False #Para que no vuelva a entrar en el boton
            self.estado2=False #Cuando termine la programacion de boton 1 el candado se desbloquea, para que el hilo automatico no ejecute su programcion uso esta bandera en caso de que el candado este liberado
            self.__candado.acquire()

            #----Variables internas-----
            datosMaquinas=[] #Variable para contener a sim juntos con las velocidades normales y lentas(vlns) y los golpes de la maquina: [sim,vlns,CGolpes]
            banderaSimMolde,sim=self.condicionesConsulta() #Determino si esta todo en condiciones para hacer una consulta o no
            #----Consultas----- 
            if banderaSimMolde==True:
                if self.__year.currentIndex()==self.__indexs[0]: #Si el indice de mes es igual al indice de la poscion inicial entonces consulto el año
                    (datos,CGolpes,ahora)=self.__miConsulta.consulta12Hs(sim) #De las ultimas 12 hs
                    self.indicadorConsulta=0
                    # self.estado2=True #Para que el hilo de consulta automatica pueda seguir
                elif self.__month.currentIndex()==self.__indexs[1]: #Si el indice de mes es igual al indice de la poscion inicial entonces consulto el año
                    (datos,CGolpes,ahora)=self.__miConsulta.consultaA(self.__year.currentText(),sim)#Consulta SQL del año seleccionado y especifico numero de serie de la maquina
                    self.indicadorConsulta=1
                    # self.estado2=False #Para que el hilo de consulta automatica no pueda seguir
                elif self.__day.currentIndex()==self.__indexs[2]: #Lo mismo que el elif anterior pero con day
                    (datos,CGolpes,ahora)=self.__miConsulta.consultaAM(self.__year.currentText(),self.__miDic[self.__month.currentText()],sim)#Consulta SQL del año y mes seleccionados y especifico numero de serie de la maquina
                    self.indicadorConsulta=2
                    # self.estado2=False #Para que el hilo de consulta automatica no pueda seguir
                elif self.__turno.currentIndex()==self.__indexs[3]: #Lo mismo que el elif anterior pero con turno
                    (datos,CGolpes,ahora)=self.__miConsulta.consultaAMD(self.__year.currentText(),self.__miDic[self.__month.currentText()],self.__day.currentText(),sim)#Consulta SQL del año,mes y dia seleccionados y especifico numero de serie de la maquina
                    self.indicadorConsulta=3
                    # self.estado2=False #Para que el hilo de consulta automatica no pueda seguir
                else: 
                    (datos,CGolpes,ahora)=self.__miConsulta.consultaAMDT(self.__ahoraT3,self.__futuroT3,self.__turnoNum,sim)#Consulta SQL del año,mes,dia seleccionados y especifico numero de serie de la maquina
                    self.indicadorConsulta=4

                for i in range(0,len(sim)):
                    datosMaquinas.append((sim[i],CGolpes[i]))
                self.actualizacionGraficos(datos,datosMaquinas,ahora)
   
            self.__estado1=True
            if self.indicadorConsulta==0:
                self.estado2=True #Para que el hilo de consulta automatica pueda seguir
            self.__candado.release()

    def botonSql2(self):
        """ Metodo que gestiona el evento de botonSql2 "Reiniciar" cuando se presiona sobre este, el mismo vuelve a poner una configuracion
        por defecto en los QListWidget "year" "month" "day" y "turno" y manda a ejecutar una consulta sql de las ultima 12 hs de la maquina ademas de devolver el control de las consutlas sql al hilo que ejecuta las consutals automaticas """
        if self.__estado1==True:
            self.__estado1=False #Para que no vuelva a entrar en el boton
            self.__candado.acquire() #Bloqueo para quen o hagan otra consulta a la bbdd el hilo o el boton de consulta
            #------------Seteo los QComboBox a sus posiones originales es decir a los elementos que dicen "Año","Mes","Día" y "Turno"-------------
            self.__year.setCurrentIndex(self.__indexs[0])
            self.__month.setCurrentIndex(self.__indexs[1])
            self.__day.setCurrentIndex(self.__indexs[2])
            self.__turno.setCurrentIndex(self.__indexs[3])
            
            #-------------Inhabilito los QComboBox de month day y turno------------
            self.__month.setEnabled(False)
            self.__day.setEnabled(False)
            self.__turno.setEnabled(False)
            
            #------------Consulto las ultimas 12 hs de la maquina-------------
            #----Variables internas-----
            datosMaquinas=[] #Variable para contener a sim juntos con las velocidades normales y lentas(vlns) y los golpes de la maquina: [sim,vlns,CGolpes]
            banderaSimMolde,sim=self.condicionesConsulta() #Determino si esta todo en condiciones para hacer una consulta o no
            #---------------------------------------------------------------------------------------
            #Nota: Falta Cartel que no se selecciona ningun sim ni molde
            #--------------------------------------------------------------------------------------- 
            if banderaSimMolde==True:
                (datos,CGolpes,ahora)=self.__miConsulta.consulta12Hs(sim) #De las ultimas 12 hs
                self.indicadorConsulta=0
                for i in range(0,len(sim)):
                    datosMaquinas.append((sim[i],CGolpes[i]))
                self.actualizacionGraficos(datos,datosMaquinas,ahora)  #Aca esta el problema
                self.estado2=True #Para que el hilo de consulta automatica pueda seguir
            else:
                self.estado2=False #Para que el hilo de consulta automatica no pueda seguir
                #Cartel de que hay algo que no esta bien
            self.__estado1=True #Habilito boton 1 y 2 de consulta y reiniciar
            self.__candado.release() #Libero candado

    def __diasMes(self,any_day):
        """ Metodo que calculo la cantidad de dias del mes y año seleccionado """
        next_month=any_day.replace(day=28)+timedelta(days=4)
        return next_month-timedelta(days=next_month.day)

    def __agregarDias(self):
        """ Este metodo agrega los dias del mes y año seleccionado al QListWidgets "day" """
        mes=int(self.__miDic[self.__month.currentText()])
        year=int(self.__year.currentText())
        fecha=datetime.now()
        NroDias=self.__diasMes(date(year,mes,1)).day #Calculo los nros de dias del mes                       
        self.__day.clear() #Borro el QComboBox de day
        self.__day.addItem("Día")
        if fecha.year==year and fecha.month==mes:
            for i in range(1,fecha.day+1): #Le sumo 1 a NrodeDias porque range excluye el limite superior
                self.__day.addItem(str(i)) #Agrego todos los items a la lista
        else:
            for i in range(1,NroDias+1): #Le sumo 1 a NrodeDias porque range excluye el limite superior
                self.__day.addItem(str(i)) #Agrego todos los items a la lista
        self.seleccionDay()

    def __agregarMeses(self):
        """ Metodo para agregar cantidad de meses segun si estoy en el presente o años anteriores """
        fecha=datetime.now()
        self.__month.clear() #Borro lista de meses
        self.__month.addItem("Mes")
        meses=list(self.__miDic.keys()) #Extraigo claves del diccionario
        if int(self.__year.currentText())==fecha.year: #Si el año seteado es igual al año actual
            for i in range(0,fecha.month):
                self.__month.addItem(meses[i])
        
        else:
            for i in range(0,12):
                self.__month.addItem(meses[i])

    def __agregarTurnos(self):
        """ Este metodo agrega los turnos correspondientes si estan dentro de la zona horaria en caso de que consulte el mismo dia """
        fecha=datetime.now()
        self.__turno.clear() #Borro lista de meses
        self.__turno.addItem("Turno")
        meses=int(self.__miDic[self.__month.currentText()]) #Extraigo el mes seteado en su valor numerico
        horaActual=time(fecha.hour,fecha.minute,fecha.second)
        #-------Determino el turno actual en el cual estoy parado-----------
        if horaActual<=self.__turno1[1] and horaActual>=self.__turno1[0]: 
            turnoActual=1
        elif horaActual<=self.__turno2[1] and horaActual>=self.__turno2[0]:
            turnoActual=2
        elif horaActual<=self.__turno3[1] and horaActual>=self.__turno3[0]:
            turnoActual=3
        else:
            turnoActual=None
        #------Lleno la lista de de turnos segun la cantidad de turno deseados
        if int(self.__year.currentText())==fecha.year and meses==fecha.month and int(self.__day.currentText())==fecha.day: #Si el año seteado es igual al año actual
            self.__agregarItemsTurno(turnoActual)
        else:
            self.__agregarItemsTurno(3)
    
    def __agregarItemsTurno(self,tope):
        """ Metodo interno de la clase que determina cuantos turnos agregar """
        for i in range(1,tope+1):
                if i==1 :
                    self.__turno.addItem("Mañana")
                elif i==2:
                    self.__turno.addItem("Tarde")
                elif i==3:
                    self.__turno.addItem("Noche")

    def actualizacionGraficos(self,datos,datosMaquinas,ahora):
        """ Este metodo manda a procesar los datos para ser graficados
            \nArgumentos: 
                datos: tupla que contiene la informacion de los datos consultados a la tabla sql
                datosMaquinas: tupla de datos de la maquina(sim,Golpes)
                ahora: Fecha y hora de cuando presiono el boton consultar"""
        #----Varibles----
        filtroTiempo=(self.__year.currentText(),self.__month.currentText(),self.__day.currentText(),self.__turnoNum,self.__turno1,self.__turno2,self.__turno3) #Armo tupla con el filtro de tiempo seteado
        
        #----------Separo y ordeno Datos del dataframe en varios dataframe de acuerdo a su sim--------------
        Separar=SeparacionDatos()
        df,sim,Golpes,banderaDatos=Separar.separacionDatos(datos,datosMaquinas)
        #----------Proceso Todos los Dataframe por Separado------------------
        for i in range(0,len(sim)):
            DatosProcesados=ProcesamientosDatos(df[i],self.indicadorConsulta,Golpes[i],ahora,filtroTiempo)#Clase perteneciente al modelo que maneja el procesamiento de datos, apenas instancio la clase ya calcula algunas datos
            #-----------------Extraigo los datos procesados-------------------
            datosEstados=DatosProcesados.datosProcesadosEstadoMaquina()
            datosPiezasVsTiempo=DatosProcesados.datosProcesadosGolpesVsTiempo()
            datosPiezasVel=DatosProcesados.datosProcesadosGraficoVelAcumulativas()
            self.actualizar.emit(datosEstados,datosPiezasVsTiempo,sim[i],datosPiezasVel,int(Golpes[i]))
        
        if banderaDatos==False: #Si tengo maquinas sin datos emito mensaje
            self.msgAviso.emit('Aviso','No se econtraron datos de algunas maquinas') 
        self.elimnarPest.emit(sim) #Señal que activa el metodo eliminaPestana en la clase Ventana en V_ventana.py que elimnar las pestañas que no se consultaron
        #----------------------------------------------------------------------------------------------------------------------------

    def bloquearBotones(self,bandera):
        """ Metodo usado por el hilo de consulta automatica para desabilitar los botones mientras se conecta a la bbdd y luego con este mismo metodo los vuelve a habilitar, no devuelve nada  
            \nArgumentos: 
                bandera: indica si habilita o no los botones(True habilita, False deshabilita)"""
        self.__botonSql1.setEnabled(bandera)
        self.__botonSql2.setEnabled(bandera)
    
    def condicionesConsulta(self):
        """ Metodo que obtiene las sims y comprueba que esten en orden para hacer la consulta sql\n
            Retorno:\n
                bandera: Inidicador para que hay aunque sea una maquina seleccionada para hacer la consulta sql\n
                sim:lista de sim a consultar\n """
        #----Variables----
        bandera=False #Variable para indicar si cada sim le corresponde un molde o no         
        sim,indicesVacios1,n=self.__FS.consultarVectorSims() #Obtengo los sims seleccionados
        self.sim=sim #Guardo las sim en una variable global aunque creo que no la uso
        
        #-----------------Determino si tengo misma cantidad de moldes y sim y en las misma posiciones para hacer una consulta---------------
        if len(indicesVacios1)!=n: #Misma cantidad seleccionado
            bandera=True

        else:
            bandera=False
            self.msgAviso.emit('Aviso','No ha seleccionado ninguna sim')

        return bandera,sim

    def __calculoTiempoTurnos(self,turno,bandera):
        """ Metodo que calcula los datetime de inicio y fin de los tres turnos 
            Argumentos:
                turno: Tupla de dos elementos tipo time que indican el inicio y fin del turno escogido para consultar\n
                bandera: Sirve para el calculo de delta de tiempo True para el turno 1 y 2 y False para el turno 3\n """
        #Nota: En deltaT3 uso el año 2021 el dia 1 de enero porq al final lo que calculo es un delta asi que no afecta, lo importante es tener en claro si turno que se consulta es en el mismo dia o en dos dias distintos
        self.__ahoraT3=datetime(int(self.__year.currentText()),int(self.__miDic[self.__month.currentText()]),int(self.__day.currentText()),turno[0].hour,turno[0].minute,turno[0].second) #Inicio del turno 3 en la fecha consultada
        if bandera==True: # Si el turno es el 1 o 2 el delta se calcula para un mismo dia
            deltaT3=datetime(2021,1,1,turno[1].hour,turno[1].minute,turno[1].second)-datetime(2021,1,1,turno[0].hour,turno[0].minute,turno[0].second) #Saco Delta de tiempo de lo que dura el turno 1 o 2
        else: # Si el turno es el 3 el delta se calcula para dos dias distintos
            deltaT3=datetime(2021,1,2,turno[1].hour,turno[1].minute,turno[1].second)-datetime(2021,1,1,turno[0].hour,turno[0].minute,turno[0].second) #Saco Delta de tiempo de lo que dura el turno 3
        self.__futuroT3=self.__ahoraT3+deltaT3 # Final del turno escogido

class FiltroSims():
    """ Clase para la creacion y manejo de las checkbox que contendran los nro de maquinas"""
    def __init__(self,labels,n) -> None:
        """ Implementa internas de la clase
            Parametros:
                labels: Etiquetas de texto donde se muestran los sims seleccionados\n
                n: Nro maximo de maquinas permitidas para seleccionar\n """
        #-------Variables--------
        self.__labels=labels
        self.__box=None #Contendra los widgets de los check de sims o moldes
        self.__contador=0 #Contador para determinar cuantos check estan activos
        self.__vector=[None,None,None,None,None] #Contiene los check seleccionados
        self.__n=n #Numero maximo de sims para poder seleccionar

    def estadoCheck(self,estado):
        """ Metodo que se ejecuta con la señal de una checkBox
            Parametros: 
                estado: Emitido por la señal, me indica si esta check o no"""
        if estado==Qt.Checked: #El check esta marcado
            self.__contador=self.__contador+1
            if self.__contador==self.__n: #Inhabilito el resto de checkbox
                self.__desactivarCheck()
            self.agregarElemento()
        elif estado==Qt.Unchecked: #El check no esta marcado
            self.__contador=self.__contador-1
            if self.__contador==(self.__n-1): #Habilito el resto de checkbox
                self.__activarCheck()
            self.quitarElemento()
    
    def guardarCheckBoxSims(self,lista):
        """ Metodo para guardar todas las check box en uan variable interna del filtro 
            Parametros:
                lista: lista de las check box totales de sims"""
        self.__box=lista
    
    def __activarCheck(self):
        """ Metodo interno para habilitar los check cuando hay seleccionados menos de cinco"""
        for i in self.__box:
            if i.isEnabled()==False:
                i.setEnabled(True)

    def __desactivarCheck(self):
        """ Metodo interno para deshabilitar los check que no se usan cuando se tiene n(5 en este caso) seleccionados"""
        for i in self.__box:
            if i.isChecked()==False:
                i.setEnabled(False)
    
    def agregarElemento(self):
        """ Metodo que se llama cuando se tilda un checkbox y modifica el vector que contiene los datos a consultar en sql """
        for i in range(0,len(self.__box)):
            valor=self.__box[i].text()
            if self.__box[i].isChecked()==True: #Casilla tildada
                if (valor in self.__vector):
                    pass
                else: #Si la casilla esta tildada pero su valor no esta en el vector
                    for j in range(0,len(self.__vector)):
                        if self.__vector[j]==None:
                            self.estilizar(j,valor)
                            self.__vector[j]=valor #Guardo valor en el primer none que encuentro
                            return

    def quitarElemento(self):
        """ Metodo que se llama cuando se destilda un checkbox y modifica el vector que contiene los datos a consultar en sql """
        for i in range(0,len(self.__box)):
            valor=self.__box[i].text()
            if (valor in self.__vector) and self.__box[i].isChecked()==False: #Valor repetido
                self.estilizar(self.__vector.index(valor),'N/A')
                self.__vector[self.__vector.index(valor)]=None #self.__vector.index(valor) --> Indice
                return
            else:
                pass
    
    def estilizar(self,i,texto):
        """ Metodo para estilizar las etiquetas de texto
            Parametros: 
                i: Posicion de la etiqueta\n
                texto: Texto del labels """
        self.__labels[i].setText(texto)
        self.__labels[i].setStyleSheet( 'font-size:12pt;\n' 
                                        'color:#55ffff;\n'
                                        'font: bold;')

    def consultarVectorSims(self):
        """ Metodo que devuelve el vector en limpio(sin none) con los datos para armar la consulta sql\n 
            Retorno:\n
                sim: Lista Sim\n
                indicesVacios: Indices de las posiciones vacias de la lista sim\n
                n: Nro maximo de sims selecionables\n"""
        sim=[]
        indicesVacios=[]
        for i in range(0,len(self.__vector)):
            if self.__vector[i]!=None:
                sim.append(self.__vector[i])
            else: #Determino los indices vacios para igualar con los indices del filtro de sim
                indicesVacios.append(i)
        return sim,indicesVacios,self.__n
