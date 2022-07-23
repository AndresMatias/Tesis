import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

data1=[30]
data2=[20]
data3=[40]
y1=["Periodo Maquina"]
y2=[" "]

y3=["Dia","Mes","Año"]

fig=plt.figure(facecolor='#33B5FF') #Color de fondo facecolor
grafica=fig.add_subplot(111)

#------------Tratamiento en los Ejes---------------------
grafica.axis("off") #Saco Ejes
#grafica.set_xlabel('Tiempo') #Solo funciona con los ejes activados

#---------------------Titulo y Texto-------------------------------
grafica.set_title('Perido de 12 hs') #Titulo
#Tiempos
grafica.text(-0.5,0.15,"Texto 1",fontsize=10)
grafica.text(9.5,0.15,"Texto 2",fontsize=10)
grafica.text(19.5,0.15,"Texto 3",fontsize=10)
grafica.text(29.5,0.15,"Texto 4",fontsize=10)
grafica.text(39.5,0.15,"Texto 5",fontsize=10)




grafica.barh(" ",1,height=0.1,color="#33B5FF") #Para centrar la barra, admite el color en hexadecimal, esta es la posicion 0 en el eje y

grafica.barh(y1,data3,height=0.3,color="green",left=1,label="Python") #Esta es la posicion 1 en el eje y
 
grafica.barh("  ",1,height=0.1,color="#33B5FF") #Para centrar la barra

#grafica.plot([1,2],[1,1],color='red') #Agrego linea blanca para achicar el espacio que ocupa la barra en el grafico 

#grafica.plot([1,2],[0,0],color='red') #Agrego linea blanca para achicar el espacio que ocupa la barra en el grafico

#-----------------------------------Lineas de para diferenciar tiempo------------------------------------
# grafica.axvline(x=1,ymin=0.2,ymax=0.8,color="#000000",linestyle=(0, (2,6))) #Lineas verticales en x
# grafica.axvline(x=11,ymin=0.2,ymax=0.8,color="#000000",linestyle=(0, (2,6))) #Lineas verticales en x
# grafica.axvline(x=21,ymin=0.2,ymax=0.8,color="#000000",linestyle=(0, (2,6))) #Lineas verticales en x
# grafica.axvline(x=31,ymin=0.2,ymax=0.8,color="#000000",linestyle=(0, (2,6))) #Lineas verticales en x
# grafica.axvline(x=41,ymin=0.2,ymax=0.8,color="#000000",linestyle=(0, (2,6))) #Lineas verticales en x
grafica.vlines(x=[1,11,21,31,41],ymin=0.5,ymax=1.5,color="#000000",linestyle=(0, (2,6)))


#----------------------------Perzonalizar LEGEND-------------------------------------------
#grafica.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
custom_lines = [Line2D([0], [0], color="red", lw=4),
                Line2D([0], [0], color="green", lw=4),
                Line2D([0], [0], color="#00FFDC", lw=4)]

#legend=grafica.legend(custom_lines,["OK","NOK","N/D"],labelcolor=['red','green','#00FFDC'],loc=0,bbox_to_anchor=(1,1))
legend=grafica.legend(custom_lines,["OK","NOK","N/D"],labelcolor=['red','green','#00FFDC'],loc=0)
legend.get_frame().set_facecolor('#33B5FF') #Color de fondo de legend

plt.show()
