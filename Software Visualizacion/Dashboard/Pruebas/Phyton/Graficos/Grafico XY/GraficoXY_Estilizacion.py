import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


fig=plt.figure(facecolor='#33B5FF') #Color de fondo facecolor
grafica=fig.add_subplot(111)


#----------Configuracion Ejes----------------
grafica.axis("off") #Saco ejes
grafica.set(xlim=(0, 12), ylim=(0, 6)) #Rango de Ejes
#grafica.axis('auto')
#-----------Lineas Horizontales--------------
grafica.hlines(y=[1,2,3,4,5,6],xmin=0,xmax=12,color="#000000")
#--------------Etiquetas de Texto----------------------------( con bucles for y tuplas o listas de nombres puedo acortar esta parte)
#Horizontales
grafica.text(-1.5,1,"Texto 1",fontsize=10)
grafica.text(-1.5,2,"Texto 2",fontsize=10)
grafica.text(-1.5,3,"Texto 3",fontsize=10)
grafica.text(-1.5,4,"Texto 4",fontsize=10)
grafica.text(-1.5,5,"Texto 5",fontsize=10)
grafica.text(-1.5,6,"Texto 6",fontsize=10)
#Verticales
grafica.text(0.5,0,"Texto 1",fontsize=10)
grafica.text(1.5,0,"Texto 2",fontsize=10)
grafica.text(2.5,0,"Texto 3",fontsize=10)
grafica.text(3.5,0,"Texto 4",fontsize=10)
grafica.text(4.5,0,"Texto 5",fontsize=10)
grafica.text(5.5,0,"Texto 6",fontsize=10)
grafica.text(6.5,0,"Texto 7",fontsize=10)
grafica.text(7.5,0,"Texto 8",fontsize=10)
grafica.text(8.5,0,"Texto 9",fontsize=10)
grafica.text(9.5,0,"Texto 10",fontsize=10)
grafica.text(10.5,0,"Texto 11",fontsize=10)
grafica.text(11.5,0,"Texto 12",fontsize=10)



grafica.plot([1,6],[1,6],color="Blue") #Recta uno
grafica.fill_between([1,6],[1,6],color="#FF6A6A") #Sombrear debajo de la curva
# grafica.plot([4,5,6,7],[3,2,1,1])       #Recta dos
# grafica.plot([7,12],[1,6])       #Recta tres


plt.ylabel('Algunos Numeros')


plt.show()