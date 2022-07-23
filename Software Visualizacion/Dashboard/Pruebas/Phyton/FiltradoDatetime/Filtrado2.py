
from datetime import datetime,timedelta,date,time
import pyodbc
import numpy as np
import math

def filtro(fecha):
    if fecha == date(D.year,D.month,D.day):
        #print("Verdadero")
        return True
    else:
        #print("Falso")
        return False

D=datetime.now()
delta=timedelta(days=1)
Fecha=[]
Hora=[]
for i in range(0,6):
    Fecha.append(date(D.year,D.month,D.day)+(delta*(i)))
    Hora.append(time(D.hour,D.minute,D.second))
    # print("Fecha: {0},   Hora:{1}".format(Fecha[i],Hora[i]))
    # print("\n")

Filtrado=list(filter(filtro,Fecha))

for i in Filtrado:
    print(i)
# print(filtrado)    
