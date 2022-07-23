#Constantes
from turtle import delay
from Constantes import *
#-----Mis Clases de Modelo------
from M_consultaSql import *

#-----Mis Clases de Controlador------
from C_Filtros import *
from C_GraficoXY import *
#from C_GraficoBarrasH import *
from C_Gestion import *
from C_Hilos import ConsultaAutomatica,GraficoEstado,ConsultaAutomatica2
from V_Ventanas_Auxiliares import *

#-----Clase de Hilos------
from threading import Lock

#-----Clases PyQt5-----
from PyQt5 import uic,QtCore
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

#----Para poder Importar ui por pyinstaller
from recursos import *

class Ventana(QMainWindow):
    """La clase ventana implementa la ventana principal del programa y la configuracion grafica contenida en el archivo .ui
    realizada a travez de Qt Designer y las clases que dan funcionalidad al interfaz todo esto siguendo el modelo MVC(Modelo Vista Controlador) 
    , los archivos.py que comiencen con M_ pertenecen a grupo de modelo, los C_ al grupo controlador y V_ a vista"""
    #----Señales----
    cierreHilo=pyqtSignal(bool) #Señal para cerrar todos los hilos de grafica

    def __init__(self):
        """ Configuraciones iniciales """
        #Iniciar el objeto QMainWindow(Ventana)
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui(que contiene toda la interfaz hecha en Qt Designer) en el objeto
        # Forma 1 de Carga UI
        # uic.loadUi("V_Interfaz_3_v2.ui",self)
        
        # Forma 2 de Carga UI
        # ventana_path = resource_path("V_Interfaz_3_v2.ui")
        # uic.loadUi(ventana_path, self)

        # Forma 3 de Carga UI
        fileh = QtCore.QFile('V_Interfaz_3_v2.ui')
        fileh.open(QtCore.QFile.ReadOnly)
        uic.loadUi(fileh, self)
        fileh.close()

        #----Configuraciones Previas Ventana----
        self.setWindowTitle("Sistema de Monitoreo Industrial Alladio") #Texto
        # self.setWindowFlags(Qt.Window | Qt.WindowSystemMenuHint | Qt.CustomizeWindowHint)#Quito Los marcos de la Vetana
        # self.showFullScreen() #Pantalla Completa
        # self.setGeometry(0,0,1366,768)
        self.showMaximized() #maximizo
        self.menubar.setVisible(False) #Escondo barra de tareas
        #---------Variables----------------
        self.coloresWidgets=('#787878','#282828','#464646') #gris oscuro,casi negro, intermedio entre los otros
        self.coleresLabels=('#ffffff','','#55ffff') #blanco, ,azul resaltado
        self.__pest=[] #Lista para de pestañas de maquinas
        
        #-----Pestaña Estado y Avisos-----
        self.Avisos=InterfazAvisos(self.tabs)
        self.estado=InterfazEstados(self.tabs)
        self.tabs.addTab(self.estado,'Estados')
        self.tabs.addTab(self.Avisos,'Avisos Importantes')

        #----Configuraciones Iniciales Basicas-------
        self.nroGolpes.setVisible(False)
        self.l_8.setVisible(False)

        #---------Variables para los filtros----------------
        self.__filtroTiempo=(self.year,self.month,self.day,self.turno,self.botonSql1,self.botonSql2) #Widgets donde escojo la fecha a consultar y los botones de consutlar y reiniciar
        self.__labelsFiltrosSims=(self.mm_1,self.mm_2,self.mm_3,self.mm_4,self.mm_5) #Labels de texto para indicar las maquinas escogidas
        self.__boxS=[] #Va a contener la direccion de los widgets de checkbox de sims
        self.__candado=Lock() #Actualmente no utilizo este candado para sincronizar hilos pero lo dejo aca por si llego a poner mas hilos y nececito sincronizar
        self.llenarYear()

        #------Variables para Scroll Area de los checkBox de las Maquinas
        self.__cont1=QWidget() #Widget contenedor de sims
        self.__lv1=QVBoxLayout() 

        # ---------Instancio mis Clases para el manejo inicial del programa-----------------
        self.__Mi_Consulta=EjecutaConsulta()
        Inicio=GestionInicio(self.__Mi_Consulta,self.servidor,self.servidor_2)
        Inicio.construccionFiltros.connect(self.construirFiltros) #Conecto señal-slot para construir filtros

        #----------Instancio mis clases para el manejo del menu----------
        #MiGestionMenu=GestionMenu(Inicio) #Reciclo clase de inicio para la conexion sql en el menu
        #Nota debo poner a la escucha el menu y probarlo pero de momento no lo hago
        
        #---------Ejecuto metodos para conexion sql y construccion de filtros---------
        Inicio.conexionSql(True)
        Inicio.cargaSim()

        #-----------Enlazo señales-slots de Filtro de Tiempo---------------
        self.year.activated.connect(self.__MiFiltroTiempo.seleccionYear)
        self.month.activated.connect(self.__MiFiltroTiempo.seleccionMonth)
        self.day.activated.connect(self.__MiFiltroTiempo.seleccionDay)
        self.turno.activated.connect(self.__MiFiltroTiempo.seleccionTurno) #No uso esta señal ni su metodo pero esta comentado mas abajo por si algun llega a usarse para que ya este listo
        self.botonSql1.clicked.connect(self.__MiFiltroTiempo.botonSql1)
        self.botonSql2.clicked.connect(self.__MiFiltroTiempo.botonSql2)

        #----Instancio mi hilo de consulta automatica----
        #self.__MiGestionAvisos=GestionAvisos(self)
        self.__MiProceso=ProcesamientosDatosAvisos(None)
        self.__Hilo_1=ConsultaAutomatica('Consulta_Automatica',self.__MiFiltroTiempo,self.__candado, self.__Mi_Consulta)
        self.__Hilo_1.start()
        self.__Hilo_2=ConsultaAutomatica2(self.__candado, self.__Mi_Consulta,self.__MiProceso,self)
        self.__Hilo_2.actualizarInfoAvisos.connect(self.actualizoAvisos)
        #self.__Hilo_2.cerrarPest.connect(self.__MiGestionAvisos.signalCerrarPosponer)
        self.__Hilo_2.start()    
        
    def construirFiltros(self,sims,n):
        """ Metodo que construye los filtros para seleccion de maquina y sim 
            Paramtros:
                sims: lista de sims\n
                moldes: lista de moldes\n
                n: nro maximo de sims a consultar"""
        #-------Contruyo los filtros en base a los datos de sims y moldes de las tablas de las bbdd-----
        self.__MiFiltroSim=FiltroSims(self.__labelsFiltrosSims,n)
        self.__MiFiltroTiempo=FiltroTiempo(self.__filtroTiempo, self.__Mi_Consulta,self.__candado,self.__MiFiltroSim)
        
        #--------------Configuraciones Graficas-------------------
        self.__cont1.setLayout(self.__lv1)
        self.scMa.setWidget(self.__cont1) #widget de scroll de maquina le seteo el widget que contiene los check box
        self.agregarSims(sims)

        #--------------Enlazo señales-slots de pestañas y avisos---------------------
        self.tabs.currentChanged.connect(self.cambioPestana)
        self.__MiFiltroTiempo.actualizar.connect(self.actualizar)
        self.__MiFiltroTiempo.elimnarPest.connect(self.eliminarPestana)
        self.__MiFiltroTiempo.msgAviso.connect(self.ventanaAviso)

    def agregarSims(self,sims):
        """ Metodo para agregar sims al scroll area y conectar con los slot de la clase que gestiona su funcionamiento """
        sim=sims['SIM'].tolist() #Paso el dataframe a una lista
        for i in range(0,len(sim)):
            box=QCheckBox(str(sim[i]))
            box.stateChanged.connect(self.__MiFiltroSim.estadoCheck)
            self.__estilizar(box,'#282828')
            self.__lv1.addWidget(box)
            self.__boxS.append(box)
        self.__MiFiltroSim.guardarCheckBoxSims(self.__boxS)
    
    def __estilizar(self,box,colorFondo):
        box.setStyleSheet(  'font-size:12pt;\n' 
                            'color:#ffffff;\n'
                            'background:'+colorFondo+';\n'
                            'font: bold;')

    def llenarYear(self):
        """ Este metodo llena la lista de años desde el año actual hasta 2013, dicho tope se modifica en el while\n
        Argumentos:
            year: Referencia al QComboBox que contiene a la lista de años """
        #-----Inabilito los QComboBox menos el de año-----
        self.month.setEnabled(False)
        self.day.setEnabled(False)
        self.turno.setEnabled(False)
        #-----Lleno la lista de años--------------
        yearActual=datetime.now().year
        y=int(yearActual)
        while(y>2013):
            self.year.addItem(str(y))
            y=y-1
    
    def eliminarPestana(self,sim):
        """ Metodo que detecta las pestañas que no estan en la consutla sql y las elimina
        Parametros:
            sim:Lista sim de la consulta sql  """
        bandera=False
        vecAux=[]
        for i in self.__pest:
            for j in sim:
                if i[0].sim==j:
                    bandera=True
                    break
                else:
                    bandera=False #Sim no esta en la consulta
            vecAux.append(bandera) #Detecto los elementos a eliminar
        
        n=len(vecAux)-1
        for i in range(0,len(vecAux)): #Elimino de atras para adelante
            if  vecAux[n-i]==False:
                self.estado.destruirMaquina(self.__pest[n-i][3]) #Remueve widget de la maquina en la pestaña estado
                self.tabs.removeTab(n-i+pestFijas) #El pestFijas sale de que la pestaña de filtro, estado y Avisos Importantes no estan incluidas en el vecttor self.__pest
                self.__pest.pop((n-i))

    def actualizar(self,estados,piezasVtiempo,sim,datosPiezas,Golpes):
        """ Metodo que actulizar los graficos y labels de las maquinas por separado y crea las pestañas de maquinas que no estan, ademas de crear y modificar los graficos de la pestaña estado\n
            \nParametros:
                estados: Datos de la barra de estados(emitido por la señal que activa el slot)\n
                piezasVtiempo: Datos de piezas vs tiempo en funcion del filtro de tiempo(emitido por la señal que activa el slot)\n
                sim: Maquina a la cual se va actualizar en su pestaña o crear y actulizar la pestaña(emitido por la señal que activa el slot)\n
                datosPiezas: Piezas segun su velocidad(emitido por la señal que activa el slot)\n
                Golpes: Golpes de la maquina(emitido por la señal que activa el slot)\n  """
        bandera=False
        #-----Determino si la pestaña ya esta creada-----
        for i in self.__pest:
            if sim==i[0].sim: #La maquina esta en las pestañas
                bandera=True
                self.actualizarPestana(i,estados,piezasVtiempo,sim,datosPiezas,Golpes) #Actualizo la pestaña
                break
        #-----Agrego pestaña que no estan-----
        if bandera==False: 
            self.crearPestana(estados,piezasVtiempo,sim,datosPiezas,Golpes)

    def crearPestana(self,estados,piezasVtiempo,sim,datosPiezas,Golpes):
        """ Metodo que  crea las pestañas de maquinas que no existen y las barras de estados en la pestaña Estado que tampoco esxisten\n
            Parametros:\n
                estados: Datos de la barra de estados(emitido por la señal que activa el slot)\n
                piezasVtiempo: Datos de piezas vs tiempo en funcion del filtro de tiempo(emitido por la señal que activa el slot)\n
                sim: Maquina a la cual se va actualizar en su pestaña o crear y actulizar la pestaña(emitido por la señal que activa el slot)\n
                datosPiezas: Piezas segun su velocidad(emitido por la señal que activa el slot)\n
                Golpes: Golpes de la maquina(emitido por la señal que activa el slot)\n """
        #----Creo la Pestaña de la Maquina----
        tab=InterfazMaquina(self.tabs,sim,Golpes)
        #miEstado=GraficoBarras(self.coloresWidgets[1],tab.estadoMaquina.contenedorObjeto)
        miEstado=GraficoEstado(tab.estadoMaquina.contenedorObjeto,self) #Hilo
        miEstado.start() #Inicio Hilo
        miXY=GraficoXY(self.coloresWidgets[1],tab.piezasVsTiempo.contenedorObjeto)

        #----Creo el widget que va dentro de la Pestaña Estado----
        maquina=self.estado.crearMaquina()
        #miEstado2=GraficoBarras(self.coloresWidgets[1],maquina.estado)
        miEstado2=GraficoEstado(maquina.estado,self)
        miEstado2.start()
        
        #----Actualizo Pestañas Maquina----
        miXY.ploteo(piezasVtiempo[0],piezasVtiempo[1],piezasVtiempo[2],piezasVtiempo[3])
        #miEstado.ploteo(estados[0],estados[1],estados[2],estados[3],estados[4])
        miEstado.actualizarGrafico(estados)
        tab.piezasNormales.estilizar(tab.piezasNormales.etiqueta,datosPiezas[0],tab.piezasNormales.colorLabel,16,'MS Shell Dlg 2')
        tab.piezasLentas.estilizar(tab.piezasLentas.etiqueta,datosPiezas[1],tab.piezasLentas.colorLabel,16,'MS Shell Dlg 2')
        tab.piezasFueraRango.estilizar(tab.piezasFueraRango.etiqueta,datosPiezas[2],tab.piezasFueraRango.colorLabel,16,'MS Shell Dlg 2')
        
        #----Actualizo Pestaña Estado----
        maquina.modificarValores(sim,datosPiezas[0],datosPiezas[1],datosPiezas[2],Golpes,'#ffffff',16,'MS Shell Dlg 2')
        miEstado2.actualizarGrafico(estados)

        #-----Agrego pestaños de maquinas y las guardo en una lista--------
        self.tabs.addTab(tab,str(sim))
        self.__pest.append((tab,miEstado,miXY,maquina,miEstado2)) 

    def actualizarPestana(self,pest,estados,piezasVtiempo,sim,datosPiezas,Golpes):
        """ Metodo que actulizar los graficos y labels de las maquinas por separado y crea las pestañas de maquinas que no estan, ademas de crear y modificar los graficos de la pestaña estado\n
            Parametros:\n
                pest: Pestaña que se quiere actualizar\n
                estados: Datos de la barra de estados(emitido por la señal que activa el slot)\n
                piezasVtiempo: Datos de piezas vs tiempo en funcion del filtro de tiempo(emitido por la señal que activa el slot)\n
                sim: Maquina a la cual se va actualizar en su pestaña o crear y actulizar la pestaña(emitido por la señal que activa el slot)\n
                datosPiezas: Piezas segun su velocidad(emitido por la señal que activa el slot)\n
                Golpes: Golpes de la maquina(emitido por la señal que activa el slot)\n """

        #----Actualizo Pestañas de Maquinas----
        pest[0].Golpes=Golpes
        pest[1].actualizarGrafico(estados)
        pest[2].ploteo(piezasVtiempo[0],piezasVtiempo[1],piezasVtiempo[2],piezasVtiempo[3])
        pest[0].piezasNormales.estilizar(pest[0].piezasNormales.etiqueta,datosPiezas[0],pest[0].piezasNormales.colorLabel,16,'MS Shell Dlg 2')
        pest[0].piezasLentas.estilizar(pest[0].piezasLentas.etiqueta,datosPiezas[1],pest[0].piezasLentas.colorLabel,16,'MS Shell Dlg 2')
        pest[0].piezasFueraRango.estilizar(pest[0].piezasFueraRango.etiqueta,datosPiezas[2],pest[0].piezasFueraRango.colorLabel,16,'MS Shell Dlg 2')
        
        #----Actualizo Pestaña de Estado----
        pest[3].modificarValores(sim,datosPiezas[0],datosPiezas[1],datosPiezas[2],Golpes,'#ffffff',16,'MS Shell Dlg 2')
        pest[4].actualizarGrafico(estados)

    def cambioPestana(self,inidice):
        """ Metodo que se llama cuando se cambia la pestaña
            Parametros:
                Indice: Lo envia la señal, es el indice de la pestaña a la que se cambio """
        if inidice>(pestFijas-1): #Cambiar el 0 a 2 cuando agregue la pestaña de avisos Importantes
            actual=self.tabs.currentWidget() #Obtengo widget actual
            # print(actual.Golpes)
            self.estilizar(self.nroGolpes,str(actual.Golpes),self.coleresLabels[2],16,'MS Shell Dlg 2')
            self.estilizar(self.nroMaquina,'Inyectora Nro: '+str(actual.sim),self.coleresLabels[0],26,'MS Shell Dlg 2')
            self.l_8.setVisible(True)
            self.nroGolpes.setVisible(True)
        elif inidice<=(pestFijas-1): #Selecciono la pestaña de Filtro
            self.estilizar(self.nroMaquina,'Sistema Industrial de Monitoreo',self.coleresLabels[0],26,'MS Shell Dlg 2')
            self.nroGolpes.setVisible(False)
            self.l_8.setVisible(False)
    
    def estilizar(self,etiqueta,titulo,color,tam,fuente):
        """ Metodo para estilizar y setear texto de un label 
            Parametros:
                etiqueta: QLabel que se desea modificar\n
                tiutlo: Texto a mostrar\n
                color: color del texto(preferentemente en formato html)\n
                tam: Tamaño de letra\n
                fuente: Fuente de texto(ej: Arial)\n"""
        etiqueta.setText(titulo) 
        etiqueta.setStyleSheet( 'font-size:'+str(tam)+'pt;\n' 
                                'color:'+color+';\n'
                                'font: '+fuente+';\n'
                                'qproperty-alignment: AlignCenter;')

    def closeEvent(self,event):
        """ Evento de cierre de ventana si se cierra desde la X """
        respuesta=QMessageBox(QMessageBox.Question,"Cerrar Ventana","Desea Salir del Programa",buttons=QMessageBox.Yes|QMessageBox.No,parent=self)
        respuesta.setDefaultButton(QMessageBox.No) #Respeusta por defecto
        respuesta.setStyleSheet('QMessageBox {\n'
                                        'background-color: #FFFFFF;\n '
                                        'color: white;\n'
                                        '}\n'
                                    'QPushButton:hover{\n'
                                        'color: #2b5b84;\n'
                                        '}\n'
                                    'QLabel{\n' 
                                        'color: black;\n'
                                        'background-color: rgb(255, 255, 255);\n'
                                        '}')
        respuesta.exec_()
        reply=respuesta.standardButton(respuesta.clickedButton())
        if reply==QMessageBox.Yes:
            try:
                self.__Hilo_1.cierreHilo(True)
                self.cierreHilo.emit(True)
                self.__Hilo_1.join() #Espero a que termine el Hilo_1 antes de finalizar el hilo principal
                #self.__Hilo_2.exit() #Espero a que termine el Hilo_2 antes de finalizar el hilo principal
                
            except Exception as err:
                pass
            finally:
                event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event): # Evento de teclado
        """ Metodo para cerrar el programa si se presiona la tecla "Esc" """
        key=event.key()
        if key==Qt.Key_Escape: #Si presiono escape
            respuesta=QMessageBox(QMessageBox.Question,"Cerrar Ventana","Desea Salir del Programa",buttons=QMessageBox.Yes|QMessageBox.No,parent=self)
            respuesta.setDefaultButton(QMessageBox.No) #Respeusta por defecto
            respuesta.setStyleSheet('QMessageBox {\n'
                                        'background-color: #FFFFFF;\n '
                                        'color: white;\n'
                                        '}\n'
                                    'QPushButton:hover{\n'
                                        'color: #2b5b84;\n'
                                        '}\n'
                                    'QLabel{\n' 
                                        'color: black;\n'
                                        'background-color: rgb(255, 255, 255);\n'
                                        '}')
            respuesta.exec_()
            reply=respuesta.standardButton(respuesta.clickedButton())
            if reply==QMessageBox.Yes:
                try:
                    self.__Hilo_1.cierreHilo(True)
                    self.cierreHilo.emit(True)
                    self.__Hilo_1.join() #Espero a que termine el Hilo_1 antes de finalizar el hilo principal
                    #self.__Hilo_2.exit() #Espero a que termine el Hilo_2 antes de finalizar el hilo principal
                except Exception as err:
                    pass
                finally:
                    self.close()    
            else:
                event.ignore()

    def ventanaAviso(self,titulo,mensaje):
        """ Este metodo implementa una ventana de aviso QMessageBox\n
            Parametros:
                titulo: titulo de la ventana\n
                mensaje: mensaje que va a leer el usuario\n """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        msg.setWindowTitle(titulo)
        msg.exec_()
    
    def actualizoAvisos(self,sims,i,bandera):
        """ Metodo llamado por ConsultaAutomatica2 en C_Hilos.py para actualizar la informacion
            de los avisos
            Parametros:
                sims: Lista str con las maquinas para los avisos
                i: posicion del aviso en el array de avisos de InterfazAvisos a actualizar
                bandera: Booleano para indicar si cambio el estilo de la pestaña o no """
        self.Avisos.ArrayAvisos[i].estilizar(self.Avisos.ArrayAvisos[i].etiqueta,sims,azulResaltado,26,'MS Shell Dlg 2')
        if bandera==True:
            self.tabs.setCurrentIndex(2)

       
class InterfazMaquina(QWidget):
    """ Esta clase contruye la interfaz para visualizar informacion de una maquina en una pestaña, la misma puede reutilizarse para varias maquinas"""
    def __init__(self,parent,sim,Golpes) -> None:
        """ Constructor de la clase donde se aloja todo el codigo que contruye y distribuye todos los componentes graficos(widgets y labels principalmente) que van a contener los datos de la maquina
        Parametros:
            parent: widget del cual va a heredar la clase\n
            sim: Nro de serie de la maquina\n
            Golpes: Golpes de la maquina\n """
        super(QWidget, self).__init__(parent)
        #-----Variables--------
        self.lv=QVBoxLayout()
        self.lh=QHBoxLayout()
        self.sim=sim #Nombre sim de la maquina para identificar al widget
        self.Golpes=Golpes

        #-------------Estructuras Estandares---------------------
        self.piezasNormales=EstructuraEstandar(parent,(1,10),grisNegro,azulResaltado,'Nro Piezas Normales',10,'N/A',26)
        self.piezasLentas=EstructuraEstandar(parent,(1,10),grisNegro,azulResaltado,'Nro Piezas lentas',10,'N/A',26)
        self.piezasFueraRango=EstructuraEstandar(parent,(1,10),grisNegro,azulResaltado,'Nro Piezas Fuera de Rango',10,'N/A',26)
        self.estadoMaquina=EstructuraEstandar(parent,(1,10),grisNegro,azulResaltado,'Estado de la maquina',10,None,None)
        self.piezasVsTiempo=EstructuraEstandar(parent,(1,10),grisNegro,azulResaltado,'Piezas vs Tiempo',10,None,None)

        #-----------Agrego componentes a layout horizontal---------------
        self.lh.addWidget(self.piezasNormales)
        self.lh.addWidget(self.piezasLentas)
        self.lh.addWidget(self.piezasFueraRango)

        #-----------Agrego componentes a layout vertical---------------
        self.lv.addLayout(self.lh)
        self.lv.addWidget(self.piezasVsTiempo)
        self.lv.addWidget(self.estadoMaquina)

        #-----------Seteo estiramientos y separacion de margenes en el layout vertical el cual contiene todo----------------
        self.lv.setStretch(0,2) 
        self.lv.setStretch(1,8)
        self.lv.setStretch(2,4)
        self.lv.setContentsMargins(4,4,4,4) #Separacion entre componentes de los margenes creo
        self.setLayout(self.lv)

        #----Hoja de Estilos----
        self.setAttribute(Qt.WA_StyledBackground, True) #Habilito hoja de estilo
        self.setStyleSheet( 'background-color: '+grisIntermedio+';')
    
class EstructuraEstandar(QWidget):
    """ Esta clase implementa una estructura grafica(interfaz grafica) que se repite varias veces por lo cual con esta clase se puede reutilzar el codigo
    , la misma esta compuesta por dos widgets y uno o dos labels, un widget contiene un label para un titulo y el otro puede contener el otro label o un objeto de otro tipo como puede ser un grafico """
    def __init__(self,parent,estirar,colorWidget,colorLabel,titulo,tamTitulo,label,tamLabel) -> None:
        """ Constructor de la clase donde se aloja todo el codigo que contruye y distribuye todos los componentes graficos\n
        Parametros:\n
            parent: widget del cual va a heredar la clase\n
            estirar: tupla de dos elementos int para indicar en que proporcion se van a distribuir los widgets es decir cual va a ocupar mas espacio\n
            colorwidget: color del widget contenedor\n
            coloresLabels: color de la etiqueta del titulo y/o label del segundo 2do widget\n
            titulo: Nombre que va llevar la etiqueta de texto que va indicar que se esta representando\n
            tamTitulo: Tamaño de letra del titulo\n
            label: Texto de la 2da etiqueta, si no se usa poner None de esa forma no se agregara en la interfaz y se podra usar otro objeto\n
            tamLabel: Tamaño del label\n """
        super(QWidget, self).__init__(parent)
        #-----Variables----------
        self.etiqueta=None #Etiqueta para contener a label
        self.colorWidget=colorWidget
        self.colorLabel=colorLabel
        self.estirar=estirar
        self.lv=QVBoxLayout()
        self.setLayout(self.lv)

        #------Widgets------
        self.contenedorTitulo=QWidget()
        self.contenedorObjeto=QWidget()
        self.titulo=QLabel()

        #-----Layouts-----
        self.lvTitulo=QVBoxLayout()
        self.lvObjeto=QVBoxLayout()
        
        #-----------Configuraciones----------------
        self.lv.setContentsMargins(0,0,0,0)
        self.contenedorTitulo.setLayout(self.lvTitulo)
    
        self.lvTitulo.addWidget(self.titulo)
        if label!=None:
            self.etiqueta=QLabel()
            self.contenedorObjeto.setLayout(self.lvObjeto) #Incluyo el layout aca porque sino me jode el layout de la clase de dibujo
            self.lvObjeto.addWidget(self.etiqueta)

        self.lv.addWidget(self.contenedorTitulo)
        self.lv.addWidget(self.contenedorObjeto)
        self.lv.setStretch(self.estirar[0],self.estirar[1]) #Seteo cual se extiende mas

        #-----------Hoja de Estilos----------------
        self.contenedorTitulo.setStyleSheet('background-color: '+colorWidget+';')
        self.contenedorObjeto.setStyleSheet('background-color: '+colorWidget+';')   
        self.estilizar(self.titulo,titulo,colorLabel,tamTitulo,'MS Shell Dlg 2')
        if self.etiqueta!=None:
            self.estilizar(self.etiqueta,label,colorLabel,tamLabel,'MS Shell Dlg 2')

    def estilizar(self,etiqueta,titulo,color,tam,fuente):
        """ Metodo para estilizar y setear texto de un label 
            Parametros:
                etiqueta: QLabel que se desea modificar\n
                tiutlo: Texto a mostrar\n
                color: color del texto(preferentemente en formato html)\n
                tam: Tamaño de letra\n
                fuente: Fuente de texto(ej: Arial)\n"""
        etiqueta.setText(titulo) 
        etiqueta.setStyleSheet( 'font-size:'+str(tam)+'pt;\n' 
                                'color:'+color+';\n'
                                'font: '+fuente+';\n'
                                'qproperty-alignment: AlignCenter;')

class InterfazEstados(QScrollArea):
    """ Esta clase construye la interfaz para visualizar las barras de estado de tiempo de todas las maquinas """
    
    def __init__(self,parent) -> None:
        """ Se crean las barras de estado\n
        Parametros:\n
            parent: Clase padre de la cual hereda esta clase\n """
        super(QWidget, self).__init__(parent)
        #-----Variables---------- 
        self.widget = QWidget()   #Widget Contenedor Principal       
        self.vbox = QVBoxLayout() #Layout del widget contenedor

        #----Configuraciones----
        # self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.widget.setLayout(self.vbox)
        self.setWidget(self.widget)
        self.setStyleSheet( 'background-color: '+grisIntermedio+';')

    def crearMaquina(self):
        """ Metodo que crea una estructura estandar para representar los datos de una maquina en la pestaña estado
        y devuelve esta estrutra en el retorno
            Retorno:
                Objeto del tipo EstrucutraEstantarEstados\n """
        object=EstructuraEstandarEstados(self)
        self.vbox.addWidget(object)
        #---Configuracion Scroll Area----
        self.setWidgetResizable(True)

        return object
    
    def destruirMaquina(self,maquina):
        """ Metodo que remueve las maquinas de la pestaña estado 
            Parametros:
                maquina: Objeto del tipo EstructuraEstandarEstado que se desea remover de la pestaña estado\n"""
        self.vbox.removeWidget(maquina)
        
class EstructuraEstandarEstados(QWidget):
    """ Esta clase implementa la estructura basica que se repite en toda la pestaña de Estados """
    def __init__(self,parent) -> None:
        super().__init__(parent=parent)
        #----layouts------
        self.lh=QHBoxLayout() #Layout principal
        self.setLayout(self.lh)
        #----Fijo alto en 250 pixeles para el widget contenedor
        self.setMinimumHeight(250)
        self.setMaximumHeight(250)

        #----Variables----
        self.nroSim=None #Nro de identificacion de la maquina
        self.nroPiezasBajas=None #Nro de piezas que se fabricaron a una baja velocidad
        self.nroPiezasNormal=None #Nro de piezas que se fabricaron a una velocidad normal
        self.nroPiezasFueraRango=None #Nro de piezas que se fabricaron fuera de rango de velocidad
        
        #----Etiquetas de Texto------
        self.sim=QLabel() 
        self.piezasVelNormal=QLabel()
        self.piezasVelBaja=QLabel()
        self.piezasFueraRango=QLabel()
        self.nroGolpes=QLabel()

        #----Widget para la grafica de estado-----
        self.estado=QWidget()

        #-----Configuraciones-----
            #---Agrego Componentes al layout horizontal---
        self.lh.addWidget(self.sim)
        self.lh.addWidget(self.estado)
        # self.lh.addWidget(self.piezasVelNormal)
        # self.lh.addWidget(self.piezasVelBaja)
        # self.lh.addWidget(self.piezasFueraRango)
        # self.lh.addWidget(self.nroGolpes)
        self.lh.setSpacing(0) #Espacio entre componentes dentro del widget principal

            #---Factor de estiramiento de cada componente---
        self.lh.setStretch(0,1)
        self.lh.setStretch(1,10)
        # self.lh.setStretch(2,1)
        # self.lh.setStretch(3,1)
        # self.lh.setStretch(4,1)
        # self.lh.setStretch(5,1)

            #---Hoja de estilos---
        self.setStyleSheet('background-color: '+grisNegro+';')

    def modificarValores(self,sim,vl,vn,fr,golpes,color,tam,fuente):
        """ Este metodo estiliza los numeros de sim, velocidad normal, velocidad lenta, piezas fuera de rango y golpes de acuerdo al color tamaño y fuente que se ingresen
            Parametros:
                sim: Nro de serie de la maquina\n
                vl: Nro de piezas fabricadas a velocidad lenta\n
                vn: Nro de piezas fabricadas a velocidad normal\n
                fr: Nro de piezas fabricadas fuera del rango de velocidad\n
                golpes: Nro de golpes de la maquina
                color: Color que se desea que tengas los textos en los labels
                tam: Tamaño de letra deseado
                fuente: Fuente de la letra Ej: Arial(Ingresar en formato string) """
        self.estilizar(self.sim,'SIM\n'+str(sim),color,tam,fuente)
        # self.estilizar(self.piezasVelNormal,'Velocidad Normal\n'+str(vn),color,tam,fuente)
        # self.estilizar(self.piezasVelBaja,'Velocidad Lenta\n'+str(vl),color,tam,fuente)
        # self.estilizar(self.piezasFueraRango,'Fuera de Rango\n'+str(fr),color,tam,fuente)
        # self.estilizar(self.nroGolpes,'Nro Golpes\n'+str(golpes),color,tam,fuente)
        self.sim.adjustSize() 
        # self.piezasVelNormal.adjustSize() 
        # self.piezasVelBaja.adjustSize() 
        # self.piezasFueraRango.adjustSize() 
        # self.nroGolpes.adjustSize() 

    def estilizar(self,etiqueta,titulo,color,tam,fuente):
        """ Metodo para estilizar y setear texto de un label 
            Parametros:
                etiqueta: QLabel que se desea modificar\n
                tiutlo: Texto a mostrar\n
                color: color del texto(preferentemente en formato html)\n
                tam: Tamaño de letra\n
                fuente: Fuente de texto(ej: Arial)\n"""
        etiqueta.setText(titulo) 
        etiqueta.setStyleSheet( 'font-size:'+str(tam)+'pt;\n' 
                                'color:'+color+';\n'
                                'font: '+fuente+';\n'
                                'qproperty-alignment: AlignCenter;')

class InterfazAvisos(QWidget):
    """ Esta clase contruye la interfaz para visualizar informacion de una maquina en una pestaña, la misma puede reutilizarse para varias maquinas"""
    def __init__(self,parent,) -> None:
        """ Constructor de la clase donde se aloja todo el codigo que contruye y distribuye todos los componentes graficos(widgets y labels principalmente) que van a contener los datos de la maquina
        Parametros:
            parent: widget del cual va a heredar la clase\n
            sim: Nro de serie de la maquina\n
            Golpes: Golpes de la maquina\n """
        super(QWidget, self).__init__(parent)
        #-----Variables--------
        self.lv=QVBoxLayout()
        self.lh=QHBoxLayout()
        #self.MiGestion=GestionAvisos()
        self.__titulos=('Corte de Energia','Max Temp Superada','Caja Scrap Llena','Cajas Scraps Abiertas','Fallo Seguridad Scraps')
        self.ArrayAvisos=[]
        #-------------Estructuras Estandares---------------------
        for i in range(0,5):
            self.ArrayAvisos.append(EstructuraEstandar(parent,(1,10),grisNegro,azulResaltado,self.__titulos[i],10,'N/A',26))
            self.lh.addWidget(self.ArrayAvisos[i])
        """ self.avisoPiezasMax=EstructuraEstandar(parent,(1,10),grisNegro,azulResaltado,'Caja Scrap Llena',10,'N/A',26)
        self.avisoTempMax=EstructuraEstandar(parent,(1,10),grisNegro,azulResaltado,'Max Temp Superada',10,'N/A',26)
        self.avisoCorteLuz=EstructuraEstandar(parent,(1,10),grisNegro,azulResaltado,'Corte de Energia',10,'N/A',26)
        self.avisoAbertura=EstructuraEstandar(parent,(1,10),grisNegro,azulResaltado,'Cajas Scraps Abiertas',10,'N/A',26)
        self.avisoViolacion=EstructuraEstandar(parent,(1,10),grisNegro,azulResaltado,'Fallo Seguridad Scraps',10,'N/A',26) """

        #-----------Agrego componentes a layout horizontal---------------
        """ self.lh.addWidget(self.avisoPiezasMax)
        self.lh.addWidget(self.avisoTempMax)
        self.lh.addWidget(self.avisoCorteLuz)
        self.lh.addWidget(self.avisoAbertura)
        self.lh.addWidget(self.avisoViolacion) """

        #-----------Agrego componentes a layout vertical---------------
        self.lv.addLayout(self.lh)
        """ self.lv.addWidget(self.avisoAbertura)
        self.lv.addWidget(self.avisoViolacion) """

        #-----------Seteo estiramientos y separacion de margenes en el layout vertical el cual contiene todo----------------
        #self.lv.setStretch(0,2) Entre Componentes Verticales pero como no tengo no hace falta
        self.lv.setContentsMargins(4,4,4,4) #Separacion entre componentes de los margenes creo
        self.setLayout(self.lv)

        #----Hoja de Estilos----
        self.setAttribute(Qt.WA_StyledBackground, True) #Habilito hoja de estilo
        self.setStyleSheet( 'background-color: '+grisIntermedio+';')