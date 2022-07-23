import threading
import time
import datetime 
import logging

def consultar(numero):
	time.sleep(2)
	print("Variable: "+str(numero))

def guardar():
	time.sleep(5)
	print("Hola mundo desde 2do hilo")

tiempo_ini=datetime.datetime.now()
numero=10
t1=threading.Thread(name="hilo_1",target=consultar,args=(numero,)) #Declaro mi hilo
t2=threading.Thread(name="hilo_2",target=guardar) #Declaro mi hilo

t1.start()#Inicio hilo
t2.start()#Inicio hilo
#Digo que el hilo principal se siga ejecutando luego de que se ejecute este hilo, sin esto se ejecuta el principal al mismo tiempo
# t1.join()
# t2.join()

tiempo_fin=datetime.datetime.now()
tiempo_trascurrido=tiempo_fin-tiempo_ini
print("Tiempo transcurrido: "+str(tiempo_trascurrido))
print("Hola mundo desde principal")