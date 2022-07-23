from PyQt5.QtWidgets import QDialog,QCheckBox,QWidget,QVBoxLayout
from PyQt5 import uic
#-----Mis Clases------
from C_Filtros import *
from V_Componentes import ConfigInicial
#-----Clase de Hilos------
from threading import Lock

class VentanaFiltroTMM(QDialog):
    """ Ventana de dialogo que contiene la interfaz para los filtros de Tiempo-Maquinas-Moldes"""
    def __init__(self,sims,moldes,miConsulta):
        QDialog.__init__(self)
        uic.loadUi("V_Filtro_Tiempo_1.ui",self)
        self.setWindowTitle("Filtros") #Texto

        #------Variables--------
        self.__filtroTiempo=(self.year,self.month,self.day,self.turno,self.botonSql1,self.botonSql2) #Widgets donde escojo la fecha a consultar y los botones de consutlar y reiniciar
        self.__labelsFiltrosSims=(self.mm_1,self.mm_2,self.mm_3,self.mm_4,self.mm_5) #Labels de texto para indicar las maquinas escogidas
        self.__labelsFiltrosMoldes=(self.mm_11,self.mm_12,self.mm_13,self.mm_14,self.mm_15) #Labels de texto para indicar los moldes escogidos
        self.__boxS=[] #Va a contener la direccion de los widgets de checkbox de sims
        self.__boxM=[] #Va a contener la direccion de los widgets de checkbox de moldes
        self.__candado=Lock() #Actualmente no utilizo este candado para sincronizar hilos pero lo dejo aca por si llego a poner mas hilos y nececito sincronizar
        #self.__direcWidgetsGraficos=(None,None,self.xy1,self.xy2,self.barras) #tupla con las dirreciones a los widgets de las graficas y textos
        self.llenarYear()

        #------Variables para Scroll Area de Maquinas
        self.__contenedor1=QWidget() #Widget contenedor de sims
        self.__lv1=QVBoxLayout() 
        
        #------Variables para Scroll Area de Moldes
        self.__contenedor2=QWidget() #Widget contenedor de sims
        self.__lv2=QVBoxLayout() 

        #------Instancio Mis Clases--------
        self.__MiFiltroSim=FiltroSimsMoldes(self.__labelsFiltrosSims)
        self.__MiFiltroMolde=FiltroSimsMoldes(self.__labelsFiltrosMoldes)
        self.__MiFiltroTiempo=FiltroTiempo(self.__filtroTiempo,None,miConsulta,None,self.__candado,self.__MiFiltroSim,self.__MiFiltroMolde)

        #------Configuraciones--------
        self.__contenedor1.setLayout(self.__lv1)
        self.scMa.setWidget(self.__contenedor1) #widget de scroll de maquina le seteo el widget que contiene los check box
        self.__contenedor2.setLayout(self.__lv2)
        self.scMo.setWidget(self.__contenedor2) #widget de scroll de moldes le seteo el widget que contiene los check box 
        self.agregarSims(sims)
        self.agregarMoldes(moldes)

        #-----------Conecto señales con slot de la clase de FiltroTiempo---------------
        self.year.activated.connect(self.__MiFiltroTiempo.seleccionYear)
        self.month.activated.connect(self.__MiFiltroTiempo.seleccionMonth)
        self.day.activated.connect(self.__MiFiltroTiempo.seleccionDay)
        self.turno.activated.connect(self.__MiFiltroTiempo.seleccionTurno) #No uso esta señal ni su metodo pero esta comentado mas abajo por si algun llega a usarse para que ya este listo
        self.botonSql1.clicked.connect(self.__MiFiltroTiempo.botonSql1)
        self.botonSql2.clicked.connect(self.__MiFiltroTiempo.botonSql2)
    
    def agregarSims(self,sims):
        """ Metodo para agregar sims al scroll area y conectar con los slot de la clase que gestiona su funcionamiento """
        sim=sims['SIM'].tolist() #Paso el dataframe a una lista
        for i in range(0,len(sim)):
            box=QCheckBox(str(sim[i]))
            box.stateChanged.connect(self.__MiFiltroSim.estadoCheck)
            self.__estilizar(box)
            self.__lv1.addWidget(box)
            self.__boxS.append(box)
        self.__MiFiltroSim.guardarCheckBoxSims(self.__boxS)

    def agregarMoldes(self,moldes):
        """ Metodo para agregar nro de moldes al scroll area y conectar con los slot de la clase que gestiona su funcionamiento """
        nm=moldes['Molde'].tolist() #Nombre molde
        vn=moldes['Vel_Normal'].tolist() #velocidad normal
        vl=moldes['Vel_Lenta'].tolist() #Velocidad lenta
        for i in range(0,len(moldes)):
            box=QCheckBox(str(nm[i]).strip()+' -> vel normal: '+str(vn[i])+' vel lenta: '+str(vl[i]))
            box.stateChanged.connect(self.__MiFiltroMolde.estadoCheck)
            self.__estilizar(box) 
            self.__lv2.addWidget(box)
            self.__boxM.append(box)
        self.__MiFiltroMolde.guardarCheckBoxMoldes(self.__boxM,vn,vl)
    
    def __estilizar(self,box):
        box.setStyleSheet(  'font-size:12pt;\n' 
                                'color:#55ffff;\n'
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