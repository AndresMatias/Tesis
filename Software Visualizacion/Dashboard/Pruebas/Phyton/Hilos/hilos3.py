import threading
import time
import datetime 
import logging

class ConsultaAutomatica(threading.Thread):
    def __init__(self,nombre_hilo,numero,d):
        threading.Thread.__init__(self,name=nombre_hilo,target=ConsultaAutomatica.run)# Herencia, cuando ejecuta este hilo, ejecuta el metodo run de esta clase
        self.numero=numero
        self.d=d
    def run(self):
        self.consultaAutomatica()
    def consultaAutomatica(self):
        time.sleep(2)
        self.d.datosCompartidos(3)

class datosCompartidos():
    def __init__(self,numero):
        self.numero=numero
    def datosCompartidos(self,numero):
    	print("\nNumero actual: "+str(self.numero))
    	self.numero=numero
    	print("\nNumero actualizado: "+str(self.numero))
    def imprimirNumero(self):
    	print("\nNumero impreso: "+str(self.numero))
              	


numero=10
d1=datosCompartidos(numero)
d1.imprimirNumero()
t1=ConsultaAutomatica("Hilo_1",numero,d1)
t1.start()
t1.join()
print("Hilo principal")
d1.imprimirNumero()