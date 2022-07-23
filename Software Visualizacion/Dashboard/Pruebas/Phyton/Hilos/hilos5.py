import threading  
import queue
import time
q = queue.Queue() #Tamaño de cola   
  
class MiThread(threading.Thread):  
    def __init__(self,candado):   
        threading.Thread.__init__(self)
        self.__candado=candado  
  
    def run(self):
        candado.acquire()
        print("Inicio hilo 1")  
        for i in range(1,4):   
            time.sleep(0.5)    
            print("a")
        candado.release()    
 
candado=threading.Lock() 
t = MiThread(candado)  
t.start()
#candado.acquire()
for i in range(1,3):   
    time.sleep(0.5)    
    print("b") 
#candado.release()   
#t.join()