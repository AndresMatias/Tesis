import numpy as np
from datetime import datetime,time,timedelta
import matplotlib.pyplot as plt

t1=datetime(2021,1,1,12,0,0,30,tzinfo=None)
t2=datetime(2021,1,1,15,0,0,tzinfo=None)
t3=datetime(2021,1,1,16,0,0,tzinfo=None)
t4=datetime(2021,1,1,17,0,0,0,tzinfo=None)
t5=datetime(2021,1,1,18,0,0,tzinfo=None)

t6=datetime(2021,1,1,18,0,1,300000,tzinfo=None)
t7=datetime(2021,1,1,18,0,0,tzinfo=None)

delta=(t6-t7)
segundos=delta.total_seconds()
print(t1)
print(segundos)

lista=[t1,t2,t3,t4,t5] #cada posicion se asume un horario que despues puedo asosiarlo con un diccionario
posX=0
year=["Estados de la maquina"]

plt.barh(year,segundos,color="yellow",left=posX,label="t1")
# plt.barh(year,1,color="yellow",left=posX,label="t1")
# posX=posX+1 #Determina la poscion en el eje x para graficar la siguiente barra
# plt.barh(year,1,color="green",left=posX,label="t2")
# posX=posX+1 #Determina la poscion en el eje x para graficar la siguiente barra
# plt.barh(year,1,color="red",left=posX,label="t3")
# posX=posX+1 #Determina la poscion en el eje x para graficar la siguiente barra
# plt.barh(year,1,color="blue",left=posX,label="t4")
# posX=posX+1 #Determina la poscion en el eje x para graficar la siguiente barra
# plt.barh(year,1,color="red",left=posX,label="t5")
# posX=posX+1 #Determina la poscion en el eje x para graficar la siguiente barra
			
#plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
plt.show()	





# lista=[1,1,1,1,2,3,2,2,1,1,1,3,3] #cada posicion se asume un horario que despues puedo asosiarlo con un diccionario
# posX=0
# year=["Estados de la maquina"]
# for i in range(0,len(lista)):
	
# 	#problema con las etiquetas tengo que ver como poner los labels aparte
# 	if lista[i]==1:
# 		plt.barh(year,1,color="yellow",left=posX,label="Funcionando")
# 	elif lista[i]==2:
# 		print("Suma: "+str(posX))
# 		plt.barh(year,1,color="green",left=posX,label="Parada")
# 	elif lista[i]==3:
# 		plt.barh(year,1,color="red",left=posX,label="Stan by")	
# 	else:
# 		pass
# 	posX=posX+1 #Determina la poscion en el eje x para graficar la siguiente barra		
# #plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
# plt.show()	