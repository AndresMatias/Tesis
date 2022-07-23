import threading  
import queue
q = queue.Queue() #Tamaño de cola   
  
class MiThread(threading.Thread):  
    def __init__(self, q):  
        self.q = q  
        threading.Thread.__init__(self)  
  
    def run(self):  
        while True:   
            try:  
                obj= q.get(False)   
            except queue.Empty:  
                print("Fin")   
                break  
            print(obj) 
  
for i in range(10):  
    q.put(i)  
      
t = MiThread(q)  
t.start()  
t.join()