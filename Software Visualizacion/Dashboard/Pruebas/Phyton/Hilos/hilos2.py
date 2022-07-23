import threading
import time
import datetime 
import logging

class ConsultaAutomatica(threading.Thread):
    def __init__(self,nombre_hilo):
        threading.Thread.__init__(self,name=nombre_hilo,target=ConsultaAutomatica.run)# Herencia, cuando ejecuta este hilo, ejecuta el metodo run de esta clase

    def run(self):
        self.consultaAutomatica()
    def consultaAutomatica(self):
        for i in range(1,10):
        	time.sleep(1)
        	print("Segundos:"+str(i))

t1=ConsultaAutomatica("Hilo_1")
t1.start()
#t1.join()
print("Hilo principal")        	