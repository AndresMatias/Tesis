import numpy as np
import matplotlib.pyplot as plt


#forma 1: paso un diccionario con 4 claves: 3 de esas claves son los estados de la maquina y cada clave tiene asocioado una tupla con el numero de posicion temporal que sucedio el estado, 4 clave y estado numero total de eventos
#forma 2: una lista que se vaya llenado con el estado de la maquina secuencialmente y ademas paso una tupla de 4 valores q son el tiempo de la ventana de 12 hs aunque por ahora trabajo con porcentajes
#forma 3: ?
#forma 2 de momento me parece lo mejor

#3 estados, funcionando: 1 parada:2 , reparacion:3
#Condiciones para incrementar un contador: que la posicion actual y siguiente sean iguales
#Condicones para crear un nuevo contador: que la siguiente poscion sea distina a la anterior
# lista=[1,1,1,1,2,3,2,2,1,1,1,3,3] #cada posicion se asume un horario que despues puedo asosiarlo con un diccionario
lista=[1,2] #cada posicion se asume un horario que despues puedo asosiarlo con un diccionario
posX=0
year=["Estados de la maquina"]
for i in range(0,len(lista)):
	
	#problema con las etiquetas tengo que ver como poner los labels aparte
	if lista[i]==1:
		plt.barh(year,1,color="yellow",left=posX,label="Funcionando")
	elif lista[i]==2:
		print("Suma: "+str(posX))
		plt.barh(year,1,color="green",left=posX,label="Parada")
	elif lista[i]==3:
		plt.barh(year,1,color="red",left=posX,label="Stan by")	
	else:
		pass
	posX=posX+1 #Determina la poscion en el eje x para graficar la siguiente barra		
#plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
plt.show()				