import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from timeit import default_timer as timer

fig=plt.figure(facecolor='#FFFFFF') #Color de fondo facecolor
grafica=fig.add_subplot(111)

# x=[0,1]
x=np.arange(10)
y=np.zeros(len(x))
color1=['red','blue']

#----------Configuracion Ejes----------------
grafica.axis("off") #Saco ejes
grafica.set(xlim=(0, 12), ylim=(0, 6)) #Rango de Ejes
#grafica.axis('auto')
plt.ylabel('Algunos Numeros')

#--------------Grafico----------------

start =timer() #Inicio para medir tiempo

# for i in range(1,len(x)):
# 	grafica.plot([x[i-1],x[i]],[y[i-1],y[i]],linewidth=100.0,color='blue') #Recta uno

# grafica.plot(x,y,linewidth=100.0,color='blue') #Recta uno

# plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
grafica.scatter(x, y)
end =timer() #Fin para medir tiempo
print ('Tiempo de Ejecucion',end-start)
plt.show()
